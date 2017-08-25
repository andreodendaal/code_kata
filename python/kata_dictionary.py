
def main():

    record = {}
    name = 'Andre Odendaal'
    record['Name'] = 'Andre Odendaal'
    record['Location'] = 'Highland Park'
    record['Employee Number'] = 1

    emp_record = dict_access()
    emp_record.add_record(name, record)

    name = 'Paul Preen'
    record['Name'] = name
    record['Location'] = 'Langebaan'
    record['Employee Number'] = 2
    emp_record.add_record(name, record)
    print(emp_record.return_all())

class dict_access:
    def __init__(self):
        self.dict_record = {}

    def add_record(self, name, record):
        self.dict_record[name] = record

    def return_all(self):
        return self.dict_record

    def __iter__(self):
        return self.dict_record.__iter__()

if __name__ == '__main__':
    main()





