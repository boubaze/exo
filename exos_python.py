#!/usr/bin/env python
# coding: utf-8

# In[2]:


##Question 1
##Declaration de ma liste vide qui va accueillir les nombres
B = []

for n in range(2000, 3200): ##utlisation du boucle for pour l'opperation et la fonction RANGE

   if n%7 == 0 and n%5 != 0:   ## la condition pour que n soit ajouté à la liste Le signe % désigne l'opérateur "modulo", c'est lui qui permet de donner le reste de n dans la division euclidienne par 7 et 5.

       B.append(n)

print(B)


# In[3]:


##Question 2
from math import factorial ##Importation de la biblioheque math pour les factoriel
n=int(input("Veuillez saisir un nombre possitif:")) ##Invite l'utilisateur à saisir un chiffre
if n<0:
    print("Merci de saisir un nombre possitif SVP!!!")##Message afficher en cas de saisie d'un nombre negatif
else:
    print("Le factoriel de",n, "est:",factorial(n)) ##Le resultat 


# In[4]:


##Question 3
MyDict=dict()
MyDict
n=int(input("Veuillez saisir un nombre entier:")) ##Invite l'utilisateur à saisir un chiffre
for n in range(1, n+1): ##utlisation du boucle for pour l'opperation et la fonction RANGE

   if n>0 and n!= 0:
    MyDict={n,n*n}
    print(MyDict)


# In[7]:


##Question 6
import numpy as np 
  
  
array1 = np.array([0, 1, 1]) 
array2 = np.array([2, 2, 1]) 
  
print(array1) 
  
print(array2) 
  
print("\nLa covariance des deux matrices sont:\n", 
      np.cov(array1, array2)) 


# In[9]:


##Question 5
import numpy as np

oned = np.array( [[0,1] ,[2, 3], [4, 5]] )

print(oned)##AFFICHE LE TABLEAU ORIGINAL
print(oned.tolist())##CONVERSION DU TABLEAU EN LIST


# In[10]:


##QUESTION 7
from math import sqrt
D=[int(x) for x in  input("Saisir les trois valeurs de D (des entiers) separes par une virgule:").split(',')] ##INVITE DE SAISIR LES TROIS CHIFFRES DE D AU CLAVIER
H=30
C=50
Q1=D[0]
Q2=D[1]
Q3=D[2]
print("La racine carré de Q1 vaut:", round(sqrt((2 * C * Q1)/H)))##AFFICHE LE RESULTAT DE Q1
print("La racine carré de Q2 vaut:", round(sqrt((2 * C * Q2)/H)))  ##AFFICHE LE RESULTAT DE Q2
print("La racine carré de Q3 vaut:", round(sqrt((2 * C * Q3)/H)) )  ##AFFICHE LE RESULTAT DE Q3


# In[30]:


##QUESTION 4
missing_char=['kitten']
print(missing_char)

