import dataclasses
import sys
from dataclasses import dataclass, field

# L = [x ** 2 for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

# print(isinstance(L, list))
from typing import ClassVar, List


@dataclass
class Worker:
    def __init__(self, name, pay):  # Initialize when created
        self.name = name.strip()  # self is the new object
        self.pay = pay

    def __repr__(self):
        b = len(self.name.split(' ')) > 1 and self.name.split(' ')[-1] != ''
        c = "%s with %.2f salary" % (self.name.split()[-1].strip() if b else '', self.pay)

        return "Worker %s" % (self.name.split()[0] + " " if b else self.name) + c + "__rept__"

    def __str__(self):
        b = len(self.name.split(' ')) > 1 and self.name.split(' ')[-1] != ''
        c = "%s with %.2f salary" % (self.name.split()[-1].strip() if b else '', self.pay)

        return "Worker %s" % (self.name.split()[0] + " " if b else self.name) + c + "__str__"

    def lastname(self):
        return self.name.split()[-1]  # Split string on blanks

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)


w = Worker('Abilio', 115)

print(w.__str__())
w.give_raise(.25)
print(w.__repr__())

print(w)


@dataclass(eq=True, frozen=False, unsafe_hash=True)
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str = ''
    unit_price: float = 0.00
    quantity_on_hand: int = field(repr=False, default=0)
    id: int = 0

    def total_cost(self) -> "Total Cost of item inventory":
        return self.unit_price * self.quantity_on_hand

    '''def __str__(self):
        return str(self.total_cost.__annotations__)'''

    '''def __hash__(self):
        return hash(self.name)'''


a = InventoryItem('Gloves', 1.52, 10.5, 115002)
b = InventoryItem('Soldier Gloves', 4.52, 3, 115001)
c = InventoryItem('Soldier Gloves', 4.52, 3, 115001)

print('\n\n\n')
print(a.__repr__(), 'a')
print(dataclasses.Field.name)
print(dataclasses.fields(a))
print(dataclasses.asdict(a))
print(dataclasses.astuple(a))
print('\n\n\n')

a.name = 'Tits'

print(a.total_cost.__annotations__)
print(a.total_cost())
print(a.__hash__(), b.__hash__(), c.__hash__(), 'hashes')
print(b.__eq__(c), 'equal')
print(a.__gt__(b), 'greater than')

print(a.__hash__(), b.__hash__())
print(a.__eq__)

OBJs = [a, b, c]

print('\n\n\n')
print([x.name for x in OBJs])

# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#    Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# print(__name__)

# print({x ** 2 for x in [1, 2, 3, 4]})

# from fractions import Fraction

# print(Fraction(Fraction(2, 3)+1))

# print(1 != 2)

