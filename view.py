import math

# Retourne la ligne d'une grille
#def grille_liste(matrice,ligne): ## JL: attention, la fonction a le meme nom qu'une variable utilisée ensuite
#    return matrice[ligne]

# Retourne une grille contenant la matrice dont les colones et lignes sont
# séparées par des caractères et listes vides (3 d'espace)
#def affichage(matrice):
#   grille=[]
#   n = len(matrice)
#   b = int(math.sqrt(n))
#   for ligne in range(n+b-1): # Parcourt le nombre de lignes
#     grille.append([])
   #     for col in range(n+b-1): # Parcourt du nombre de colones
    #        grille[ligne].append(str(matrice[ligne][col]))
      #      if(col == 1):
         #       grille[ligne].append("|")
       # if(ligne == 1):
        #        grille.append([])
  #  return grille


def ligne_separation(n): # Ajoute les séparations horizontales
    # n = longueur des lignes
    liste = n * ["−"]
    return liste

def affichage_ligne(ligne,p): # Ajoute les lignes remplies
    liste = []
    cpt = 0
    while cpt < p**2: #p² = longueur de la ligne
        if cpt % p == 0:
            # Ajoute un | pour chaque indice multiple de p
            liste.append("|")
        liste.append(str(ligne[cpt]))
        cpt+=1
    liste.append("|") # Ajoute le dernier | de chaque ligne
    return liste

def affichage_grille(matrice): # Construit la matrice
    grille = []
    n = len(matrice) 
    p = int(math.sqrt(n))
    cpt = 0
    while cpt < n: # Parcourt le nombre de lignes
        if cpt % p==0:
            # Ajoute les - pour chaque indice multiple de p
            grille.append(ligne_separation(n+p+1))
        grille.append(affichage_ligne(matrice[cpt],p))
        cpt +=1
    grille.append(ligne_separation(n+p+1)) # Ajoute la dernière ligne de -
    return grille

def affichage_sudoku(matrice): # Affiche graphiquement la grille du sudoku
    grille = affichage_grille(matrice)
    sudoku = ""
    n = len(grille)
    for ligne in range(n):
        sudoku+="".center(40)
        for col in range(n):
            valeur = "".center(3)
            if (grille[ligne][col] != "0"):
                valeur+=str(grille[ligne][col])
            else:
                valeur+=" "
            sudoku+=valeur
        sudoku+="\n\n" # Saut de ligne    
    print(sudoku)