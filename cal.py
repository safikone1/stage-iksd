def addition(a,b):
    return(a+b)
def soustraction(a,b):
    return(a-b)
def multiplication(a,b):
 return(a*b)
def division(a,b):
   if a!= 0:
     return a/b
   else:
      print("erreur de divison")
      return None
   print("selectiooner une operation")
   print("1 addition")
   print("2 soustraction")
   print("3 multiplication")
   print("4 division")

   choix= input("entre votre choix(1/2/3/4)")
   num1= float(input("entrez le premier nombre"))
   num2= float(input("entrez le seconde nombre"))

   if choix==1:
      resultat=addition(num1,num2)
      print("Le resultat de l'addition est:",resulat)
   elif choix==2:
      resultat=soustraction(num1,num2)
      print("le resultat de la soustraction est:",resultat)
   elif choix==3:
      resultat=multiplication(num1,num2)
      print("le resultat de la multiplication est:",resultat)
   elif choix==4:
      resultat=division(num1,num2)
      print("le resultat de la division est:",resultat)
   if resultat is not None:
      print("le resultat est:",resultat)
   else:
     print("resultat invalide:")

        