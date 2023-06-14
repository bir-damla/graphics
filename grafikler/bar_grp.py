import matplotlib.pyplot as plt
import numpy as np

sehir = ['istanbul','antalya','samsun','izmir']
gunduz = [20,25,22,28]
gece = [14,15,16,14]
x = np.arange(len(sehir))
genislik = 0.25
#yan yana yazdırma
#plt.bar(x - genislik/2, gunduz,genislik,label='Gündüz')
#plt.bar(x + genislik/2,gece,genislik,label = 'Gece')
#üst üste yazdırma
plt.bar(sehir, gunduz,genislik,label='Gündüz')
plt.bar(sehir,gece,genislik,label = 'Gece',bottom=gunduz)

plt.xticks(x,sehir)
plt.xlabel('şehirler')
plt.ylabel('sıcaklık')
plt.title('hava durumu')
plt.legend()
plt.grid(True)
plt.show()