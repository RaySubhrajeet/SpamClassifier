import glob
import sys
import math
import random

my_path = sys.argv[1]


#Recursively read all the tresting file paths
files = glob.glob(my_path + '/**/*.txt', recursive=True)


#Reading Model data from nbmodel.txt
model_file = open('nbmodel.txt', 'r')

train_ham_probability_dict = {}
train_spam_probability_dict = {}

vocabSize= int(model_file.readline())

ham_files_count = int(model_file.readline())
spam_files_count = int(model_file.readline())

ham_count= int(model_file.readline())
spam_count = int(model_file.readline())

ham_dict_size = int(model_file.readline())
spam_dict_size = int(model_file.readline())

for j in range(0, ham_dict_size):
	line = model_file.readline()
	keyVal = line.split()
	train_ham_probability_dict[keyVal[0]] = float(keyVal[1])

for j in range(0, spam_dict_size):
	line = model_file.readline()
	keyVal = line.split()
	train_spam_probability_dict[keyVal[0]] = float(keyVal[1])


ham_probability = (ham_count/(ham_count + spam_count))
spam_probability = (spam_count/(ham_count + spam_count))

# test_spam_probability = {}
# test_ham_probability = {}

#opening file to write output
outFile = open("nboutput.txt", "w")
#Reading test files and calculation P(msg|ham) and P(msg|spam) 
for filename in files:
	f = open(filename, "r", encoding="latin1")
	log_spam_prob = math.log(spam_probability)
	log_ham_prob = math.log(ham_probability)
	for line in f:
		for word in line.split():   
			#Calculating ham probability
			if word in train_ham_probability_dict.keys(): 
				log_ham_prob += math.log(train_ham_probability_dict[word])
			#calculating ham probability using smoothing
			else:
				if word in train_spam_probability_dict.keys(): 
					 smoothing_ham_prob = 1/(ham_count + vocabSize)
					 log_ham_prob += math.log(smoothing_ham_prob)


			#Calculating spam probability
			if word in train_spam_probability_dict.keys(): 
				log_spam_prob += math.log(train_spam_probability_dict[word])
			#calculating ham probability using smoothing
			else:
				if word in train_ham_probability_dict.keys(): 
					 smoothing_spam_prob = 1/(spam_count + vocabSize)
					 log_spam_prob += math.log(smoothing_spam_prob)

	f.close()

	if log_spam_prob > log_ham_prob:
		outFile.write("spam" +" " +filename+ "\n")

	elif log_ham_prob > log_spam_prob:
		outFile.write("ham" +" " +filename+ "\n")

	else:
	    randomVal= random.uniform(0, 1)
	    if randomVal == 0:
	  	 	outFile.write("spam" +" " +filename+ "\n")
	    else:
	   		outFile.write("ham" +" " +filename+ "\n")


outFile.close()
model_file.close()


				   

#print len(Lines)
# print (vocabSize)
# print(ham_count)
# print(spam_count)
# print(ham_dict_size)
# print(spam_dict_size)


# print(len(spam_probability_dict))
# print(len(ham_probability_dict))