import numpy as np
import matplotlib.pyplot as plt

Size = [768,1024]
MFT = np.zeros(Size)


Xpixels = np.arange(Size[1])
Ypixels = np.arange(Size[0])

Frecuency_B = np.log((Size[1]/2))/Size[1]
Frecuency_A = 1/(Frecuency_B*Size[1])
Frecuency = Frecuency_A*np.exp(Frecuency_B*Xpixels)
VaryngSin = 0.5*np.sin(2*np.pi*Frecuency)

Atenuacion_C = 16/Size[0]
Atenuacion =  np.exp(-1*Ypixels*Atenuacion_C) 
Atenuacion = Atenuacion

MFT = np.matmul(Atenuacion[::-1].reshape([Size[0],1]), VaryngSin.reshape([1,Size[1]]))+0.5
MFT = MFT.clip(min=0.0,max=1.0)
##MFT = np.round(MFT * 200.0)

fig = plt.figure("Señales")
ax = fig.add_subplot(1, 2, 1)
plt.plot(Xpixels, VaryngSin)
 
ax = fig.add_subplot(1, 2, 2)
plt.plot(Ypixels, Atenuacion)

plt.imsave('test.jpg', MFT, cmap = plt.cm.gray)

fig = plt.figure("Imagen")
plt.imshow(MFT)
plt.axis("off")

plt.show()
