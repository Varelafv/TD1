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
    F=[0]
    I=[]
    #Determination de la moyenne
    for i in range(k) :
        xi.append(int((x[0][i]+x[1][i])/2))
        fi.append(x[2][i]/Nt)
        Prod.append(xi[i]*fi[i])
        Moy = sum(Prod[0:])
    #Determination de la variance
    for i in range(k) :
        var.append(float(1/Nt)*(x[2][i]*(xi[i]**2) - Moy**2 ))
        V =  sum(var[0:])
    Fi=fi
    # Determination de la  Frequence cumulées
    for i in range(1,k) :
        Fi[i]=Fi[i-1]+fi[i]
    I=x[0][0:]
    I.append(x[1][k-1])
    for i in Fi :
        F.append(i)
    # Affichage de Graphique
    plt.xlabel('Tranches d_âge')
    plt.ylabel('Fréquences cumulées')
    plt.title('Grafique de fréquences cumulées.')
    plt.plot(I,F,'bo',I,F,'k')
    return (Moy,V)
#Tableau de teste exo 2
x=[[0,10,20,30,40,50,60,70],[10,20,30,40,50,60,70,80],[18,44,68,54,42,36,16,10]]
k=8
Moy,V=mMeanVar(x,k)
print("La Moyenne {:.2f}".format(Moy))
print("La Variance {:.2f}".format(V))
plt.grid(True)
plt.show()
