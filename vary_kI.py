import scipy.io
import cmath
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.offsetbox import AnchoredText
import matplotlib.ticker as mticker

kdeg = 10**(-5)
n = 3
kp = 1.5 * 10**(10)
P = 100 * 10**(-9)
a = 3.3
kr = 2 * 10^(11)

x_ticks = []
kl_val = []
kdeg_p = [10**(-2),10**(-4),10**(-6)]
x_know = []
x_array = []
itr1_array = []
for j in range(6,-2,-1):
    x_ticks.append(10**(-j))
for kdeg in kdeg_p:
    print(kdeg)
    x  = []
    itr1 = []
    for j in range(20,-5,-1):
        i = -j/4
        kl = 10**(i)
        kl_val.append(kl)
        # print(kl)
        # x_ticks.append(kl)
        a1 = kdeg*kr
        b = (1+kp*P)*kdeg
        c = -n*kp*P*kl*a
        d = (b**2) - (4*a1*c)
        #sol1 = (-b-cmath.sqrt(d))/(2*a)
        R = (-b+cmath.sqrt(d))/(2*a1)
        R = np.real(R)
        print(R)
        Sunreg = -kdeg
        Sauto = -(n*kp*P*kl*a*kr)/((1+kp*P+kr*R)**2) - kdeg
        Sr = Sauto/Sunreg
        print(Sr)
        x.append(Sr)
        itr1.append(i)
    x_array.append(x)
    itr1_array.append(itr1)

# print(kl_val)
# print(x)


fig = plt.figure()
ax = plt.subplot(111)
locs = ax.get_xticks()
labels = ax.get_xticklabels()
print(locs)
print(labels)
print(x_ticks)
print(len(labels))
ax.set_xticklabels(x_ticks)
ax.set_xlabel('$k_I (s^{-1})$')
ax.set_ylabel('$S_{r}$')
ax.plot(itr1_array[0], x_array[0], label="$k_{deg}=1e-2$",linestyle='dashed')
ax.plot(itr1_array[1], x_array[1], label="$k_{deg}=1e-4$",linestyle='dashed')
ax.plot(itr1_array[2], x_array[2], label="$k_{deg}=1e-6$",linestyle='dashed')
plt.title("Stability Ratio vs Isomerization Rate")

plt.legend()
plt.show()
print(itr1_array[0])
print(kl_val)
# for i in range(0,3):
iternum = 0
for j in range(0,25,4):
    iternum +=1
    print("\\textbf{" + str(iternum) + "}  & " + str(x_ticks[iternum]) + " & " + str(round(x_array[2][j],3))+ " & " +  str(round(x_array[1][j],3)) + " & " +  str(round(x_array[0][j],3)) + "\\\\ \hline")
iternum = 0

for j in range(0,25,4):
    iternum +=1
    print("\\textbf{" + str(iternum) + "}  & " + str(x_ticks[iternum])+ " & "+  str(round(x_array[1][j],3)) + "\\\\ \hline")
