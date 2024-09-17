def est_isocele(a,b,c) :
   if (a==b or b==c or a==c):
    return(True)
   else:
    return(False)
print(est_isocele(3,5,8))



def lpp(a,b):
    if a<b:
       return a 
    else:
       return b
print (lpp(2,8))


def valeur_absolue(x):
    if x<0 :
      return x*(-1)
print (valeur_absolue(-5))  

#EXERCICE 10
def est_pair (n):
    if n%2:
        return False
    else:
        return True
print (est_pair(0))

#EXERCICE 12
def signe (x):
    if x>0:
        return "Positif"
    elif x==0:
        return "Nulle"
    elif x<0:
        return "Negative"
print (signe(5))

#EXERCICE 
def suite(n):
    u = 1
    for k in range(n):
        u = 2*u+k
    return u
print (suite(2))

#lundi 16 septembre
def find_roots(a,b,c):
    D=b**2 - 4*a*c
    if D>0:
        root1=(-b+D**0.5)/2*a 
        root2=(-b-D**0.5)/2*a
        return [root1,root2]
    elif D==0:
        root3=-b/2*a 
        return root3
    else:
        return None
        
print(find_roots(6,6,1))


#mardi test
S=0
for i in range (1,6):
    S=S+i 
print(S)


def seuil (eps):
    u=1
    n=0
    while(u>eps):
        u=u/(n+1)
        n=n+1
        return n 
print(seuil(0))
