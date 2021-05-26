import glob
import sys

my_path = sys.argv[1]

vocabulary = set()
ham_dict = {}
spam_dict = {}
prob_ham_dict = {}
prob_spam_dict = {}
total_ham_words = 0
total_spam_words = 0
total_words = 0


#Recursively reading ham and spam files
ham_files = glob.glob(my_path + '/*/ham/*.txt', recursive=True)
spam_files = glob.glob(my_path + '/*/spam/*.txt', recursive=True)

#Calculating P(ham) and  P(spam)
ham_count = len(ham_files)
spam_count = len(spam_files)
prob_ham = 0
prob_spam = 0

if ham_count + spam_count > 0:
    prob_ham = ham_count/ (ham_count + spam_count)
    prob_spam = spam_count/ (ham_count + spam_count)


#Creating vocabulary and calculating word frequencies
for filename in ham_files:
    f = open(filename, "r", encoding="latin1")
    for line in f:
        for word in line.split():   
            if word in ham_dict.keys(): 
                ham_dict[word] = ham_dict[word] + 1

            else:
                ham_dict[word] = 1
                vocabulary.add(word)
    f.close()


for filename in spam_files:
    f = open(filename, "r", encoding="latin1")
    for line in f:
        for word in line.split():
            if word in spam_dict.keys(): 
                spam_dict[word] = spam_dict[word] + 1

            else:
                spam_dict[word] = 1
                vocabulary.add(word)
    f.close()


# counting total ham and spam words
for key, value in ham_dict.items():
    total_ham_words += value

for key, value in spam_dict.items():
    total_spam_words += value


#calculating the conditional probabilities of words P(word|ham) and P(word|spam)
for key, value in ham_dict.items():
    prob_ham_dict[key] = value/total_ham_words

for key, value in spam_dict.items():
    prob_spam_dict[key] = value/total_spam_words

# print(ham_dict)
# print("..................................")
# print(spam_dict)

# print("..................................")
# for v in vocabulary:
#     print(v)


print(len(vocabulary))
print(ham_count)
print(spam_count)
print(total_ham_words)
print(total_spam_words)
print(len(prob_ham_dict))
print(len(prob_spam_dict))

# for key, value in prob_ham_dict.items():
#     print(key, value)

f = open("nbmodel.txt", "w")

f.write(str(len(vocabulary)) + "\n")
f.write(str(ham_count) + "\n")
f.write(str(spam_count) + "\n")
f.write(str(total_ham_words) + "\n")
f.write(str(total_spam_words) + "\n")
f.write(str(len(prob_ham_dict)) + "\n")
f.write(str(len(prob_spam_dict)) + "\n")


for key, value in prob_ham_dict.items():
    f.write(key +" "+ str(value) + "\n")
for key, value in prob_spam_dict.items():
    f.write(key +" "+ str(value) + "\n")
f.close()