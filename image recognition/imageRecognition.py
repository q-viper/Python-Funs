#Image recognition using python 3.5
#Step 1 creating a database.

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from collections import Counter
from functools import reduce

np.seterr(over = 'ignore')



def applyThreshold(imageArray):
    balanceArray = []
    newArray = imageArray

    try:
       
        for eachRow in imageArray:
            for eachPixel in eachRow:
                averageNumber = reduce(lambda x,y: x + y, eachPixel[:3])/len(eachPixel[:3])
                balanceArray.append(averageNumber)

        balance = np.average(balanceArray)

        for eachRow in newArray:
            for eachPixel in eachRow:
                if reduce(lambda x,y: x + y, eachPixel[:3])/len(eachPixel[:3])>balance:
                    eachPixel[0] = 255
                    eachPixel[1] = 255
                    eachPixel[2] = 255
                    eachPixel[3] = 255
                else:
                    eachPixel[0] = 0
                    eachPixel[1] = 0
                    eachPixel[2] = 0
                    eachPixel[3] = 255

        return(newArray)

    except:
        return(imageArray)


#Save all arrays equivalent to image inside some file.

def createLetterExamples():
    letterArraysFile = open('letterArrays.txt','a')
    lettersWithUs = ['A', 'B', 'C', 'D', 'E']
    versionsOfLetters = range(1,6)

    for eachLetter in lettersWithUs:
        for eachVersion in versionsOfLetters:
            imageLocation = 'images/' + eachLetter + '.' + str(eachVersion) + '.png'
            openImage = Image.open(imageLocation)

            imageArray = applyThreshold(np.array(openImage))
            imageArrayList = str(imageArray.tolist())
            writeLine = eachLetter + ': :' + imageArrayList + '\n'
            letterArraysFile.write(writeLine)
#createLetterExamples()

#Checking the user input image and database.

def checkWhichWord(fileLocation):
    matchedArray = []
    loadExamplesFile = open('letterArrays.txt', 'r').read()
    loadExamples = loadExamplesFile.split('\n')

    checkImage = Image.open(fileLocation)
    imageArray = applyThreshold(np.array(checkImage))
    imageArrayList = str(imageArray.tolist())

    for eachExample in loadExamples:
        if len(eachExample)>3:
            splitExample = eachExample.split(': :')
            currentLetter = splitExample[0]
            currentArray = splitExample[1]
            eachPixelInImage = imageArrayList.split('],')
            eachPixelInExample = currentArray.split('],')

            x = 0

            while x < len(eachPixelInExample):
                if eachPixelInExample[x] == eachPixelInImage[x]:
                    matchedArray.append(currentLetter)

                x = x+1

    countMatched = Counter(matchedArray)
    return(countMatched)

checkedResults = checkWhichWord('images/D.png')

x = []
labels = []
explode = []
exp = 0
for key, value in checkedResults.items():
    x.append(value)
    labels.append(key)
    explode.append(exp)
    exp = exp + 0.1
    
    
fig = plt.figure()
plt.pie(x, labels = labels,explode = explode, autopct = '%1.1f%%')
plt.title('Result in pie chart.')

plt.show()



























