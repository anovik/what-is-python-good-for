import csv
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

class Continent:
    def __init__(self, index, name, population, area):
        self.index = index
        self.name = name
        self.population = population
        self.area = area    
  
with open("continents.csv", "r") as file:
    data = list(csv.reader(file, delimiter=';'))
    
continents = [Continent(row[0], row[1], locale.atof(row[2]), locale.atof(row[3])) for row in data[1:]]    

names = [c.name for c in continents]
areas = [c.area for c in continents]
populations = [c.population for c in continents]

#pie chart
fig, ax = plt.subplots()
ax.pie(areas, labels=names, autopct='%1.2f%%')
plt.title("Area by continent")
plt.show()

fig, ax = plt.subplots()
ax.pie(populations, labels=names, autopct='%1.2f%%')
plt.title("Population by continent")
plt.show()

#bar chart
fig, ax = plt.subplots()
ax.bar(height=areas, x=names)

ax.set_ylabel('Area')
ax.set_title('Continents by Area')

plt.show()

fig, ax = plt.subplots()
ax.bar(height=populations, x=names, log=True)

ax.set_ylabel('Population')
ax.set_title('Continents by Population(Log scale)')

plt.show()