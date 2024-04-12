# tuple is great, but it allows us to remember the position or name of tuple

# so namedtuple is good

# students = (('Scot',28, 'A' ), ('Nicole', 26, 'B'),('Jonh', 29, 'D')) --> normal tuple

# students = namedtuple('students', ['name', 'age', 'grade']) -> namedtuple
# scott = student('Scott', 28, 'A')
# nicole = student('Nicole ', 68, 'B')
# John = student('John', 29, 'D')

# Access Scott’s information for example
# print(scott.name) # Output: Scott
# print(scott.age) # Output: 28
# print(scott.grade) # Output: ‘A’

# we can package three student tuples neatly into a tuple called students like so
# students = (scott, nicole, john)

from collections import namedtuple

country = namedtuple("country", ["name", "capital", "continent"])

france = country("France", "Paris", "Europe")
japan = country("Japan", "Tokyo", "Asia")
senegal = country("Senegal", "Dakar", "Africa")

countries = (france, japan, senegal)
