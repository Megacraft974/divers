dico = open("le_dictionnaire_fou.txt","r")
mot=0
def creer_une_phrase():
    compteur=0
    mot1a=range(0,9)
    mot2a=range(0,9)
    mot3a=range(0,9)
    for mot1 in dico:
        if compteur == mot1a:
            compteur=0
        else:
            compteur=compteur+1
    for mot2 in dico:
        if compteur == mot2a:
            compteur=0
        else:
            compteur=compteur+1
    for mot3 in dico:
        if compteur == mot3a:
            compteur=0
        else:
            compteur=compteur+1
    print(mot1,mot2,mot3)
question = input("Si vous souhaitez creer une phrase,entrez 1.Si vous souhaitez entrer un mot,entrez 2.")
if question == 1:
    creer_une_phrase()
if question == 2:
    phrase = input("Taper le mot que vous souhaitez entrer,suivi de virgule et f s'il est feminin ou, a l'inverse, suivi de virgule et m s'il est masculin.")
    dico = open("le_dictionnaire_fou.txt","w")
    dico.write(str("phrase"))
    mot=mot+1
dico.close()
