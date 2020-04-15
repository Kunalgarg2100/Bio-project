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
kl = 0.3 * 10**(-9)
a = 3.3

x_ticks = []
kr_val = []
kdeg = 10**(-5)
x_know = []
for j in range(6,13):
    x_ticks.append("$10^{"+str(j)+"}$")

x  = []
itr1 = []
for j in range(28,49):
    i = j/4
    kr = 10**(i)
    kr_val.append(kr)
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

fig = plt.figure()
ax = plt.subplot(111)
locs = ax.get_xticks()
labels = ax.get_xticklabels()
print(locs)
print(labels)
print(x_ticks)
print(len(labels))
ax.set_xticklabels(x_ticks)
ax.set_xlabel('$k_r (s^{-1})$')
ax.set_ylabel('$S_{r}$')
ax.plot(itr1, x,linestyle='dashed')
plt.title("Stability Ratio vs Binding Constant of the Repressor")

iternum = 0
tp = 6
print(x)
for j in range(0,25,4):
    iternum +=1
    tp += 1
    print("\\textbf{" + str(iternum) + "}  & " + "$10^{"+str(tp)+"}$" + " & "+  str(round(x[j],3)) + "\\\\ \hline")