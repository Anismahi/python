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