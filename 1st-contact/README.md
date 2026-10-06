# 1st Contact Session Assignment - Package Setup

This folder contains the setup and import verification script for the required Python libraries.

## Installed Libraries
* `psycopg2-binary`
* `mysqlclient` (provides `MySQLdb` for Python 3)
* `urllib3`
* `scipy`
* `numpy`
* `pandas`
* `matplotlib`

## Python 3 Package Compatibility Notes
* **`urllib` & `urllib2`:** Standard library modules (`urllib.request`, `urllib.parse`) in Python 3; no separate `pip` installation required.
* **`mysqldb`:** Installed via the `mysqlclient` package.
* **`psycopg2`:** Installed using `psycopg2-binary` for pre-compiled binaries.

## How to Verify
1. Activate the virtual environment:
   ```powershell
   ..\venv\Scripts\Activate.ps1