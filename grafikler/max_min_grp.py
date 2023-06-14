import matplotlib.pyplot as plt

dizi = [0,1,2,3,4,3,2,1,2,3,4,5,6,7,8,9,6,5,4,3,2]
lokal_minler = []
lokal_makslar =[]

plt.plot(dizi,'-or')

for i in range(1,len(dizi)-1):
    if dizi[i]< dizi[i-1] and dizi[i] < dizi[i+1]:
        lokal_minler.append([i,dizi[i]])
        plt.text(lokal_minler[-1][0],lokal_minler[-1][1],'lokal min'
                 +str(len(lokal_minler)))
    if dizi[i] > dizi[i-1] and dizi[i]>dizi[i+1]:
        lokal_makslar.append([i,dizi[i]])
        plt.text(lokal_makslar[-1][0],lokal_makslar[-1][1], 'lokal maks'
                +str(len(lokal_makslar)))

plt.grid(True)
plt.show()
