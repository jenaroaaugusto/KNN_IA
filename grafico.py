
import numpy as np
import matplotlib.pyplot as plt


data1 = [0,72.580,70.370,67.272,70.491,100.0]
data2 = [ 0,3,5,7,9,11]
x = [0,3,5,7,9,11]

plt.plot( x, data1, 'go') # green bolinha
plt.plot( x, data1, 'k--', color='red') # linha pontilha orange

plt.plot( x, data2, 'r^') # red triangulo
plt.plot( x, data2, 'k--', color='blue')  # linha tracejada azul

#plt.axis([3,5, 7, 9])
plt.title("Wine KNN")

plt.grid(True)
plt.xlabel("Valore de K")
plt.ylabel("Precisão %")
plt.show()