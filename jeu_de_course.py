from tkinter import*

def circuit_droit(x1=50,x2=50):
    can1.create_line( x1 , 500 , x2 , 5 )

def modifier():
    circuit_droit(550,550)
   
fen1 = Tk()

can1 = Canvas(fen1,bg="dark grey",height=500,width=500)
can1.pack()

bou1 = Button(fen1,text="Quitter",command = fen1.destroy)
bou1.pack()


bou2 = Button(fen1,text="Modifier",command = modifier)
bou2.pack()

bou2 = Button(fen1,text="Tracer",command = circuit_droit)
bou2.pack()
    
fen1.mainloop()


