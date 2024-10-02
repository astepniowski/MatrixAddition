import numpy as np
import os.path
import re

dirname = os.path.dirname(__file__)

outputFilePath = os.path.join(dirname, "astepniowski_p3_out")

def resolveFile():
    
    matrixNumber = input("Enter the first matrix to add (mat#) : ") #fetch user input
    filename = os.path.join(dirname, "astepniowski_" + matrixNumber.lower() + ".txt") #resolve relative matrix output file from p1
    
    global outputFilePath
    outputFilePath += re.findall("\d", matrixNumber)[0]

    return filename

matOneFilePath = resolveFile()
matTwoFilePath = resolveFile()
outputFilePath += ".txt"
#all of the code above is reused from the p2 file, refer to 'astepniowskip2.py' for documentation


array1 = np.loadtxt(matOneFilePath, dtype=float) 
array2 = np.loadtxt(matTwoFilePath, dtype=float)
#parse the matrix text files to a numpy array

np.savetxt(outputFilePath, np.add(array1, array2), fmt='%s')
#save the result of adding our numpy arrays to a txt file, formated as a string