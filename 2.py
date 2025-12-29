import pyodbc

# ✅ Connect to SQL Server
try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=Munikumar\\SQLEXPRESS;'     # Double backslash for Python
        'DATABASE=STUDENT;'
        'Trusted_Connection=yes;'
    )
    print("✅ Connected to SQL Server successfully!")
except pyodbc.Error as e:
    print("❌ Connection failed:", e)
    exit()

cursor = conn.cursor()

# --- Function to insert College data ---
def insert_college():
    n = int(input("How many colleges do you want to insert? "))
    for _ in range(n):
        college_id = input("Enter College ID: ")
        college_name = input("Enter College Name: ")
        cursor.execute("INSERT INTO College (college_id, college_name) VALUES (?, ?)", (college_id, college_name))
    conn.commit()
    print("✅ College data inserted successfully!")

# --- Function to insert Branch data ---
def insert_branch():
    n = int(input("How many branches do you want to insert? "))
    for _ in range(n):
        branch_id = int(input("Enter Branch ID: "))
        college_id = input("Enter College ID (must exist): ")
        branch_name = input("Enter Branch Name: ")
        cursor.execute("INSERT INTO Branch (branch_id, college_id, branch_name) VALUES (?, ?, ?)", 
                       (branch_id, college_id, branch_name))
    conn.commit()
    print("✅ Branch data inserted successfully!")

# --- Function to insert Semester data ---
def insert_semester():
    n = int(input("How many semesters do you want to insert? "))
    for _ in range(n):
        semester_id = int(input("Enter Semester ID: "))
        semester_name = input("Enter Semester Name: ")
        cursor.execute("INSERT INTO Semester (semester_id, semester_name) VALUES (?, ?)", (semester_id, semester_name))
    conn.commit()
    print("✅ Semester data inserted successfully!")

# --- Function to insert Student data ---
def insert_student():
    n = int(input("How many students do you want to insert? "))
    for _ in range(n):
        student_id = int(input("Enter Student ID: "))
        student_name = input("Enter Student Name: ")
        college_id = input("Enter College ID: ")
        branch_id = int(input("Enter Branch ID: "))
        cursor.execute("INSERT INTO Student (student_id, student_name, college_id, branch_id) VALUES (?, ?, ?, ?)", 
                       (student_id, student_name, college_id, branch_id))
    conn.commit()
    print("✅ Student data inserted successfully!")

# --- Function to insert Marks data ---
def insert_marks():
    n = int(input("How many marks records do you want to insert? "))
    for _ in range(n):
        student_id = int(input("Enter Student ID: "))
        semester_id = int(input("Enter Semester ID: "))
        subject = input("Enter Subject Name: ")
        marks = int(input("Enter Marks: "))
        total = int(input("Enter Total Marks: "))
        cursor.execute("INSERT INTO Marks (student_id, semester_id, subject, marks, total) VALUES (?, ?, ?, ?, ?)", 
                       (student_id, semester_id, subject, marks, total))
    conn.commit()
    print("✅ Marks data inserted successfully!")

# --- Menu for selection ---
while True:
    print("\n--- Choose an option to insert data ---")
    print("1. Insert College")
    print("2. Insert Branch")
    print("3. Insert Semester")
    print("4. Insert Student")
    print("5. Insert Marks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        insert_college()
    elif choice == '2':
        insert_branch()
    elif choice == '3':
        insert_semester()
    elif choice == '4':
        insert_student()
    elif choice == '5':
        insert_marks()
    elif choice == '6':
        print("👋 Exiting program...")
        break
    else:
        print("⚠️ Invalid choice. Try again.")

# ✅ Close connection
cursor.close()
conn.close()
print("✅ All data inserted and connection closed successfully.")
