class Employee:
    def __init__(self, name, city, id):
        self.name = name
        self.city = city
        self.id = id
    def show(self):
        print(f"Emp name: {self.name}, Emp ID: {self.id}, Emp City: {self.city}")
Employee = [
    Employee("Sharvari", "Nagpur", 404),
    Employee("Esha", "Pune", 609),
    Employee("Suraj", "Bangalore", 765)
]

for emp in Employee:
    if emp.city == "Bangalore":
        emp.show()