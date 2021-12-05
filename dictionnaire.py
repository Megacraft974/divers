from tkinter import*
def ecrire(mot):
    dico_mot=open("dico_mot.txt","a")
    dico_mot.write(str(mot)+"\n")
    dico_mot.close()
    
def lire():
    lecteur=open("dico_mot.txt","r")
    lecture=lecteur.read()
    print(lecture)
    lecteur.close()

fen1=Tk()
enregistrer=Label(fen1,text="Enregistre un mot:",fg="blue")
recherche=Entry(fen1)
affiche=Button(fen1,text="Consulter le dictionnaire.",command= lire())
enregistrer.pack()
recherche.pack()
affiche.pack()
fen1.mainloop()

ecrire(recherche)
