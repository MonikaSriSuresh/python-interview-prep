"""
Composition vs Aggregation vs Inheritance
"""

# ==================================================
# 1. INHERITANCE (IS-A Relationship)
# ==================================================

print("===== INHERITANCE =====")


class Employee:

    def work(self):
        print("Employee Working")


class Developer(Employee):
    pass


dev = Developer()

dev.work()

print()

# ==================================================
# 2. COMPOSITION (Strong HAS-A Relationship)
# ==================================================

print("===== COMPOSITION =====")


class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car Started")


car = Car()

car.start_car()

print()

# ==================================================
# 3. AGGREGATION (Weak HAS-A Relationship)
# ==================================================

print("===== AGGREGATION =====")


class Address:

    def __init__(self, city):
        self.city = city


class Employee:

    def __init__(self, address):
        self.address = address

    def display(self):
        print("City:", self.address.city)


addr = Address("Chennai")

emp = Employee(addr)

emp.display()

print()

# ==================================================
# 4. COMPOSITION EXAMPLE
# ==================================================

print("===== COMPOSITION EXAMPLE =====")


class Battery:

    def charge(self):
        print("Battery Charging")


class Mobile:

    def __init__(self):
        self.battery = Battery()

    def charge_mobile(self):
        self.battery.charge()


mobile = Mobile()

mobile.charge_mobile()

print()

# ==================================================
# 5. AGGREGATION EXAMPLE
# ==================================================

print("===== AGGREGATION EXAMPLE =====")


class Department:

    def __init__(self, employee):
        self.employee = employee

    def show(self):
        print("Employee:", self.employee)


employee = "Monika"

dept = Department(employee)

dept.show()

print()

# ==================================================
# 6. INTERVIEW EXAMPLE
# ==================================================

print("===== INTERVIEW EXAMPLE =====")


class CPU:

    def process(self):
        print("Processing...")


class Computer:

    def __init__(self):
        self.cpu = CPU()

    def start(self):
        self.cpu.process()
        print("Computer Started")


computer = Computer()

computer.start()

print()

# ==================================================
# 7. AGGREGATION INTERVIEW EXAMPLE
# ==================================================

print("===== AGGREGATION INTERVIEW EXAMPLE =====")


class Teacher:

    def __init__(self, name):
        self.name = name


class School:

    def __init__(self, teacher):
        self.teacher = teacher

    def display(self):
        print("Teacher:", self.teacher.name)


teacher = Teacher("John")

school = School(teacher)

school.display()