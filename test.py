import numpy as np 
import matplotlib.pyplot as plt

year = np.arange(2008,2020,1)
catSec = [50919, 52186, 52073, 51263, 51325, 49190, 45183, 45413, 47869, 43031, 42238, 39522]

print(year)
print(catSec)

plt.xticks = (np.arange(2008, 2019, 1))
plt.plot((2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019), catSec)
plt.show()