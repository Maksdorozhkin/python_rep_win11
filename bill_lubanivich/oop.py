# Определение класса
class Cat():
    # методы инициализация метода
    def __init__(self, name) -> None:
        self.name = name


# a_cat = Cat()
# another_cat = Cat()

# Атрибуты класса
# a_cat.age = 3
# a_cat.name = "Толик"
# a_cat.namesis = another_cat

# print(a_cat.age)
# print(a_cat.name)

# a_cat.namesis.name = "Витя"
# print(a_cat.namesis.name)
furball = Cat('Grunpy')

print("Our lasted edition: ", furball.name)

# Наследование


# class Car():
#     def exclaim(self):
#         print("I am a car!")


# class Yugo(Car):
#     pass


# print(issubclass(Yugo, Car))
# give_me_a_car = Car()
# give_me_a_yugo = Yugo()
# give_me_a_car.exclaim()
# give_me_a_yugo.exclaim()

# Переопределение классов
class Car():
    def exclaim(self):
        print("I am a car!")

# Добавление метода


class Yugo(Car):
    def exclaim(self):
        print("I am Yugo!")

    def need_a_push(self):
        print("A little help here?")


print(issubclass(Yugo, Car))
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
give_me_a_yugo.need_a_push()


class Person():
    def __init__(self, name) -> None:
        self.name = name


class MDPerson():
    def __init__(self, name) -> None:
        self.name = "Doctor " + name


class JDPerson():
    def __init__(self, name) -> None:
        self.name = name + ", Esquire"


person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person.name)
print(doctor.name)
print(lawyer.name)

# получаем помощь от родительского класса с помощью метода super()


class EmailPerson(Person):
    def __init__(self, name, email) -> None:
        super().__init__(name)
        self.email = email


bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)
