import glob
import sys
import math
import random

my_path = sys.argv[1]

actual_ham_count = 0
actual_spam_count = 0
predicted_ham_count = 0
predicted_spam_count = 0

ham_true_positive = 0
spam_true_positive = 0

ham_false_negative = 0
spam_false_negative = 0

with open(my_path) as fp:
	Lines = fp.readlines()
	for line in Lines:
		keyVal = line.split()
		path = keyVal[1]
		predicted_class = keyVal[0]
		if (path.find("ham") == -1 and path.find("spam") == -1):
			continue

		elif path.find("ham") > -1:
			actual_ham_count += 1
			if predicted_class == "spam":
				ham_false_negative +=1

		elif path.find("spam") > -1:
			actual_spam_count += 1
			if predicted_class == "ham":
				spam_false_negative +=1

		if predicted_class == "ham":
			predicted_ham_count +=1
			if path.find("ham") > -1:
				ham_true_positive += 1


		else:
			predicted_spam_count +=1
			if path.find("spam") > -1:
				spam_true_positive += 1

ham_accuracy = (ham_true_positive / actual_ham_count)
spam_accuracy = (spam_true_positive / actual_spam_count)

ham_precision = (ham_true_positive / predicted_ham_count)
spam_precision = (spam_true_positive / predicted_spam_count)

ham_recall = (ham_true_positive /(ham_true_positive + ham_false_negative))
spam_recall = (spam_true_positive / (spam_true_positive + spam_false_negative))

ham_f1_score = ( 2 * ham_precision * ham_recall)/(ham_precision + ham_recall)
spam_f1_score = (2 * spam_precision * spam_recall)/ (spam_precision + spam_recall)

print("Spam -  Accuracy:" + str(spam_accuracy) +" Precision:"+ str(spam_precision) +  " Recall:"+ str(spam_recall) +" F1 Score:" + str(spam_f1_score))
print("Ham -  Accuracy:" + str(ham_accuracy) +" Precision:"+ str(ham_precision) +  " Recall:"+ str(ham_recall) +" F1 Score:" + str(ham_f1_score))



