import glob
import sys
import math
import random
import os

my_path = sys.argv[1]


##Recursively reading test files and in alphabetical order of files and then subfolders
#files = glob.glob(my_path + '/**/*.txt', recursive=True)

files = []
def list_files_directories(filepath):
    my_files = []
    directories = []
    filepath_content = os.listdir(filepath)

    for con in filepath_content:        
        if os.path.isdir(filepath +"/"+con):
            directories.append(filepath +"/"+con)
        else:
            #print(con)
            if con.endswith('.txt'):
                 my_files.append(filepath +"/"+con)

    my_files.sort()
    directories.sort()

    for file in my_files:        
        files.append(file)
    
    for dire in directories:
        list_files_directories(dire)



list_files_directories(my_path)


#Reading Model data from nbmodel.txt
model_file = open('percmodel.txt', 'r')

avg_weights_vector = {}
beta = float(model_file.readline())
dimension = int(model_file.readline())

for j in range(0, dimension):
	line = model_file.readline()
	keyVal = line.split()
	avg_weights_vector[keyVal[0]] = float(keyVal[1])


#opening file to write output
outFile = open("percoutput.txt", "w")
#Reading test files and calculation P(msg|ham) and P(msg|spam) 
for filename in files:
	f = open(filename, "r", encoding="latin1")
	alpha = beta
	for line in f:
		for word in line.split():   
			if word in avg_weights_vector.keys():  
				alpha += avg_weights_vector[word]

	f.close()

	if alpha > 0:
		outFile.write("spam" + " " + filename+ "\n")

	else:
		outFile.write("ham" +" " +filename+ "\n")

outFile.close()
model_file.close()