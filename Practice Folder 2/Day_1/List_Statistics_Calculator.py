"""
Given a list of integers, write a function analyze_list(numbers) that calculates and returns the primary statistical properties.

The function must return a dictionary with three keys:
1. Mean
2. Median
3. Mode
"""

def analyze_list(numbers):
    # validate
    if not numbers or not all(isinstance(num, int) for num in numbers):
        return False

    # Mean
    mean_val = sum(numbers) / len(numbers)

    # Median (manual calculation)
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 1:  # odd length
        median_val = sorted_nums[mid]
    else:  # even length
        median_val = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

    # Mode (still using count to find the most frequent)
    counts = {}
    for num in sorted_nums:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    mode_val = modes[0] if len(modes) == 1 else "No unique mode"

    return {
        "Mean": mean_val,
        "Median": median_val,
        "Mode": mode_val
    }
