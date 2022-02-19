from tkinter import*
def ecrire(mot):
    if len(mot) == 0 or not isinstance(mot, str):
        return
    dico_mot=open("dico_mot.txt","a")
    dico_mot.write(str(mot)+"\n")
    dico_mot.close()
    
def lire():
    with open("dico_mot.txt","r") as lecteur:
        print(lecteur.read())

fen1=Tk()
Label(fen1,text="Enregistre un mot:",fg="blue").pack()
recherche=Entry(fen1)
recherche.pack()
Button(fen1, text="Enregistrer", command=lambda r=recherche:ecrire(recherche.get())).pack()
Button(fen1,text="Consulter le dictionnaire.",command= lire).pack()
fen1.mainloop()
