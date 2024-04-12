class Mobil:
    def __init__(self, warna, merk, kecepatan):
        self.warna = warna
        self.merk = merk
        self.kecepatan = kecepatan

    def speedster(self):
        self.kecepatan += 10


class sport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def speedster(self):
        super().speedster()
        print("Tambahan kecepatan: ", self.kecepatan)


pigeot = Mobil("merah", "peugeot", 220)
lamborghini = sport("kuning", "lamborghini", 300)

print(pigeot.kecepatan)
pigeot.speedster()
print(pigeot.kecepatan)
print(lamborghini.kecepatan)
lamborghini.turbo()
print(lamborghini.kecepatan)
lamborghini.speedster()


def decorator(func):
    def wrapper():
        print("Before: ")
        func()
        print("After: ")

    return wrapper


@decorator
def greets():
    print("Hello cuk!")


greets()


class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species


class Cat(Animal):
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"

    def suara(self):
        return "meow!"


myCat = Cat("Neko", 3, "Persian")

print(myCat.deskripsi())
print(myCat.suara())
