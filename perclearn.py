import glob
import sys
import os

my_path = sys.argv[1]

vocabulary = set()
input_vector_weights = {}
input_vector_avg_weights = {}
max_iterations = 100
c = 1
b = 0
beta = 0
yham = -1
yspam = 1



#Recursively reading ham and spam files and in alphabetical order of files and then subfolders
all_files = [] #glob.glob(my_path + '/**/*.txt', recursive=True)

def list_files_directories(filepath):
    files = []
    directories = []
    filepath_content = os.listdir(filepath)

    for con in filepath_content:        
        if os.path.isdir(filepath +"/"+con):
            directories.append(filepath +"/"+con)
        else:
            #print(con)
            if con.endswith('.txt'):
                 files.append(filepath +"/"+con)

    files.sort()
    directories.sort()

    for file in files:        
        all_files.append(file)
    
    for dire in directories:
        list_files_directories(dire)



list_files_directories(my_path)

#Creating vocabulary i.e the d dimensions
for filename in all_files:
    f = open(filename, "r", encoding="latin1")
    for line in f:
        for word in line.split():              
             if word in input_vector_weights.keys(): 
                continue
             else:
                input_vector_weights[word] = 0
                input_vector_avg_weights[word] = 0
                vocabulary.add(word)

    f.close()


print(len(input_vector_weights))
print(len(input_vector_avg_weights))

#Training the perceptron model
for i in range(0, 100):
    for filename in all_files:        
        f = open(filename, "r", encoding="latin1")

        if filename.find("ham") > -1:
            y = yham
        else:
            y=yspam
        alpha = b

        words = []
        for line in f:
            for word in line.split():
                words.append(word)
                alpha = alpha + input_vector_weights[word] 
        
        yalpha = alpha * y
        # print(yalpha)
        if yalpha <= 0:
            b = b + y
            beta = beta + (y * c)  
            for newword in words:             
                input_vector_weights[newword] = input_vector_weights[newword] + y
                input_vector_avg_weights[newword] = input_vector_avg_weights[newword] + (y * c) 
                
        c = c+1       
        f.close()

   


for key, value in input_vector_avg_weights.items():
    input_vector_avg_weights[key] = input_vector_weights[key] - ((1/c) * input_vector_avg_weights[key]) 

beta = b - ((1/c) * beta)
# print (beta)
# for key, value in input_vector_avg_weights.items():
#     print( str(key) + ": " + str(value))



f = open("percmodel.txt", "w")

f.write(str(beta) + "\n")
f.write(str(len(input_vector_avg_weights)) + "\n")


for key, value in input_vector_avg_weights.items():
    f.write(key +" "+ str(value) + "\n")

f.close()

