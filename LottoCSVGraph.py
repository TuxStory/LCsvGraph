import matplotlib.pyplot as plt
import numpy as np
import csv, statistics

def DataList():
    path ="./LottoGameData.csv"
    file = open(path,newline='')
    reader = csv.reader(file)
    header = next(reader) #first line is the reader
    data = []
    for row in reader:
        # row =  [date, n1, n2, n3, n4, n5, n6 ,n7]
        num = list(map(int,row[1:8])) #map applique la fontion int à tout le tableau qui était String
        data.append(num)
    return data

def Graphique(chiffre,counts):
    #y_pos = np.arange(len(counts))
    plt.subplot(211)
    bar = plt.bar(range(len(chiffre)), counts, align='center', alpha=0.5,color='g')
    plt.xticks(range(len(counts)),chiffre)
    plt.title("Lotto Stats by Number")
    plt.grid()    

def Graphique2(x,y):  
    plt.subplot(212)
    plt.title("Lotto Stats by Counts")
    bar = plt.bar(range(len(x)), y, align='center', alpha=0.5)
    plt.xticks(range(len(y)),x)
    plt.grid()

def Statistique(Tirage,Tab):
    print("Statistique".center(25,"*"))
    print("Nombre de Tirages :", Tirage)
    chiffre, counts = zip(*Tab)
    print("Nombre moyen de tirage d'un chiffre:", statistics.mean(counts))
    print("Rang 1 : 1/8.145.060")
    for i in range(len(Tab)):
       print("Chiffre:",Tab[i][0]," - Nombre de Tirage",Tab[i][1], Tab[i][1]/Tirage*100,"%")
    
    
    
def main():
    Stat = DataList()
    #print(Stat)
    chiffre, counts = np.unique(Stat, return_counts=True)
    c = list(zip(chiffre, counts))
    print(c)
    tri = sorted(c, key=lambda c: c[1])
    print("TRI".center(25,"*"))
    print(tri)
    x, y = zip(*tri)
    tirages = len(Stat)
    Statistique(tirages,c)
    Graphique(chiffre,counts)
    Graphique2(x,y)
    plt.show()
    
if __name__=="__main__":
    main()


