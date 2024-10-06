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


#exercice 16
def p_ieme(n,p):
    S=0
    for k in range(1,n+1):
        S=S+k**p
    return S 
print(p_ieme(8,2))


#exercie17
def mult_7(n):
    S=0
    for i in range(1,n+1):
        if i%7==0:
            S=S+1
    return S 
print(mult_7(42))

#partie 2
def mult_7_pas_3_5(n):
    count=0
    for i in range(1,n+1):
        if i%7==0 and i%3!=0 and i%5!=0:
            count=count+1
    return count
print(mult_7_pas_3_5(50))




x=50
k=0
while x<1000:
    x=x+4*k
    print(x)
    k=k+1


def est_parfait(n):
    s=0
    for i in range (1,n+1):
        if n%i==0:
            s=s+i 
    return s==2*n
print(est_parfait(10))

x=50
k=0
while x<1000:
    x=x+4*k
    print(x)
    k=k+1

def factorielle(n):
    fact=1
    for i in range(1,n+1):
     fact=fact*i 
    return fact
print (factorielle(3))



#TP 2
#exercice 1
'''
vrai
faux 
vrai
faux 
vrai
vrai
vrai
faux
'''
#exercice 2
'''
B
j
7
print([7])IndexError
br
brrrr
yes there is 
false minuscule
true
false
bonjoura
bonjourbonjour
'''
#exercice3
'''
a="2"
b=3
a=a+"1"
b=a+"b"
print(a,b)=21 21b
'''
'''
A='a'
B='b'
A=A*2
B=A+B
print(A,B)=aab
'''
'''
a=0
b=1
a=a+b
b='a'+'b'
print(a,b)=1 ab
'''

'''
a='b'
b='a'
a=a*2
b=a+b
print(a,b)=bba
'''
#exercice4
'''def chaine(c,n):
    if n>0:
        return c*n
    else:
        return False 
ch='c'
number=3
result=chaine(ch,number)
print(result)'''
    
'''def chaine_2 (c,d,n,m):
    if (n>0 and m>0):
       return (c*n + d*m) 
    else:
        return False 
ch_1='c'
number_1=2
chh='d'
number_2=2
result=chaine_2(ch_1,chh,number_1,number_2)
print(result)'''

#exercie 6
'''def chaine_ch(ch,n):
    if n>0:
      for i in range(n):
        print(ch)
    else:
            return False
a='ch'
b=2
result=chaine_ch(a,b)
print(a,b)
'''

#exerice prof
'''message="anis"
message1=message.replace("anis","sina")
print(message1)


inverse="anis"
inverse1=inverse[::-1]
print(inverse1)

string='anis'
inverse = ''
for i in string :
    inverse = i + inverse 
print (inverse )'''




def suspect(ch):
    tentative=2
    mdp="ANIS1234"
if mdp!="ANIS1234":
        tentative=tentative-1
    return "le mot de passe est incorrect"
elif tentative >=2:
    return "on essaye de vous pirater"
else:
    return"le mot de passe est bon"


'''while tentative<=2:'''



liste=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

password='anis'
chaine=str()
mot= input("entrez votre mot de passe :")

def test1 (password,mot):
    if chaine==password:
        return 'le mot de passe est juste'
    else:
        return 'le mot de passe est incorrect'


def brut_force():
    for i in liste:
        chaine=i
        test1(chaine,mot)

        for i2 in liste:
            chaine=i+i2
            test1(chaine,mot)

            for i3 in liste:
                chaine=i+i2+i3
                test1(chaine,mot)

                for i4 in liste:
                    chaine=i+i2+i3+i4
                    test1(chaine,mot)

