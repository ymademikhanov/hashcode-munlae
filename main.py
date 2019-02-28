import os
import sys
import random as random
from evaluate import score

random.seed(1000)

class Photo:
    def __init__(self, kind, tags):
        self.kind = kind
        self.tags = tags

    def __str__(self):
        result = ""
        for tag in self.tags:
            result += tag + " "
        return "Photo of type " + self.kind + " with tags: " + result

class Frame:
    def __init__(self, photoIDs):
        self.kind


class Slide:
    def __init__(self, photoIDs):
        self.length = len(photoIDs)
        self.photoIDs = photoIDs
    
    def mutate(self):
        a = 0
        b = 0
        # print("length of slide:", self.length)
        while a == b:
            a = random.randint(0, self.length - 1)
            b = random.randint(0, self.length - 1)
            # print("randoming")
        # swapping.
        self.photoIDs[a], self.photoIDs[b] = self.photoIDs[b], self.photoIDs[a]

    def crossover(self, otherSlide):
        genes = self.photoIDs[0 : int(self.length / 2)]
        usedGenes = set()
        for gene in genes:
            usedGenes.add(gene)

        for gene in otherSlide.photoIDs:
            if gene not in usedGenes:
                genes.append(gene)

        # print("genes.length:", len(genes))
        return Slide(genes)

    def fitnessScore(self):
        l = []
        for photoID in self.photoIDs:
            l.append([photoID])
        return score(l, photosAsList)
    
    def __str__(self):
        result = "[ "
        for photoID in self.photoIDs:
            result += str(photoID) + ", "
        result += "]"
        return result

class Population:
    def __init__(self, selectionRate, populationSize):
        self.selectionRate = selectionRate
        self.populationSize = populationSize
        self.slides = []

    def addSlide(self, slide):
        self.slides.append(slide)

    def fitnessAndSort(self):
        self.slides.sort(key=lambda slide : slide.fitnessScore())

    def reproduce(self):
        newPopulation = []
        # crossover
        # print("len(slides):", len(self.slides))
        for slide1 in self.slides:
            for slide2 in self.slides:
                if slide1 != slide2:
                    offspring = slide1.crossover(slide2)
                    # print("new offspring")
                    # mutation.
                    offspring.mutate()
                    # print("new offspring mutated")
                    newPopulation.append(offspring)

        self.slides = newPopulation
        # print("cross-over done")

        # sort slides
        self.fitnessAndSort()
        # print("sorted")

        # cut-off
        self.slides = self.slides[ : int(self.populationSize)]
        # print("cut-off")

    def returnBestSlide(self, writer):
        bestSlide = self.slides[0]
        writer.write(str(len(bestSlide.photoIDs)))
        writer.write("\n")
        for photoID in bestSlide.photoIDs:
            # writer.write(str(photoID) + " kind " + photos[photoID].kind)
            writer.write(str(photoID))
            writer.write("\n")

# filepath = input()
filepath = "b_lovely_landscapes.txt"
photos = []
photosAsList = []

with open(filepath) as fp:  
    n = int(fp.readline())
    for i in range(n):
        line = fp.readline().split()
        photos.append(Photo(kind = line[0], tags = line[2:]))
        photosAsList.append(line[2:])

validIDs = []
for i in range(len(photos)):
    if photos[i].kind == 'H':
        validIDs.append(i)

population = Population(0.2, 20)

for i in range(20):
    slide = Slide([ID for ID in validIDs])
    population.addSlide(slide)

generation = 0
while generation < 10:
    print("generation:", generation)
    population.reproduce()
    generation += 1

population.fitnessAndSort()

fw = open("result.txt","w")
population.returnBestSlide(fw)



