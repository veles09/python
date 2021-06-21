# -*- coding: utf8 -*-
class person:
def __init__(self, name, pol, age):
self.name = name #имя жильца
self.pol = pol # пол
self.age = age # возраст

def __str__(self):
return "name: {0} pol: {1} age: {2}".format(self.name, self.pol, self.age)

class Apartment:
def __init__(self, number, condition, storey, chambers):
self.number = number #номер квартиры
self.storey = storey #состояние кваритры
self.condition = condition #номер этажа
self.chambers = chambers #количество комнат
self.people = [] # жильцы этой квартиры

def add(self, human):

self.people.append(human) #Добавления жильца в квартиру


def __str__(self):
res = "number: {}, codition: {}\n".format(self.number, self.condition)
for h in self.people:
res += str(h) + "\n"
return res
# добавить квартиры, реализовать метод add, __str__
class House:
def __init__(self, number=1, address="Romantikov"): #дом в котором живут люди
self.address = address #адресс
self.number = number #номер
self.apart = [] #квартира

def add(self,apartment):
self.apart.append(apartment)

def __str__(self):
res = "house number: {}, address: {}\nappartments: {}\n".format(self.number, self.address, len(self.apart))
for h in self.apart:
res += str(h) + "\n"
return res


ctac = person("Ctac", "M", 30) #пол человека M-мужской, J-женский

def main(person, Apartment, House):
nikita = person("Nikita", "M", 28)
str_nikita = str(nikita)
natasha = person("Natasha", "J", 24)
apartment02 = Apartment(2,"good", 1, 3)
mihail = person("Mixail", "M", 55)
vova = person("Vova", "M", 25)
lena = person("Lena", "J", 20)
apartment02.add(mihail)
apartment02.add(vova)
apartment02.add(lena)

apartment01 = Apartment(1, "good", 1, 5)
apartment01.add(ctac)
apartment01.add(nikita)
apartment01.add(natasha)


house = House()
house.add(apartment01)
house.add(apartment02)
print(house)

if __name__ == "__main__":
main(person, Apartment, House)