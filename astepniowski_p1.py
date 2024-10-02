import os.path #used for file i/o

aidan, stepniowski = (5, 11) #cols, rows

mat1 = [[0 for i in range (aidan)] for j in range(stepniowski)]

mat2 = [[0 for i in range (aidan)] for j in range(stepniowski)]

num = 0
for j in range(aidan):
    for i in range(stepniowski):
        mat1[i][j] = num=num+1

num = 2
for j in range(stepniowski):
    for i in range(aidan):
        mat2[j][i] = num 
        num+=3

aidan, stepniowski = (2, 4)
mat3 = [[0 for i in range (aidan)] for j in range(stepniowski)]
num = 10
for j in range(aidan):
    for i in range(stepniowski):
        mat3[i][j] = num
        num-=2

mat4 = [[0 for i in range (aidan)] for j in range(stepniowski)]
num = -6
for j in range(stepniowski):
    for i in range(aidan):
        mat4[j][i] = num
        num+=1.5

dirname = os.path.dirname(__file__) #retrieve directory path
matricies = (mat1, mat2, mat3, mat4) #create an array container to hold our matrices

for n in range(len(matricies)): #iterate through all the matricies
    
    filename = os.path.join(dirname, "astepniowski_mat" +  str(n+1) + ".txt") #resolve relative directoy, append relative file name and create a string
    
    with open(filename, "a+") as f: #create file with our path if it dosen't exist, otherwise open it with write permissions
        for i in range(len(matricies[n])):
            if i > 0:
                f.write("\n") #seperate rows using a new line, skip the first iteration
            for j in range(len(matricies[n][i])):
                f.write(str(str(matricies[n][i][j]) + " "))
                #iterate through all the matricies and output to their respective text files using 'space space' as a delimiter
              
        
 