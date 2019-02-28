import os
import math

import random as random


filepath = "e_shiny_selfies.txt"


def min_set(A, B):
    A_prime = A.difference(B)
    B_prime = B.difference(A)
    C = A.intersection(B)

    return min(len(A_prime), len(B_prime), len(C))

def dmin_set(A, B):
    A_prime = A.difference(B)
    B_prime = B.difference(A)
    C = A.intersection(B)

    return min(len(A_prime), len(B_prime), len(C))

def scoreOfTwo(id1, id2):
    A = set(photos[id1].tags)
    B = set(photos[id2].tags)
    score_pair = min_set(A, B)
    return score_pair

def dscoreOfTwo(id1, id2):
    A = set(dphotos[id1].tags)
    B = set(dphotos[id2].tags)
    score_pair = min_set(A, B)
    return score_pair

class Photo:
    def __init__(self, id, kind, tags):
        self.id = id
        self.kind = kind
        self.tags = tags

    def __str__(self):
        result = ""
        for tag in self.tags:
            result += tag + " "
        return "Photo of type " + self.kind + " with tags: " + result

class DoublePhoto:
    def __init__(self, id1, id2, kind, tags):
        self.id1 = id1
        self.id2 = id2
        self.kind = kind
        self.tags = tags

    def __str__(self):
        result = ""
        for tag in self.tags:
            result += tag + " "
        return "Photo of type " + self.kind + " with tags: " + result

photos = []
photosAsList = []
dphotos = []
dphotosAsList = []

with open(filepath) as fp: 
    lastVerticalPhoto = None
    n = int(fp.readline())
    for i in range(n):
        line = fp.readline().split()
        if line[0] == 'H':
            photos.append(Photo(id = i, kind = line[0], tags = line[2:]))
            photosAsList.append(line[2:])
        else:
            if lastVerticalPhoto == None:
                lastVerticalPhoto = Photo(id = i, kind = line[0], tags = line[2:])
            else:
                cur = Photo(id = i, kind = line[0], tags = line[2:])
                ctags = list(set(lastVerticalPhoto.tags + cur.tags))
                dphotos.append(DoublePhoto(lastVerticalPhoto.id, cur.id, 'V', ctags))
                dphotosAsList.append(ctags)
                lastVerticalPhoto = None

# photos = photos[:10300]

answer = []
used = [False for _ in range(len(photos))]
for i in range(len(photos)):
    if not used[i]:
        used[i] = True
        if i % 500 == 0:
            print(i)
        bestPhotoIndex = -1
        bestFit = 0
        step = int(math.sqrt(len(photos) - i) / 8)
        if step > 0:
            for j in range(0, len(photos), step):
                if i != j and not used[j]:
                    score = scoreOfTwo(i, j)
                    if score > bestFit:
                        bestFit = score
                        bestPhotoIndex = j
            
            if bestPhotoIndex >= 0:
                used[bestPhotoIndex] = True
                answer.append([photos[i].id])
                answer.append([photos[bestPhotoIndex].id])

dused = [False for _ in range(len(dphotos))]
for i in range(len(dphotos)):
    if not dused[i]:
        dused[i] = True
        if i % 500 == 0:
            print(i)
        bestPhotoIndex = -1
        bestFit = 0
        step = int(math.sqrt(len(dphotos) - i) / 8)
        if step > 0:
            for j in range(0, len(dphotos), step):
                if i != j and not dused[j]:
                    score = dscoreOfTwo(i, j)
                    if score > bestFit:
                        bestFit = score
                        bestPhotoIndex = j
            
            if bestPhotoIndex >= 0:
                dused[bestPhotoIndex] = True
                answer.append([dphotos[i].id1, dphotos[i].id2])
                answer.append([dphotos[bestPhotoIndex].id1, dphotos[bestPhotoIndex].id2])


fw = open("result2.txt","w")

fw.write(str(len(answer)))
fw.write("\n")
for photoset in answer:
    for photo in photoset:
        fw.write(str(photo) + " ")
    fw.write("\n")