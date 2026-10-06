import os
import re

# ----------------------------------------------------
# 1. Custom Sorting Algorithm (Merge Sort from Scratch)
# ----------------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].lower() <= right[j].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ----------------------------------------------------
# 2. Custom Binary Search Implementation
# ----------------------------------------------------
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    target_lower = target.lower()

    while low <= high:
        mid = (low + high) // 2
        current = arr[mid].lower()

        if current == target_lower:
            return mid  # Found target at index 'mid'
        elif current < target_lower:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Not found


# ----------------------------------------------------
# 3. Main Script: Extract Names using Regex
# ----------------------------------------------------
def main():
    file_path = os.path.join(os.path.dirname(__file__), "baby2008.html")
    
    if not os.path.exists(file_path):
        print(f"Error: Could not find 'baby2008.html' at {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Regex pattern to match table rows: <td>rank</td><td>boy_name</td><td>girl_name</td>
    pattern = r'<td>(\d+)</td>\s*<td>(\w+)</td>\s*<td>(\w+)</td>'
    matches = re.findall(pattern, html_content)

    names = []
    for rank, boy_name, girl_name in matches:
        names.append(boy_name)
        names.append(girl_name)

    print(f"Extracted {len(names)} total baby names using Regex.")

    # Sort names using custom merge sort
    sorted_names = merge_sort(names)
    print("Names sorted successfully using custom Merge Sort algorithm.")

    # Search for a name using Binary Search
    target_name = "Samuel"
    index = binary_search(sorted_names, target_name)

    print("==========================================")
    if index != -1:
        print(f"Binary Search: Found '{target_name}' at index {index} in sorted array!")
    else:
        print(f"Binary Search: '{target_name}' was not found in the list.")
    print("==========================================")

if __name__ == "__main__":
    main()