import os

# 1. Using 'os' library to get and print absolute file path
script_path = os.path.abspath(__file__)
print("==========================================")
print(f"Local File Path: {script_path}")
print("==========================================\n")

# 2. Read full name from text file
txt_file_path = os.path.join(os.path.dirname(__file__), "fullname.txt")

with open(txt_file_path, "r") as file:
    full_name = file.read().strip()

# Extract names
name_parts = full_name.split()
first_name = name_parts[0] if len(name_parts) > 0 else ""
middle_name = name_parts[1] if len(name_parts) > 2 else ""
last_name = name_parts[-1] if len(name_parts) > 1 else ""

print("Extracted Name Components:")
print(f"Full Name:   {full_name}")
print(f"First Name:  {first_name}")
print(f"Middle Name: {middle_name}")
print(f"Last Name:   {last_name}")