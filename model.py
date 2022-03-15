import random

def est_dans(element,liste):
    for i in liste:
        if element== i:
            return True
    return False

def verification(tab):
    var=0
    A=[0]*p*p
    for i in range (0,p*p):
        A[i] = i+1 # Crée une liste de longueur p² avec les valeurs acceptées
  
    for j in range (0,p*p):       
        if est_dans(tab[j],A):
            A.remove(tab[j])
            var+=1
        elif tab[j]==0:
            var+=1
        else: return False
    if var==p*p:
        return True
    else:
        return False

       
p=2

def verification_ligne(n,matrice):
    if verification(matrice[n]) == False:
        return False
    else : 
        return True
    

def verification_colonne(m,matrice) : 
    B=[0]*p*p
    for i in range (0,p*p):
        B[i]=matrice[i][m]
    if verification(B) == False:
        return False
    else:
        return True

def verification_bloc(m,n,matrice):
    # (m,n) indice de la case en haut à gauche de chaque bloc
    B=[0]*p*p
    cpt=0
    for i in range(0,p):
        for j in range(0,p):
            B[cpt]=matrice[m+i][n+j]
            cpt+=1

    return verification(B)

def verification_toutes_leslignesetcolonnes(matrice):
    for i in range (0,p*p):
        if verification_ligne(i,matrice)==False:
            return False
        if verification_colonne(i,matrice)==False:
            return False
    return True

def verification_tous_lesblocs(matrice):
    for i in range(0,p):
        for j in range(0,p):
            if verification_bloc(p*i,p*j,matrice)==False:
                return False
    return True

def verification_grille(matrice):
   return verification_tous_lesblocs(matrice) and verification_toutes_leslignesetcolonnes(matrice)

    

def grille_complete(matrice):
    for i in range(0,p*p):
        for j in range (0,p*p):
            if matrice[i][j]==0:
                return False
    return True

def premier_élément_nul(matrice):
    for i in range (0,p*p):
        for j in range(0,p*p):
            if matrice[i][j]==0:
                return ([i,j])
    return 0

def Resoudre_grille (matrice):
    if verification_grille(matrice)==False:
        return False , []
    if grille_complete(matrice)==True:
        return True , matrice
    for i in range(1,p*p+1):
        [x,y]=premier_élément_nul(matrice)
        matrice[x][y]=i
        if Resoudre_grille(matrice)[0]==True:
            return True , matrice
        else:
            matrice[x][y]=0
    return False , []

def Resoudre_grille_aleatoirement (matrice):
    if verification_grille(matrice)==False:
        return False , []
    if grille_complete(matrice)==True:
        return True , matrice
    valeurs=[j for j in range (1,p*p+1)]
    random.shuffle(valeurs)
    for i in valeurs:
        [x,y]=premier_élément_nul(matrice)
        matrice[x][y]=i
        if Resoudre_grille(matrice)[0]==True:
            return True , matrice
        matrice[x][y]=0
    return False , []


def comptage_solutions(matrice):
    if verification_grille(matrice)==False:
        return 0
    if grille_complete(matrice)==True:
        return 1
    cpt=0
    for i in range(1,p*p+1):
        [x,y]=premier_élément_nul(matrice)
        
        matrice[x][y]=i
        cpt += comptage_solutions(matrice)
        matrice[x][y]=0
    return cpt

def generation_grille_complète(p):
    #A=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    A=[(p*p)*[0] for i in range(p*p)]
    # for i in range(0,p*p):
    #     for j in range(0,p*p):
    #         A[i][j]=0
    return Resoudre_grille_aleatoirement(A)[1]
    
def generation_grille_incomplète(p):
    G=generation_grille_complète(p)
    L=[]
    for i in range (0,p*p):
        for j in range (0,p*p):
            L.append([i,j])
    random.shuffle(L)
    for i,j in L:
        valeur=G[i][j]
        G[i][j]=0
        if comptage_solutions(G)>1:
            G[i][j]=valeur
    return G


