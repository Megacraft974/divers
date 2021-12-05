def lettre(c):
        l=0
        while l<c:
                try:
                        s=chr(l)
                        print(l,s)
                        int(l)
                        l=l+1
                except:
                        print("Il n'y a plus de chiffre."+str(l))
                        int(l)
                        l=l+1
