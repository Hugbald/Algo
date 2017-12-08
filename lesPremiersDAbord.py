from data import *
from outils import *

def enConflit(r1, r2):
    return not compatible(r1,r2)

def compatible(r1,r2):
    if r2[0]>=r1[1] or r1[0]>=r2[1]:
        return True
    else:
        return False

def nettoyer(req,x):
    i = 0
    while i < len(req):
        if enConflit(req[i],x):
            req.pop(i)
            i -= 1
        i += 1


def selectionnerLesPremiersDAbord(reqs):
    solution=[]
    requetes=list(reqs)
    while requetes!=[]:
        x=requetes.pop(0)
        solution.append(x)
        nettoyer(requetes,x)
    return solution

def tester(cond):
    if cond:
        print("OK !")
    else :
        print("ECHEC !")

print("Les plus petites d'abord")
requetes_triees=sorted(I1,key=lambda requete: longueur(requete))
selection=selectionnerLesPremiersDAbord(requetes_triees)
tester(len(selection)==4)
requetes_triees=sorted(I2,key=lambda requete: longueur(requete))
selection=selectionnerLesPremiersDAbord(requetes_triees)
tester(len(selection)==3)
95869f70-fec8-45dc-ac3e-dd6375a8097d
