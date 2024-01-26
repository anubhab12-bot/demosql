import pandas as pd

# Your JSON data
json_data = {
    "schoolName": "Example High School",
    "students": [
        {
            "studentNumber": "S001",
            "name": "John Doe",
            "grade": 10,
            "age": 16
        },
        {
            "studentNumber": "S002",
            "name": "Jane Smith",
            "grade": 11,
            "age": 17
        },
        {
            "studentNumber": "S003",
            "name": "Bob Johnson",
            "grade": 9,
            "age": 15
        },
        {
            "studentNumber": "S004",
            "name": "Emily Davis",
            "grade": 12,
            "age": 18
        }
        # Add more students as needed
    ]
}

# Convert the JSON to a pandas DataFrame
df = pd.json_normalize(json_data['students'])

# Save the DataFrame to a CSV file
df.to_csv('students.csv', index=False)

print("CSV file created successfully.")
