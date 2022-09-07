
def mQuantile(x,s):
     q=len(x) ; #le nombre de d'aparition de  valeur max
     for i in x :
         m=0;
         for j in x:
             if j <= i:
                 m = m + 1 #Le nombre d'aparition   d'un valeur
         if (m/q >= s):   #Compariason de m sur q
             a=x.index(i) #recuperer l'index
             break ;
     return (x[a])

X = [14,16,12, 9, 11, 18, 7, 8, 9, 16, 7, 9, 18]
X.sort()
q=[]
#DETERMINATION TOUS LES QUARTILLE
for i in range(1,5) :
    q.append(mQuantile(X,0.25*i))
print(q)

