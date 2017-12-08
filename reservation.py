def reservation(requetes):
    reservations=[]
    remplir(reservations, requetes)
    i = divisible(reservations,requetes)
    while i != -1:
        reservations.pop(i)
        remplir(reservations, requetes)
        i = divisible(reservations,requetes)
    return reservations

def divisible(reservations,requetes):
    for i in range(len(reservations)):
        for j in range(len(requetes)):
            diff=duree(reservation[i])-duree(requete[j])
            if enConflit(reservations[i],requetes[j]) and diff>0:
                return i
        
def duree(requete):
    return requete[1]-requete[0]

def remplir(reservations, requetes):
    for i in range (len(requetes)):
        if creneauDispo(reservations,requetes[i]):
            reservations.append(requetes[i])

def creneauDispo(reservation,requete):
    res = True
    for i in range(len (reservation)):
        if enConflit(reservation[i], requete):
            res = False
    return res

def enConflit(r1, r2):
    return not compatible(r1,r2)

def compatible(r1,r2):
    if r2[0]>=r1[1] or r1[0]>=r2[1]:
        return True
    else:
        return False

def tester(cond):
    if cond:
        print("OK !")
    else :
        print("ECHEC !")

def selectionValide(requetes):
   res=True
   for i in range(len(requetes)-1):
        for j in range(i+1,len(requetes)-1):
            if enConflit(requetes[i],requetes[j]):
                res=False
   return res

def selectionBrute(I,S):
    if not selectionValide(S):
        return []
    elif len(I)==0:
        return S
    else:
        J=list(I)
        premiere=J.pop()
        if selectionValide(S+[premiere]):
            aveclapremiere=selectionBrute(J,S+[premiere])
        else:
            aveclapremiere=[]
        sanslapremiere=selectionBrute(J,S)
        if len(aveclapremiere)>len(sanslapremiere):
            return aveclapremiere
        else:
            return sanslapremiere

tab=[[1,4],[5,9],[0,6],[12,14],[6,10],[5,7],[2,13],[8,12],[3,5],[8,11],[3,8]]


tester(selectionValide([[1,2]])==True)
tester(selectionValide([[1,2],[3,4]])==True)
tester(selectionValide([[3,4],[1,2]])==True)
tester(selectionValide([[3,4],[1,2],[1,3]])==False)
tester(enConflit([1,2],[1,3])==True)
#tester(reservation([[3,4],[1,2],[0,2]])==[[3,4],[1,2]])
#tester(reservation([[3,4],[1,2],[0,3]])==[[3,4],[1,2]])
#print(reservation(tab))

print(selectionBrute(tab,[]))
