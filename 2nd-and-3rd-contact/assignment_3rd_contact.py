import os
import re
import psycopg2

# Database Connection Details (Adjust to match your PostgreSQL setup)
DB_CONFIG = {
    "dbname": "bincom_db",
    "user": "postgres",
    "password": "UDBATMAN",  # Update with your DB password
    "host": "localhost",
    "port": "5432"
}

# ---------------------------------------------------------------------
# 1. Fibonacci Series Generator
# ---------------------------------------------------------------------
def fibonacci_generator(n_terms):
    """Yields Fibonacci sequence up to n terms."""
    a, b = 0, 1
    count = 0
    while count < n_terms:
        yield a
        a, b = b, a + b
        count += 1


# ---------------------------------------------------------------------
# 2. Database Setup & Table Creation
# ---------------------------------------------------------------------
def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

def init_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Create To-Do table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            task TEXT NOT NULL,
            completed BOOLEAN DEFAULT FALSE
        );
    """)

    # Create Baby Names table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS baby_names (
            id SERIAL PRIMARY KEY,
            year VARCHAR(4),
            rank INT,
            name VARCHAR(100),
            gender VARCHAR(10)
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


# ---------------------------------------------------------------------
# 3. To-Do List CRUD Operations
# ---------------------------------------------------------------------
def create_todo(task):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO todos (task) VALUES (%s) RETURNING id;", (task,))
    todo_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    print(f"[CRUD CREATE] Added Task ID {todo_id}: '{task}'")

def read_todos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, task, completed FROM todos ORDER BY id ASC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    print("\n=== TO-DO LIST ITEMS ===")
    for r in rows:
        status = "✓ Done" if r[2] else "✗ Pending"
        print(f"[{r[0]}] {r[1]} - {status}")
    print("========================\n")

def update_todo(todo_id, completed=True):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE todos SET completed = %s WHERE id = %s;", (completed, todo_id))
    conn.commit()
    cur.close()
    conn.close()
    print(f"[CRUD UPDATE] Marked Task ID {todo_id} as completed.")

def delete_todo(todo_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM todos WHERE id = %s;", (todo_id,))
    conn.commit()
    cur.close()
    conn.close()
    print(f"[CRUD DELETE] Deleted Task ID {todo_id}.")


# ---------------------------------------------------------------------
# 4. Save Extracted Baby Names into PostgreSQL
# ---------------------------------------------------------------------
def save_baby_names_to_postgres(html_filename="baby2008.html"):
    if not os.path.exists(html_filename):
        print(f"Error: {html_filename} not found.")
        return

    with open(html_filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract year
    year_match = re.search(r'Popularity in (\d{4})', content)
    year = year_match.group(1) if year_match else "2008"

    # Extract rank, boy_name, girl_name
    entries = re.findall(r'<td>(\d+)</td>\s*<td>(\w+)</td>\s*<td>(\w+)</td>', content)

    conn = get_db_connection()
    cur = conn.cursor()

    # Clear existing data to avoid duplicate runs
    cur.execute("TRUNCATE TABLE baby_names;")

    records = []
    for rank, boy, girl in entries:
        records.append((year, int(rank), boy, 'boy'))
        records.append((year, int(rank), girl, 'girl'))

    cur.executemany(
        "INSERT INTO baby_names (year, rank, name, gender) VALUES (%s, %s, %s, %s);",
        records
    )

    conn.commit()
    cur.close()
    conn.close()
    print(f"[POSTGRES] Saved {len(records)} baby name entries into 'baby_names' table.")


# ---------------------------------------------------------------------
# Main Execution
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # 1. Test Fibonacci
    print("=== FIBONACCI SERIES (10 Terms) ===")
    fib_series = list(fibonacci_generator(10))
    print(f"Fibonacci Output: {fib_series}\n")

    # 2. Database operations (Ensure PostgreSQL service is running and DB config is correct)
    try:
        init_tables()

        # To-Do CRUD Test
        create_todo("Complete Bincom 2nd Contact Assignment")
        create_todo("Complete Bincom 3rd Contact Assignment")
        read_todos()
        update_todo(1, completed=True)
        read_todos()
        delete_todo(2)
        read_todos()

        # Save Regex Extracted Baby Names to DB
        save_baby_names_to_postgres("baby2008.html")

    except Exception as e:
        print(f"\nDatabase Error: {e}")
        print("Note: Update DB_CONFIG at top of script with your PostgreSQL username, password, and database name.")