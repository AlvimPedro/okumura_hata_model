import math
import matplotlib.pyplot as plt


def okamura(fc, hb, r):

    a = 69.55 + 26.16*math.log10(fc) - 13.82*math.log10(hb)

    b = 44.9 - 6.55*math.log10(hb)

    c = 5.4 + 2*(math.log10(fc/28))**2

    d = 40.94 + 4.78*(math.log10(fc))**2 - 18.33*math.log10(fc)


    L_urbana = a + b*math.log10(r)
    L_suburbana = a + b*math.log10(r) -c
    L_aberta = a + b*math.log10(r) -d

    return L_urbana, L_suburbana, L_aberta

fc = 150
hb = 50
r = 2

l_fc1, l_fc2, l_fc3 = [], [], []
eixo_fc = []

#Variar fc
for i in range(150, 1500, 10):

    l1, l2, l3 = okamura(i, hb, r)

    l_fc1.append(l1)
    l_fc2.append(l2)
    l_fc3.append(l3)
    eixo_fc.append(i)


plt.plot(eixo_fc, l_fc1, label = "L Urbana")
plt.plot(eixo_fc, l_fc2, label = "L Suburbana")
plt.plot(eixo_fc, l_fc3, label = "L Aberta")

plt.title('Variando o fc: hb = 50m, R = 2Km')
plt.xlabel('fc (MHz)')
plt.ylabel('L_T (dB)')

plt.legend()

plt.show()

#Variando hb
fc = 200
eixo_hb = []
l_hb1, l_hb2, l_hb3 = [], [], []

for i in range(30, 200, 5):

    l1, l2, l3 = okamura(fc, i, r)

    l_hb1.append(l1)
    l_hb2.append(l2)
    l_hb3.append(l3)
    eixo_hb.append(i)


plt.plot(eixo_hb, l_hb1, label = "L Urbana")
plt.plot(eixo_hb, l_hb2, label = "L Suburbana")
plt.plot(eixo_hb, l_hb3, label = "L Aberta")

plt.title('Variando o hb: fc = 200MHz, R = 2Km')
plt.xlabel('hb (m)')
plt.ylabel('L_T (dB)')

plt.legend()

plt.show()


#Variando raio
hb = 50
eixo_r = []
l_r1, l_r2, l_r3 = [], [], []

for i in range(1, 15, 1):

    l1, l2, l3 = okamura(fc, hb, i)

    l_r1.append(l1)
    l_r2.append(l2)
    l_r3.append(l3)
    eixo_r.append(i)


plt.plot(eixo_r, l_r1, label = "L Urbana")
plt.plot(eixo_r, l_r2, label = "L Suburbana")
plt.plot(eixo_r, l_r3, label = "L Aberta")

plt.title('Variando o R: fc = 200MHz, hb = 50m')
plt.xlabel('R (Km)')
plt.ylabel('L_T (dB)')

plt.legend()

plt.show()