"""
from dataclasses import dataclass
from decimal import Decimal

L = [x ** 2 for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

print(isinstance(L, list))


@dataclass
class Worker:
    def __init__(self, name, pay):  # Initialize when created
        self.name = name.strip()  # self is the new object
        self.pay = pay

    def __repr__(self):
        b = len(self.name.split(' ')) > 1 and self.name.split(' ')[-1] != ''
        c = "%s with %.2f salary" % (self.name.split()[-1].strip() if b else '', self.pay)

        return "Worker %s" % (self.name.split()[0] + " " if b else self.name) + c

    def lastname(self):
        return self.name.split()[-1]  # Split string on blanks

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)


w = Worker('Abilio', 115)

print(w.__str__())
w.give_raise(.25)
print(w.__repr__())

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

# from math import trunc

print(len(str(999999999999999999999999999999)))
print(len(str(999999999999999999999999999999 + 1)))

print((2 ** 200) / 100)

# print(5 // 2, trunc(5 // -2))
"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''
x = set('abcde')
y = set('bdxyzabcde')

print('e' in y)

print(x > y)

print(type(x))
print(type(x))
'''
'''
L = [1, 2, 3, 4, 5, 5, 4, 3]
print(L)
print(list(set(L)))
print(set(L))

engineers = {'ahmed', 'bob', 'sue', 'ann', 'vic', 'tom'}
managers = {'tom', 'sue', 'ahmed', 'bob', 'mirtha'}

print('engineers', engineers)
print('managers', managers)

# is ahmed a manager
question = "is ahmed a manager?"
print(question, 'ahmed' in managers)

# who are both
question = "who are both?"
response_aux = str(engineers & managers)[1:-1].replace('\'', '')
pos = str(response_aux).rfind(',')
response = response_aux[:pos] + " and" + response_aux[pos + 1:]
print(question, response)

# who are in the team
question = "who are in the team?"
response_aux = str(engineers | managers)[1:-1].replace('\'', '')
pos = str(response_aux).rfind(',')
response = response_aux[:pos] + " and" + response_aux[pos + 1:]
print(question, response)

# who are engineers and not managers
question = "who are engineers and not managers?"
response_aux = str(engineers - managers)[1:-1].replace('\'', '')
pos = str(response_aux).rfind(',')
response = response_aux[:pos] + " and" + response_aux[pos + 1:]
print(question, response)

# who are managers and not engineers
question = "who are managers and not engineers?"
response_aux = str(managers - engineers)[1:-1].replace('\'', '')
pos = str(response_aux).rfind(',')
aux_res = response_aux[:pos] + " and" + response_aux[pos + 1:]
response = str(managers - engineers)[2:-2] if len(managers - engineers) < 2 else aux_res
response = 'None' if len(managers - engineers) == 0 else str(managers - engineers)[2:-2]
print(question, response)

# are all managers engineers
question = "are all managers engineers?"
print(question, managers < engineers)

# are all engineers managers
question = "are all engineers managers?"
print(question, managers > engineers)

# who is one but not both
question = "who is one but not both?"
response_aux = str(managers ^ engineers)[1:-1].replace('\'', '')
pos = str(response_aux).rfind(',')
aux_res = response_aux[:pos] + " and" + response_aux[pos + 1:]
response = str(managers ^ engineers)[2:-2] if len(managers ^ engineers) < 2 else aux_res
print(question, response)

# print(True + 1 + False * 2)

L1 = [1, 2, 3]
L2 = L1[::-4]
L1[1] = 4
print(L2)

print(L1 is L2, L2 is L1)

print("The " "meaning" ' of life' + ''' "same"''' """ for all""")

print("asd\rb\ta")

mantra = """Always look
on the bright side
of life
"""

print(mantra)

myjob = 'developer'

# for x in myjob:
#    print(x.upper())
#    print(x)
#    myjob = ''

name = 'Klol'
newname = name.replace("K", "X")
print(name, "=>", newname)

S = "Havana"
L = list(S)
pos = 0
for x in L:
    if x == 'a':
        L[pos] = 'i'
    pos += 1

S = ''.join(L)
print(S)

print('Havana'.join(['vieja', 'nueva', 'rota']))

line = 'The knights who say Ni!\n'
print(line)

sub = ' Ni!\n'
print(line.endswith(sub))
print(-len(sub), line[-len(sub):] == sub)

"""
f = open("C:\\Users\\ahmed\\Desktop\\vars.txt", "w")
f.write(str(vars()))
"""

L = ['spam', 'Spam', 'SPAM!']
L[1] = 'eggs' # Index assignment
print(L)
L[0:2] = ['eat', 'more']
# Slice assignment: delete+insert
print(L)
# Replaces items 0,1

D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(D.keys(), D.values(), D.items())

table = {'Python': 'Guido van Rossum', 'Perl': 'Larry Wall', 'Tcl': 'John Ousterhout'}
for t in table:
    print("Language\t", t, "was created by\n\t\t\t", table[t])
'''

C = dataclasses.make_dataclass(
    'C',
    [('x', int),
     'y',
     ('z', int, field(default=5))],
    namespace={'add_one': lambda self: self.x + 1,
               'add_two': lambda self: self.x + 2})

O = C(10, 0)
print(O.add_one())
print(O.add_two())
O.x = O.add_two()
print(O.x)

"""
>>> from dataclasses import dataclass, replace
>>> @dataclass
... class V:
...     x: int
...     y: int
...     
>>> v = V(1, 2)
>>> v_ = replace(v, y=42)
>>> v
V(x=1, y=2)
>>> v_
V(x=1, y=42)
"""


@dataclass()
class Point:
    x: float = dataclasses.Field(repr=True, default=0.00, default_factory=float, init=True, hash=True, compare=True,
                                 metadata={'x_axis': "X Axis", 'ext_name': "Point X Axis"})
    y: float = dataclasses.Field(repr=True, default=0.00, default_factory=float, init=True, hash=True, compare=True,
                                 metadata={'y_axis': "Y Axis", 'ext_name': "Point Y Axis"})


Point1 = Point(13.5, 455.25)
Point2 = dataclasses.replace(Point1, y=255.25)

print(Point1, Point2)

print(dataclasses.is_dataclass(Point1))


class DatabaseVar(object):
    pass


@dataclass(init=True, frozen=False)
class Pointer:
    x: float
    y: float
    z: float = dataclasses.Field(repr=True, default=0.00, default_factory=float, init=False, hash=True, compare=True,
                                 metadata={'z_axis': "Z Axis", 'ext_name': "Point Z Axis"})
    classy: ClassVar = None

    def __post_init__(self):
        self.z = (self.x + self.y) / 2


Point1 = Pointer(13.5, 455.25)
print(Point1)
f = list(dataclasses.fields(Pointer))
for x in f:
    print(x)


class DatabaseType(object):
    def lookup(self, param):
        pass


@dataclass
class C:
    i: int
    j: int = None
    database: dataclasses.InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = None


def my_database(args):
    pass


c = C(10, database=my_database)

"""
print('---------------')
x = 5
y = x

