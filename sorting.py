import random
import pygame
from time import sleep

lenght = 100
toSort = random.sample(range(0,lenght),lenght)

def bubble_sort():
    global toSort
    loop = True
    while loop and running:
        loop = False
        for i in range(len(toSort)-1):
            if(toSort[i] > toSort[i+1]):
                toSort[i], toSort[i+1] = toSort[i+1], toSort[i]
                loop = True
                update((i,i+1))

def quicksort(A, lo, hi):
    global running,screen, sizeX, sizeY
    if not running:
        return

    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p-1)
        quicksort(A, p+1, hi)

def partition(A, lo, hi):    
    pivot = A[hi]
    i = lo
    for j in range(lo,hi):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            update((i, j))
            i += 1
    A[i], A[hi] = A[hi], A[i]
    update((i,hi))
    return i

def update(changes,temp=0.1):
    global running
    if not running:
        return

    for c in changes:
        x, y = c*unitX, toSort[c]*unitY
        pygame.draw.rect(screen,(0,255,0),((x,0,2,sizeY)))
        pygame.display.flip()
        rect = pygame.draw.rect(screen,(0,0,0),((x,0,2,sizeY)))
        color = baseColor
        color.hsva = (toSort[c]*unitColor,100,100,100)
        pygame.draw.rect(screen, color, (x, sizeY, 2, -y))
    sleep(temp)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

func = lambda: quicksort(toSort,0,len(toSort)-1)
#func = bubble_sort

sizeX, sizeY = 1000,500
unitX, unitY = (sizeX/len(toSort)), (sizeY/len(toSort))
baseColor = pygame.Color(0)
unitColor = (360/len(toSort))
running = True

pygame.init()
screen = pygame.display.set_mode((sizeX,sizeY))
screen.fill((0,0,0))
update(toSort,0)
pygame.display.flip()
func()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
