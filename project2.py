import pyodbc
import random

# Check available ODBC drivers
print("Available ODBC drivers:", pyodbc.drivers())

# Set random seed for reproducible marks
random.seed(42)

# SQL Server connection details
server = 'Munikumar\SQLEXPRESS'  # Replace with your server name (e.g., '.\SQLEXPRESS' if using SQL Server Express)
database ='COLLEGEDB'
driver = 'SQL Server'  # Replace with an available driver from pyodbc.drivers()

# Connection string (Windows authentication)
connection_string = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
# For SQL authentication: f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Initialize connection and cursor variables
conn = None
cursor = None

try:
    # Establish connection
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("Connected to SQL Server")

    # 1. Insert into Students Table (2 students per branch, 5 branches = 10 students)
    students_data = [
        ('S001', 'John', 'Doe', 'Computer Science', 'Male'),
        ('S002', 'Emma', 'Davis', 'Computer Science', 'Female'),
        ('S003', 'Jane', 'Smith', 'Mechanical', 'Female'),
        ('S004', 'Robert', 'Johnson', 'Mechanical', 'Male'),
        ('S005', 'Alex', 'Brown', 'Electrical', 'Male'),
        ('S006', 'Lisa', 'Taylor', 'Electrical', 'Female'),
        ('S007', 'Sarah', 'Wilson', 'Civil', 'Female'),
        ('S008', 'David', 'Clark', 'Civil', 'Male'),
        ('S009', 'Michael', 'Lee', 'Electronics', 'Male'),
        ('S010', 'Sophia', 'Martinez', 'Electronics', 'Female')
    ]

    cursor.executemany("""
        INSERT INTO Students (Student_ID, First_Name, Last_Name, Branch, Gender)
        VALUES (?, ?, ?, ?, ?)
    """, students_data)
    print(f"Inserted {len(students_data)} students into Students table")

    # 2. Insert into Subjects Table (4 subjects per semester, 8 semesters, 5 branches = 160 subjects)
    subject_templates = {
        'Computer Science': [
            ['Data Structures', 'Programming in C', 'Mathematics I', 'Digital Logic'],
            ['Algorithms', 'Object-Oriented Programming', 'Mathematics II', 'Computer Organization'],
            ['Database Systems', 'Operating Systems', 'Discrete Mathematics', 'Software Engineering'],
            ['Computer Networks', 'Web Development', 'Probability & Statistics', 'Artificial Intelligence'],
            ['Machine Learning', 'Cloud Computing', 'Linear Algebra', 'Cybersecurity'],
            ['Distributed Systems', 'Mobile Computing', 'Numerical Methods', 'Data Science'],
            ['Big Data Analytics', 'Compiler Design', 'Optimization Techniques', 'IoT'],
            ['Advanced AI', 'Blockchain', 'Project Management', 'Capstone Project']
        ],
        'Mechanical': [
            ['Mechanics', 'Thermodynamics', 'Engineering Drawing', 'Mathematics I'],
            ['Fluid Mechanics', 'Material Science', 'Manufacturing Processes', 'Mathematics II'],
            ['Dynamics', 'Heat Transfer', 'Machine Design', 'Strength of Materials'],
            ['Control Systems', 'Automotive Engineering', 'Kinematics', 'Probability & Statistics'],
            ['Robotics', 'Energy Systems', 'CAD/CAM', 'Numerical Methods'],
            ['Mechatronics', 'Finite Element Analysis', 'Fluid Dynamics', 'Industrial Engineering'],
            ['Vibration Analysis', 'Renewable Energy', 'Operations Research', 'Thermal Engineering'],
            ['Advanced Manufacturing', 'HVAC Systems', 'Project Management', 'Capstone Project']
        ],
        'Electrical': [
            ['Circuits', 'Electronics', 'Mathematics I', 'Electromagnetic Fields'],
            ['Analog Electronics', 'Power Systems', 'Mathematics II', 'Signals & Systems'],
            ['Digital Electronics', 'Control Systems', 'Electrical Machines', 'Network Analysis'],
            ['Power Electronics', 'Microprocessors', 'Probability & Statistics', 'Instrumentation'],
            ['Renewable Energy', 'Embedded Systems', 'Linear Algebra', 'High Voltage Engineering'],
            ['Digital Signal Processing', 'Smart Grids', 'Numerical Methods', 'Communication Systems'],
            ['Power System Protection', 'VLSI Design', 'Optimization Techniques', 'IoT'],
            ['Advanced Control Systems', 'Electric Vehicles', 'Project Management', 'Capstone Project']
        ],
        'Civil': [
            ['Structural Analysis', 'Fluid Mechanics', 'Mathematics I', 'Surveying'],
            ['Concrete Technology', 'Geotechnical Engineering', 'Mathematics II', 'Environmental Engineering'],
            ['Steel Structures', 'Transportation Engineering', 'Hydraulics', 'Strength of Materials'],
            ['Earthquake Engineering', 'Construction Management', 'Probability & Statistics', 'Water Resources'],
            ['Bridge Design', 'Soil Mechanics', 'Linear Algebra', 'Urban Planning'],
            ['Structural Dynamics', 'Pavement Design', 'Numerical Methods', 'GIS'],
            ['Advanced Structural Analysis', 'Infrastructure Planning', 'Operations Research', 'Green Buildings'],
            ['Construction Costing', 'Disaster Management', 'Project Management', 'Capstone Project']
        ],
        'Electronics': [
            ['Microelectronics', 'Control Systems', 'Mathematics I', 'Analog Circuits'],
            ['Digital Circuits', 'Communication Systems', 'Mathematics II', 'Embedded Systems'],
            ['VLSI Design', 'Signal Processing', 'Electronic Devices', 'Network Theory'],
            ['Wireless Communication', 'Microcontrollers', 'Probability & Statistics', 'RF Engineering'],
            ['IoT', 'Analog IC Design', 'Linear Algebra', 'Power Electronics'],
            ['Digital Communication', 'Robotics', 'Numerical Methods', 'Sensor Technology'],
            ['Advanced VLSI', 'Optical Communication', 'Optimization Techniques', 'Embedded IoT'],
            ['Satellite Communication', 'Machine Vision', 'Project Management', 'Capstone Project']
        ]
    }

    subjects_data = []
    subject_id = 1
    for branch in subject_templates.keys():
        for semester in range(1, 9):
            for subject_name in subject_templates[branch][semester - 1]:
                subjects_data.append((f'SUB{subject_id:03d}', subject_name, branch, semester))
                subject_id += 1

    cursor.executemany("""
        INSERT INTO Subjects (Subject_ID, Subject_Name, Branch, Semester)
        VALUES (?, ?, ?, ?)
    """, subjects_data)
    print(f"Inserted {len(subjects_data)} subjects into Subjects table")

    # 3. Insert into Semester_Marks Table (marks for 10 students, 4 subjects × 8 semesters = 320 marks)
    marks_data = []
    for student in students_data:
        student_id = student[0]
        branch = student[3]
        # Filter subjects for this student's branch
        student_subjects = [s for s in subjects_data if s[2] == branch]
        for subject in student_subjects:
            subject_id = subject[0]
            semester = subject[3]
            marks = round(random.uniform(60, 95), 2)  # Random marks between 60 and 95
            marks_data.append((student_id, subject_id, semester, marks))

    cursor.executemany("""
        INSERT INTO Semester_Marks (Student_ID, Subject_ID, Semester, Marks)
        VALUES (?, ?, ?, ?)
    """, marks_data)
    print(f"Inserted {len(marks_data)} marks into Semester_Marks table")

    # Commit the transaction
    conn.commit()
    print("Data insertion completed successfully")

except pyodbc.Error as e:
    print(f"SQL Error: {e}")
except Exception as e:
    print(f"General Error: {e}")
finally:
    # Close cursor and connection if they were created
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Connection closed")