print(y)

x = 6
print(y)
print(id(x), id(y), 'Same' if id(x) == id(y) else 'Not the same')
print('---------------')
print('---------------')
x = [x for x in range(6)]
y = x

print(y)

x[0] = -1
print(y)
print(id(x), id(y), 'Same' if id(x) == id(y) else 'Not the same')
print('---------------')
print('---------------')
x = [x for x in range(6)]
y = x

print(y)

x = [x for x in range(5, 11)]
print(y)
print(id(x), id(y), 'Same' if id(x) == id(y) else 'Not the same')
print('---------------')
"""


class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self) -> str:
        print("Soy un Animal del tipo", type(self).__name__,
              "de la espacie", self.especie, "mi edad es", self.edad)


class Accion:
    def accion(self):
        pass


class Perro(Animal, Accion):
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)
        self.dueño = dueño

    def hablar(self):
        print('Guauu!')

    def accion(self):
        print('Muerde')

    def getDueño(self):
        print(self.dueño)


A = Animal('Aracnido', 2)
A.describeme()

P = Perro('Mamifero', 4, 'MiMismo')
P.describeme()
P.hablar()
P.accion()
P.getDueño()


def avg(marks):
    assert len(marks) != 0, 'Error occurred'
    return sum(marks) / len(marks)


mark1 = [0, 1]
print("Average of mark1:", avg(mark1))


# Definimos nuestra función
def pares(min=0, max=2 ** 31 - 1):
    index = min
    count = 1
    while index >= min and index <= max:
        if index % 2 == 0:
            yield index, count
        index = index + 1
        count += 1 if index % 2 == 0 else 0


for i in pares(150, 200):
    print(i)

print(list(pares(180, 200))[-1:])


class C:
    x

    def add(self, element):
        self.x = element


o1 = C()
o2 = C()
o1.add(1)
o2.add(2)
print(o1.x, o2.x)
print(o1.x == [1, 2])
print(o1.x is o2.x)


class C:
    x = []

    def add(self, element):
        self.x.append(element)


o1 = C()
o2 = C()
o1.add(1)
o2.add(2)
print(o1.x == [1, 2])
print(o1.x is o2.x)

@dataclass
class D:
    x: list = field(default_factory=list)

d1 = D()
d2 = D()
print(d1.x is d2.x)
