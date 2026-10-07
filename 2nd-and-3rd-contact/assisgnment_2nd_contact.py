import os
import re

# ---------------------------------------------------------------------
# 1. Local File Path (os module)
# ---------------------------------------------------------------------
def display_file_path():
    filepath = os.path.abspath(__file__)
    print("=== 1. LOCAL FILE PATH ===")
    print(f"Current File Path: {filepath}\n")


# ---------------------------------------------------------------------
# 2. Text File Creation & Name Extraction
# ---------------------------------------------------------------------
def extract_name_parts(txt_filename="fullname.txt", default_name="Samuel David Udo"):
    # Create text file with full name
    with open(txt_filename, "w", encoding="utf-8") as f:
        f.write(default_name)

    # Read content from text file
    with open(txt_filename, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # Split and extract name parts
    name_parts = content.split()
    first_name = name_parts[0] if len(name_parts) > 0 else ""
    middle_name = name_parts[1] if len(name_parts) > 2 else ""
    last_name = name_parts[-1] if len(name_parts) > 1 else ""

    print("=== 2. NAME EXTRACTION FROM FILE ===")
    print(f"Full Text Read: {content}")
    print(f"First Name:    {first_name}")
    print(f"Middle Name:   {middle_name}")
    print(f"Last Name:     {last_name}\n")


# ---------------------------------------------------------------------
# 3. Custom Sorting Algorithm (QuickSort)
# ---------------------------------------------------------------------
def custom_quicksort(data_list):
    """Sorts a list of tuples (name, rank) alphabetically by name."""
    if len(data_list) <= 1:
        return data_list
    
    pivot = data_list[len(data_list) // 2]
    left = [item for item in data_list if item[0].lower() < pivot[0].lower()]
    middle = [item for item in data_list if item[0].lower() == pivot[0].lower()]
    right = [item for item in data_list if item[0].lower() > pivot[0].lower()]
    
    return custom_quicksort(left) + middle + custom_quicksort(right)


# ---------------------------------------------------------------------
# 4. Custom Binary Search
# ---------------------------------------------------------------------
def binary_search(sorted_list, target_name):
    """Searches for target_name in a sorted list of (name, rank) tuples."""
    low = 0
    high = len(sorted_list) - 1
    target = target_name.lower()

    while low <= high:
        mid = (low + high) // 2
        current_name = sorted_list[mid][0].lower()

        if current_name == target:
            return sorted_list[mid]
        elif current_name < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


# ---------------------------------------------------------------------
# 5. Extract Baby Names via Regex & Execute Algorithms
# ---------------------------------------------------------------------
def process_baby_names(html_filename="baby2008.html"):
    print("=== 3. REGEX EXTRACTION, SORT & BINARY SEARCH ===")
    if not os.path.exists(html_filename):
        print(f"Error: Could not find '{html_filename}'. Make sure it is in this directory.")
        return []

    with open(html_filename, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Match format: <td>Rank</td><td>Boy Name</td><td>Girl Name</td>
    raw_entries = re.findall(r'<td>(\d+)</td>\s*<td>(\w+)</td>\s*<td>(\w+)</td>', html_content)

    # Store unique names with rank
    unique_names = {}
    for rank, boy, girl in raw_entries:
        if boy not in unique_names:
            unique_names[boy] = rank
        if girl not in unique_names:
            unique_names[girl] = rank

    # Convert to list of tuples: [("Name", "Rank"), ...]
    names_list = list(unique_names.items())

    # Custom Sort
    sorted_names = custom_quicksort(names_list)
    print(f"Extracted {len(sorted_names)} unique baby names.")
    print(f"First 5 Sorted Names: {sorted_names[:5]}")

    # Custom Binary Search Test
    query = "Michael"
    search_result = binary_search(sorted_names, query)
    
    if search_result:
        print(f"Binary Search Result for '{query}': Found at Rank {search_result[1]}\n")
    else:
        print(f"Binary Search Result for '{query}': Not found\n")

    return sorted_names


if __name__ == "__main__":
    display_file_path()
    extract_name_parts()
    process_baby_names()