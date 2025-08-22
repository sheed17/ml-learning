import matplotlib as plt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

#Scatter Plots
"""

x_data = np.random.random(100) * 100
y_data = np.random.random(100) * 75

plt.scatter(x_data, y_data, marker="*", c='r')
plt.title("Scatter Plot")
plt.show()"""


#Line Plots
"""

years = [2005 + x for x in range(10)]
height = [20, 25, 42, 76, 91, 104, 108, 115, 119, 126]

plt.xlabel("Years")
plt.ylabel("cm")

plt.plot(years, height, c='r', lw=2, linestyle='--')
plt.title("Height Growth")
plt.show()
"""


#Bar Plot
"""
x = ["Soccer", "Basketball", "Football"]
y = [25, 21, 23]

plt.bar(x, y, color='r', align='center', lw=2, width=0.5)
plt.title("Sports Selections")
plt.show()
"""


#histographs
"""
scores = np.random.normal(20, 2.1, 1000)
plt.hist(scores, bins=3)
plt.show()

"""

#Pie Charts
"""
sports = ["Lacrosse", "Badmitton", "Tennis"]
votes = [21, 13, 7]
explodes = [0.0, 0.0, 0.3]

plt.pie(votes, labels=sports, explode=explodes, autopct="%.2f%%")
plt.title("Sports Votes")
plt.show()
"""

#Box Plot
"""
heights = np.random.normal(20, 2.1, 500)
plt.boxplot(heights)
plt.show()
"""
#Plot Customization
"""
years = [2006 + x for x in range(10)]
salary = [55, 66, 69, 71, 71, 78, 84, 87, 99, 101]

salary_ticks = list(range(50, 105, 5))
plt.plot(years, salary)
plt.xlabel("Year")
plt.ylabel("Income (USD)")
plt.yticks(salary_ticks, [f"${x}k" for x in salary_ticks])
plt.title("Bob's Salary Progression")
plt.show()
"""

#Legend for having multiple plots on one
"""
stock_a = [87, 89, 94, 97, 104, 106]
stock_b = [93, 94, 99, 104, 108, 121]
stock_c = [103, 99, 96, 94, 91, 107]
plt.plot(stock_a, label="Company 1")
plt.plot(stock_b, label="Company 2")
plt.plot(stock_c, label="Company 3")
plt.legend(loc="upper center")
plt.show()
"""


#Having Multiple Plots on one Window
"""
x = np.arange(5, 250, 5)
figs, axs = plt.subplots(2,2)

axs[0,0].plot(x, np.sin(x))
axs[0,0].set_title("Sin Plot")

axs[0,1].plot(x, np.cos(x))
axs[0,1].set_title("Cos Plot")

axs[1,0].plot(x, np.random.randint(21, 55, size=49))
axs[1,0].set_title("Random Plot Bro")

axs[1,1].plot(x, np.linspace(20, 1000, 49))
axs[1,1].set_title("Random pt2 Plot Bro")

plt.show()
"""

#3D Plots

axs = plt.axes(projection='3d')

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

axs.plot(x, y, z)
axs.set_title("3D Plot")
axs.set_xlabel("X axis")
plt.show()