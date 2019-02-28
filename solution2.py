import os

import random as random


filepath = "c_memorable_moments.txt"


def min_set(A, B):
    A_prime = A.difference(B)
    B_prime = B.difference(A)
    C = A.intersection(B)

    return min(len(A_prime), len(B_prime), len(C))

def retrieve_tags(slide, photos):
    """
        slide - [int, int] or [int]
    """
    tags = []

    for photo_id in slide:
        photo_tags = photos[photo_id]
        tags.extend(photo_tags)

    return tags

def scoreOfTwo(id1, id2):
    A = set(photos[id1].tags)
    B = set(photos[id2].tags)
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

photos = []
photosAsList = []

with open(filepath) as fp:  
    n = int(fp.readline())
    for i in range(n):
        line = fp.readline().split()
        if line[0] == 'H':
            photos.append(Photo(id = i, kind = line[0], tags = line[2:]))
            photosAsList.append(line[2:])

answer = []
used = [False for _ in range(len(photos))]
for i in range(len(photos)):
    if not used[i]:
        used[i] = True
        bestPhotoIndex = -1
        bestFit = 0
        for j in range(len(photos)):
            if i != j and not used[j]:
                score = scoreOfTwo(i, j)
                if score > bestFit:
                    bestFit = score
                    bestPhotoIndex = j
        
        if bestPhotoIndex >= 0:
            used[bestPhotoIndex] = True
            answer.append(photos[i].id)
            answer.append(photos[bestPhotoIndex].id)


fw = open("result2.txt","w")

fw.write(str(len(answer)))
fw.write("\n")
for photoID in answer:
    # writer.write(str(photoID) + " kind " + photos[photoID].kind)
    fw.write(str(photoID))
    fw.write("\n")