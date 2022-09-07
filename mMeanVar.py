import matplotlib.pyplot as plt

def mMeanVar (x,k):
    xi=[]
    fi=[]
    Prod=[]
    Nt=sum(x[2][0:])
    Moy=0
    var=[]
    V=0;
    Fi=[]
    for i in range(k) :
        xi.append(int((x[0][i]+x[1][i])/2))
        fi.append(x[2][i]/Nt)
        #D.append((fi[i]/10)*100) Densinté
        Prod.append(xi[i]*fi[i])
        Moy = sum(Prod[0:])
    for i in range(k) :
        var.append(float(1/Nt)*(x[2][i]*(xi[i]**2) - Moy**2 ))
        V =  sum(var[0:])
    Fi=fi
    for i in range(1,k) :
        Fi[i]=Fi[i-1]+fi[i]
    plt.xlabel('Tranches d_âge')
    plt.ylabel('Fréquences cumulées')
    plt.title('Grafique de fréquences cumulées.')
    plt.plot(x[0][0:],Fi,'bo',x[0][0:],Fi,'k')
    return (Moy,V)
x=[[0,10,20,30,40,50,60,70],[10,20,30,40,50,60,70,80],[18,44,68,54,42,36,16,10]]
Moy,V=mMeanVar(x,8)
print("La Moyenne {}".format(Moy))
print("La Variance {}".format(V))
plt.show()
