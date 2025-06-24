import json
import math
import argparse
import numpy as np
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

# --- Configuration ---
# Tolerance for determining if a point lies on a line (distance from line).
LINE_TOLERANCE = 0.1  # meters
# Tolerance for determining if a point lies on an arc (difference in distance from center).
ARC_TOLERANCE = 0.2  # meters
# Minimum number of points to define a valid arc.
MIN_ARC_POINTS = 3
# Earth radius in meters for projection
EARTH_RADIUS = 6378137.0


def project_latlon_to_xy(coords):
    """
    Projects a list of [lon, lat] coordinates to a local a XY meter-based system.
    Uses an equirectangular projection, which is good for local areas.
    The first point is used as the reference (0, 0) origin.
    """
    projected_coords = []

    # Check if coords has at least one point
    if not coords:
        return []

    ref_lon, ref_lat = coords[0]
    ref_lat_rad = math.radians(ref_lat)

    for lon, lat in coords:
        lat_rad = math.radians(lat)

        x = EARTH_RADIUS * (math.radians(lon) - math.radians(ref_lon)) * math.cos(ref_lat_rad)
        y = EARTH_RADIUS * (lat_rad - ref_lat_rad)

        projected_coords.append([x, y])

    return projected_coords


class GeometryFitter:
    """
    Analyzes a sequence of points and fits OpenDRIVE line and arc geometries.
    """

    def __init__(self, points):
        if not isinstance(points, np.ndarray):
            self.points = np.array(points)
        else:
            self.points = points
        self.geometries = []
        self.s_offset = 0.0

    def fit(self):
        """
        Main fitting function to process all points.
        """
        idx = 0
        while idx < len(self.points) - 1:
            # Try to fit the longest possible arc first, then a line.
            end_idx_arc = self._fit_arc(idx)
            end_idx_line = self._fit_line(idx)

            # Choose the fit that covers more points.
            if end_idx_arc > end_idx_line:
                # Add Arc
                self._add_arc_geometry(idx, end_idx_arc)
                idx = end_idx_arc
            else:
                # Add Line
                self._add_line_geometry(idx, end_idx_line)
                idx = end_idx_line
        return self.geometries

    def _fit_line(self, start_idx):
        """Tries to fit the longest possible line from a starting index."""
        if start_idx >= len(self.points) - 1:
            return start_idx

        p1 = self.points[start_idx]
        p2 = self.points[start_idx + 1]

        # Handle case where p1 and p2 are the same point
        if np.allclose(p1, p2):
            return start_idx + 1

        direction_vector = p2 - p1

        end_idx = start_idx + 1
        for i in range(start_idx + 2, len(self.points)):
            p_current = self.points[i]
            # Calculate perpendicular distance from point to the line defined by p1 and p2
            distance = np.abs(np.cross(direction_vector, p_current - p1)) / np.linalg.norm(direction_vector)
            if distance > LINE_TOLERANCE:
                break
            end_idx = i
        return end_idx

    def _fit_arc(self, start_idx):
        """Tries to fit the longest possible arc from a starting index."""
        if start_idx >= len(self.points) - MIN_ARC_POINTS:
            return -1  # Cannot form an arc

        # Get initial 3 points to define the arc
        p1, p2, p3 = self.points[start_idx], self.points[start_idx + 1], self.points[start_idx + 2]

        # Fit a circle through 3 points
        res = self._get_circle_center_radius(p1, p2, p3)
        if res is None:
            return -1  # Collinear points, not an arc

        center, radius = res

        end_idx = start_idx + 2
        for i in range(start_idx + 3, len(self.points)):
            p_current = self.points[i]
            dist_to_center = np.linalg.norm(p_current - center)
            if abs(dist_to_center - radius) > ARC_TOLERANCE:
                break
            end_idx = i
        return end_idx

    def _add_line_geometry(self, start_idx, end_idx):
        p_start = self.points[start_idx]
        p_end = self.points[end_idx]

        # Recalculate length along the polyline for more accuracy
        path_length = np.sum(np.linalg.norm(np.diff(self.points[start_idx:end_idx + 1], axis=0), axis=1))

        if path_length < 1e-6: return

        heading = math.atan2(p_end[1] - p_start[1], p_end[0] - p_start[0])

        self.geometries.append({
            'type': 'line',
            's': self.s_offset,
            'x': p_start[0],
            'y': p_start[1],
            'hdg': heading,
            'length': path_length,
        })
        self.s_offset += path_length

    def _add_arc_geometry(self, start_idx, end_idx):
        points_in_arc = self.points[start_idx:end_idx + 1]
        p_start = points_in_arc[0]
        p_mid = points_in_arc[len(points_in_arc) // 2]
        p_end = points_in_arc[-1]

        res = self._get_circle_center_radius(p_start, p_mid, p_end)
        if res is None:  # Should not happen if _fit_arc passed, but as a safeguard
            self._add_line_geometry(start_idx, end_idx)
            return

        _, radius = res
        curvature = 1.0 / radius

        vec1 = p_mid - p_start
        vec2 = p_end - p_mid
        if np.cross(vec1, vec2) < 0:
            curvature = -curvature  # Right turn

        p_next = self.points[start_idx + 1]
        heading = math.atan2(p_next[1] - p_start[1], p_next[0] - p_start[0])

        arc_length = np.sum(np.linalg.norm(np.diff(points_in_arc, axis=0), axis=1))

        if arc_length < 1e-6: return

        self.geometries.append({
            'type': 'arc',
            's': self.s_offset,
            'x': p_start[0],
            'y': p_start[1],
            'hdg': heading,
            'length': arc_length,
            'curvature': curvature,
        })
        self.s_offset += arc_length

    @staticmethod
    def _get_circle_center_radius(p1, p2, p3):
        """Calculates the center and radius of a circle passing through 3 points."""
        d21 = p2 - p1
        d31 = p3 - p1

        if abs(np.cross(d21, d31)) < 1e-9:
            return None

        a = np.linalg.norm(d21)
        b = np.linalg.norm(d31)
        c = np.linalg.norm(p2 - p3)

        radius = (a * b * c) / (2 * abs(np.cross(d21, d31)))

        alpha = np.linalg.norm(p3 - p2) ** 2 * (d21 @ d31) / (2 * np.linalg.norm(np.cross(d21, d31)) ** 2)
        beta = np.linalg.norm(d31) ** 2 * (-d21 @ (p3 - p2)) / (2 * np.linalg.norm(np.cross(d21, d31)) ** 2)
        gamma = 1 - alpha - beta

        center = alpha * p1 + beta * p2 + gamma * p3
        return center, radius


def create_opendrive_xml(geometries, road_id="1", road_length=1000.0):
    """
    Generates the OpenDRIVE XML structure from the fitted geometries.
    """
    odr = Element('OpenDRIVE')
    header = SubElement(odr, 'header', revMajor="1", revMinor="6", name="", version="1.00",
                        date="Wed Sep 26 12:00:00 2023")
    road = SubElement(odr, 'road', name="Converted Road", length=f"{road_length:.16e}", id=road_id, junction="-1")

    plan_view = SubElement(road, 'planView')
    for geom in geometries:
        g = SubElement(plan_view, 'geometry',
                       s=f"{geom['s']:.16e}",
                       x=f"{geom['x']:.16e}",
                       y=f"{geom['y']:.16e}",
                       hdg=f"{geom['hdg']:.16e}",
                       length=f"{geom['length']:.16e}")
        if geom['type'] == 'line':
            SubElement(g, 'line')
        elif geom['type'] == 'arc':
            SubElement(g, 'arc', curvature=f"{geom['curvature']:.16e}")

    lanes = SubElement(road, 'lanes')
    lane_section = SubElement(lanes, 'laneSection', s="0.0")

    center = SubElement(lane_section, 'center')
    SubElement(center, 'lane', id="0", type="driving", level="false")

    right = SubElement(lane_section, 'right')
    lane_right = SubElement(right, 'lane', id="-1", type="driving", level="false")
    SubElement(lane_right, 'width', sOffset="0.0", a="3.5", b="0", c="0", d="0")

    left = SubElement(lane_section, 'left')
    lane_left = SubElement(left, 'lane', id="1", type="driving", level="false")
    SubElement(lane_left, 'width', sOffset="0.0", a="3.5", b="0", c="0", d="0")

    xml_str = tostring(odr, 'utf-8')
    pretty_xml_str = minidom.parseString(xml_str).toprettyxml(indent="  ")
    return pretty_xml_str


def main():
    parser = argparse.ArgumentParser(description="Convert GeoJSON LineString or Polygon to an OpenDRIVE (.xodr) file.")
    parser.add_argument("input_geojson", help="Path to the input GeoJSON file.")
    parser.add_argument("output_xodr", help="Path for the output OpenDRIVE file.")
    args = parser.parse_args()

    try:
        with open(args.input_geojson, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file not found at {args.input_geojson}")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {args.input_geojson}")
        return

    # Find the first LineString or Polygon in the GeoJSON
    coords = None
    if data['type'] == 'FeatureCollection':
        for feature in data['features']:
            geom_type = feature['geometry']['type']
            if geom_type == 'LineString':
                coords = feature['geometry']['coordinates']
                print("Found LineString feature.")
                break
            elif geom_type == 'Polygon':
                # For a Polygon, use the first (exterior) ring of coordinates
                coords = feature['geometry']['coordinates'][0]
                print("Found Polygon feature, using its exterior boundary.")
                break
    # Add checks for single features as well
    elif data['type'] == 'Feature':
        geom_type = data['geometry']['type']
        if geom_type == 'LineString':
            coords = data['geometry']['coordinates']
            print("Found LineString feature.")
        elif geom_type == 'Polygon':
            coords = data['geometry']['coordinates'][0]
            print("Found Polygon feature, using its exterior boundary.")

    if coords is None:
        print("Error: No LineString or Polygon feature found in the GeoJSON file.")
        return

    print(f"Extracted path with {len(coords)} points.")

    # Remove Z coordinate if present and project to local XY meters
    lon_lat_coords = [c[:2] for c in coords]
    print("Projecting Lat/Lon coordinates to a local XY grid (meters)...")
    points_2d = project_latlon_to_xy(lon_lat_coords)

    # Fit geometries
    fitter = GeometryFitter(points_2d)
    geometries = fitter.fit()

    if not geometries:
        print("Error: Could not generate any geometries from the provided points.")
        return

    print(f"Fitted {len(geometries)} geometries (lines and arcs).")

    # Generate OpenDRIVE XML
    total_length = fitter.s_offset
    opendrive_xml = create_opendrive_xml(geometries, road_length=total_length)

    # Write output file
    with open(args.output_xodr, 'w') as f:
        f.write(opendrive_xml)

    print(f"Successfully converted to {args.output_xodr}")


if __name__ == '__main__':
    main()