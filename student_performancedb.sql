-- College Table
CREATE TABLE College (
    college_id INT PRIMARY KEY,
    college_name VARCHAR(100)
);

-- Branch Table
CREATE TABLE Branch (
    branch_id INT PRIMARY KEY,
    college_id INT FOREIGN KEY REFERENCES College(college_id),
    branch_name VARCHAR(100)
);

-- Semester Table
CREATE TABLE Semester (
    semester_id INT PRIMARY KEY,
    semester_name VARCHAR(20)
);

-- Student Table
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    college_id INT FOREIGN KEY REFERENCES College(college_id),
    branch_id INT FOREIGN KEY REFERENCES Branch(branch_id)
);

-- Marks Table
CREATE TABLE Marks (
    mark_id INT PRIMARY KEY IDENTITY,
    student_id INT FOREIGN KEY REFERENCES Student(student_id),
    semester_id INT FOREIGN KEY REFERENCES Semester(semester_id),
    subject VARCHAR(100),
    marks INT,
    total INT,
    
);
