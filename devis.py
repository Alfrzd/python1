Art1 = str(input("Entrez le nom de l'article1:"))
Qte1 = int(input("Quelle quantité voulez-vous pour cet article:"))
Pu1= 3250
Pu2=650
PA1 = Pu1*Qte1
Art2 = str(input("Entrez le nom de l'article2 souhaité:"))
if Art1 == Art2:
        print("Cet article à deja été enregistré")
        reponse = str(input("voulez-vous modifier sa quantité? oui/non"))
        if reponse == "oui":
             Qte1=(input("Quelle quantité voulez-vous pour cet article:"))
             Pu1= 3250
             PA1 = Pu1*Qte1
        elif reponse == "non":
         print( "passez au prochain article")
Art2 = str(input("Entrez le nom de l'article2:"))
Qte2 = int(input("Quelle quantité voulez-vous pour cet article:"))
Pu= 356
PA2= Pu*Qte2
print(Art1,"-----------","Prix Unitaire:--",Pu1,"------Quantité:",Qte1,"---Total1:---",PA1)
print(Art2,"-----------","Prix Unitaire:--",Pu,"------Quantité:",Qte2,"---Total2:---",PA2)