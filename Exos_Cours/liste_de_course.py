
def afficher_liste(courses):
    if not courses:
        print("La liste est vide.")
    else:
        print("Liste des courses :")
        for article in courses:
            print("-", article)

def ajouter_article(courses, article):
    courses.append(article)
    print(f"{article} a été ajouté à la liste.")

def retirer_article(courses, article):
    if article in courses:
        courses.remove(article)
        print(f"{article} a été retiré de la liste.")
    else:
        print(f"{article} n'est pas dans la liste.")

def compter_articles(courses):
    return len(courses)


ma_liste = []

while True:
    print("\nQue voulez-vous faire ?")
    print("1 - Afficher la liste")
    print("2 - Ajouter un article")
    print("3 - Retirer un article")
    print("4 - Compter les articles")
    print("5 - Quitter")

    choix = input("Entrez le numéro de votre choix : ")

    if choix == "1":
        afficher_liste(ma_liste)
    
    elif choix == "2":
        article = input("Entrez le nom de l'article à ajouter : ")              
        ajouter_article(ma_liste, article)
   
    elif choix == "3":
        article = input("Entrez le nom de l'article à retirer : ")
        retirer_article(ma_liste, article)

    elif choix == "4":
        print("Nombre d'articles :", compter_articles(ma_liste))
   
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, veuillez réessayer.")
