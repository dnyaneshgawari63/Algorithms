
company = [
    {"id": 1, "city": "delhi", "salary": 45000},
    {"id": 2, "city": "mumbai", "salary": 34000},
    {"id": 3, "city": "delhi", "salary": 65000},
    {"id": 4, "city": "chennai", "salary": 75000},
    {"id": 5, "city": "mumbai", "salary": 85000},
    {"id": 6, "city": "chennai", "salary": 95000},
    {"id": 7, "city": "delhi", "salary": 67000},
    {"id": 8, "city": "mumbai", "salary": 115000},
    {"id": 9, "city": "chennai", "salary": 125000},
    {"id": 10, "city": "delhi", "salary": 20000},
    {"id": 11, "city": "mumbai", "salary": 145000},
    {"id": 12, "city": "chennai", "salary": 155000},
    {"id": 13, "city": "delhi", "salary": 165000},
    {"id": 14, "city": "mumbai", "salary": 175000},
    {"id": 15, "city": "chennai", "salary": 34000},
    {"id": 16, "city": "delhi", "salary": 45000},
    {"id": 17, "city": "mumbai", "salary": 205000},
    {"id": 18, "city": "chennai", "salary": 215000},
    {"id": 19, "city": "delhi", "salary": 225000},
    {"id": 20, "city": "mumbai", "salary": 235000},
    {"id": 21, "city": "chennai", "salary": 34000},
    {"id": 22, "city": "delhi", "salary": 255000},
    {"id": 23, "city": "mumbai", "salary": 265000},
    {"id": 24, "city": "chennai", "salary": 50000},
    {"id": 25, "city": "delhi", "salary": 285000},
]

# 1. Group employees by city
city_groups = {}
for employee in company:
    city = employee["city"]
    if city not in city_groups:
        city_groups[city] = []
    city_groups[city].append(employee)

# 2. Find the top two highest-paid employees in each city
top_two_employees = {}
for city, employees in city_groups.items():
    # Sort employees by salary (descending)
    employees.sort(key=lambda x: x["salary"], reverse=True)
    # Select the top two employees
    top_two_employees[city] = employees[:2]

# 3. Print the results 
print("Top Two Highest-Paid Employees in Each City:")
for city, employees in top_two_employees.items():
    print(f"City: {city}")
    for employee in employees:
        print(f"  ID: {employee['id']}, Salary: {employee['salary']}")
