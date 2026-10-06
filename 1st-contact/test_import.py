# 1st-contact/test_imports.py

import numpy as np
import pandas as pd
import matplotlib
import scipy
import urllib3
import psycopg2
import MySQLdb
import urllib.request  # Python 3 standard library equivalent of urllib/urllib2

def verify_installations():
    print("==========================================")
    print(" 1st Contact Assignment - Import Verification")
    print("==========================================")
    print(f"NumPy Version:      {np.__version__}")
    print(f"Pandas Version:     {pd.__version__}")
    print(f"Matplotlib Version: {matplotlib.__version__}")
    print(f"SciPy Version:      {scipy.__version__}")
    print(f"urllib3 Version:    {urllib3.__version__}")
    print(f"psycopg2 Version:   {psycopg2.__version__}")
    print(f"MySQLdb Version:    {MySQLdb.__version__}")
    print("==========================================")
    print("SUCCESS: All required packages installed and working!")

if __name__ == "__main__":
    verify_installations()