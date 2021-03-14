import pygame
import random
import sys
import time
pygame.init()

# Images
icon = pygame.image.load("sortingIcon1024.png")

# Make screen
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 169, 94))
pygame.display.set_caption("Sorting Algorithm Visualisation")
pygame.display.set_icon(icon)

# Variables
numberArray = [None] * 100

# Fill array with random numbers
for i in range(0, len(numberArray)):
    numberArray[i] = random.randint(200, 600)

def displayArray(arr):
    x = 0
    for i in range(0, len(arr) - 1):
        pygame.draw.rect(screen, (63, 82, 209), (x, 0, 10, arr[i]))
        x += 10
    pygame.display.update()

def quickSort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()

    greater = []
    lower = []

    for num in arr:
        if num > pivot:
            greater.append(num)

        else:
            lower.append(num)

    screen.fill((255, 169, 94))
    displayArray(lower + [pivot] + greater)
    pygame.display.update()
    time.sleep(0.20)
    return quickSort(lower) + [pivot] + quickSort(greater)

displayArray(numberArray)
time.sleep(2)
sorted = quickSort(numberArray)
screen.fill((255, 169, 94))
pygame.display.update()
time.sleep(2)
displayArray(sorted)

notExit = True
while notExit:
    for event in pygame.event.get():
        # If the player presses the exit window button, then quit the program
        if event.type == pygame.QUIT:
            notExit = False