# 2nd & 3rd Contact Session Assignments

This directory contains Python scripts combining the deliverables for both the 2nd and 3rd Contact Session assignments, covering file parsing, custom algorithms, regular expressions, generator functions, and PostgreSQL database integration.

## 📁 Folder Contents

- `assignment_2nd_contact.py` – Script for OS path display, name parsing, regex extraction, custom QuickSort, and Binary Search.
- `assignment_3rd_contact.py` – Script for Fibonacci generator, To-Do List CRUD operations, and baby names PostgreSQL database import.
- `fullname.txt` – Text file containing the full name for parsing.
- `baby2008.html` – Raw Social Security Administration HTML dataset.
- `requirements.txt` – Project dependencies (`psycopg2-binary`).

## ⚙️ What the Code Does

### 2nd Contact Session Assignment

- OS File Path: Prints the script's absolute local file path using the `os` library.
- Name Extraction: Reads `fullname.txt` and extracts first, middle, and last names.
- Regex Extraction: Parses ranks and names from `baby2008.html` without external HTML libraries.
- Custom Sort: Sorts extracted names alphabetically using a custom QuickSort algorithm (no built-in sort()).
- Binary Search: Performs a O(log n) binary search lookup for specific name rankings.

### 3rd Contact Session Assignment

- Fibonacci Generator: Computes Fibonacci series terms using a Python generator (`yield`).
- PostgreSQL CRUD: Establishes database connection using `psycopg2` to execute Create, Read, Update, and Delete operations on a `todos` table.
- Database Import: Bulk inserts regex-extracted baby names into a PostgreSQL `baby_names` table.

## 🚀 How to Run

### Activate Virtual Environment

PowerShell:
```powershell
..\venv\Scripts\Activate.ps1
```

### Install Dependencies

PowerShell:
```powershell
pip install -r requirements.txt
```

### Configure PostgreSQL Credentials

Ensure PostgreSQL is running locally and update `DB_CONFIG` in `assignment_3rd_contact.py`:

```python
DB_CONFIG = {
    "dbname": "bincom_db",
    "user": "postgres",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}
```

### Execute Scripts

PowerShell:
```powershell
python assignment_2nd_contact.py
python assignment_3rd_contact.py
```
