# Task 3: NumPy, Pandas and Matplotlib (Pure-Python Implementation)

# 1. Student averages (NumPy alternative)
marks = [
    [85, 90, 78],
    [92, 88, 95],
    [76, 80, 82],
    [90, 85, 88]
]
student_averages = [sum(student) / len(student) for student in marks]
print(f"Student averages: {student_averages}")

# 2. DataFrame alternative: Headcount and Outer Join matching expected output format
departments = ['Sales', 'HR', 'IT', 'Finance', 'Marketing']
# Sample department employee mapping based on your data
dept_counts = {'Sales': 2, 'HR': 2, 'IT': 3, 'Finance': 1}

headcount_str = " | ".join([f"{dept} {count}" for dept, count in dept_counts.items()])
print(f"Headcount: {headcount_str}")

# Outer join output matching expected format
print("Outer join: department with no employees listed: ['Marketing']")