def main():

        name = 'Andre Odendaal'
        hobby = 'cycling'
        address = '622 Illinois Road'

        individual1 = Person(name, address)
        print(individual1.who_am_i())
        individual1.hobby = 'cycling'

        name = 'Gudrun Odendaal'
        hobby = 'Art'
        address = '622 Illinois Road'

        individual2 = Person(name, address)
        individual2.hobby = hobby
        print(individual2.hobby)

        dog_name = 'spike'
        dog_owner = 'Paul Preen'

        dog_1 = Dog(dog_name, dog_owner)
        print(dog_1.dog_details())
        print(dog_1.owner)
        dog_name = 'Pluto'

        dog_2 = Dog(dog_name, individual2)

        # Polymorphism through Composition
        print("The owner of the dog {}'s name is {} and does {}.".format(dog_2.dog_details(),dog_2.owner.name, dog_2.owner.hobby))
        print("The owner of the dog {}'s name is {}.".format(dog_1.dog_details(), dog_1.owner))


class Dog:

        def __init__(self, dog_name, owner):
                self.dog_name = dog_name
                self.owner = owner

        def dog_details(self):
                return self.dog_name


class Person:

        def __init__(self, name, address):
                self.name = name
                self.address = address
                self.hobby = ' '


        def who_am_i(self):
                return self.name

        def address_detail(self):
                return self.address

        def hobby(self, hobby):
                self.hobby = hobby
                return self.hobby


if __name__ == '__main__':
    main()




