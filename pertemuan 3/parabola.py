"""  	
210535614881 	BRILLIANTA ZAYYAN MUHAMMAD
210535614846 	DHEA FANNY PUTRI SYARIFA
210535614833 	ERLIANA FAJARWATI
210535614873 	FARKHANA FARDA ZAHRANI
210535614854 	JUAN MICHAEL AFANDI
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,1000)
constant = 3
y = -(x**2) + x + constant

fig, ax = plt.subplots()
ax.plot(x,y)
plt.axvline(x=0, color='r')
plt.axhline(y=0, color='r')
plt.show()