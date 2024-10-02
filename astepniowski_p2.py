import os.path
import re

dirname = os.path.dirname(__file__) #resolve relative directory

outputFilePath = os.path.join(dirname, "astepniowski_p2_out") 

def checkDimensions(mat1array, mat2array): #check matrix dimensions to ensure they can be added
    if(len(mat1array) == len(mat2array)):
        for i in range(len(mat1array)):
                if len(mat1array[i]) == len(mat2array[i]):
                    return True
    print("matrix dimensions are not the same, and thus cannot be added")

def parseFile(file): #remove all new lines, and extract every number from each line to an array
    a = []
    for line in file:
        line = line.replace("\n", "")
        a.append([round(float(x), 1) for x in line.split()])

    return a

def resolveFile(): #resolve relative matrix output file from p1
    
    matrixNumber = input("Enter the first matrix to add (mat#) : ") #fetch user input
    filename = os.path.join(dirname, "astepniowski_" + matrixNumber.lower() + ".txt") 
    
    global outputFilePath #reference global variable instead of creating a new local reference
    outputFilePath += re.findall("\d", matrixNumber)[0] #extract int from the matrixNumber string to append to our output file name

    return filename


matOneFilePath = resolveFile()
matTwoFilePath = resolveFile()
outputFilePath += ".txt" #append the .txt extension

with open(matOneFilePath) as one:
    with open(matTwoFilePath) as two:

        mat1array = parseFile(one)
        mat2array = parseFile(two)

        if checkDimensions(mat1array, mat2array) == True:

            o = open(outputFilePath, "a+")

            for i in range(len(mat1array)):
                if i > 0:
                    o.write ("\n")
                for j in range(len(mat2array[i])):
                    o.write(str(mat1array[i][j]+mat2array[i][j]) + "  ")
            #iterate through the arrays retrieved from the parseFile function and print the addition results between the two to the output file
            o.close()