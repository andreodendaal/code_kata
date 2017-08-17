class EmployeeRecord:
    def __init__(self):
        self.record = {}

    def add_record(self, name, rec):
        self.record[name] = rec

    def all_employees(self):
        return self.record


employee = EmployeeRecord()
employee.add_record('Andre Odendaal', [1, '2017-02-20', 'Manager'])
employee.add_record('Gudrun Odendaal', [2, '2017-02-20', 'Boss'])
print(employee.all_employees())

