from matplotlib.image import AxesImage
import matplotlib as mpl
import matplotlib.pyplot as plt

x1, x2, x3 = [5, 7, 9]

a,b,c = [6,7,2]

y1, y2, y3 = [a*x1+x1*b-c, a*x2+x2*b-c, a*x3+x3*b-c]

print(f"O resultado de y1 é {y1}, y2 = {y2}, e y3 = {y3}.\n")

plt.plot([x1, x2, x3], [y1, y2, y3], color='blue')

plt.scatter([x1, x2, x3], [y1, y2, y3], color='red')

plt.title('Gráfico da função y=ax+xb-c')

plt.xlabel('Valores de X')

plt.ylabel('Valores de Y em relaçao a X')

plt.grid()

plt.legend(['Valores de X', 'Y correspondente a X'])
plt.show()
