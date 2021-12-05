from time import sleep

def bubble_sort(file):
    fileKeys,fileValues = list(file),list(file.values())
    loop = True
    while loop:
        loop = False
        for i in range(len(file)-1):
            if(fileValues[i] > fileValues[i+1]):
                file[fileKeys[i]], file[fileKeys[i+1]] = file[fileKeys[i+1]], file[fileKeys[i]]
                loop = True
                update((i,i+1))

def quicksort(file, lo, hi):
    fileKeys,fileValues = list(file),list(file.values())

    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p-1)
        quicksort(A, p+1, hi)

def partition(A, lo, hi):    
    pivot = A[hi]
    i = lo
    for j in range(lo,hi):
        if A[j] < pivot:
            #A[i], A[j] = A[j], A[i]
            file[fileKeys[i]], file[fileKeys[j]] = file[fileKeys[j]], file[fileKeys[i]]
            update((i, j))
            i += 1
    #A[i], A[hi] = A[hi], A[i]
    file[fileKeys[i]], file[fileKeys[j]] = file[fileKeys[j]], file[fileKeys[i]]
    update((i,hi))
    return i

def update(changes):
    print(changes)

path = "C:/Users/willi/Downloads/hunspell-french-dictionaries-v7.0/"
filename = "fr-classique.dic"

with open(path+filename,'rb') as f:
    file = {}
    for line in f.readlines():
        word = line.split(b"/")[0]
        file[word] = len(word)

bubble_sort(file)

with open(path+'fr-classique-words.txt','wb') as f:
    for word in file:
        f.write(word)
        f.write(b"\n")
print("Done!")
