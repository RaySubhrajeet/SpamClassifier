# SpamClassifier

Naive Bayes and a Perceptron classifier to identify spam messages

This is done as part of coursework for CSCI-544, Natural Language Processing at University of Southern California.

Naïve Bayes Classifier 
nbclassify.py use the model to classify new data, and nbevaluate.py print precision, recall, and F1 scores based on the output of nbclassify.py on development (i.e., labeled) data. 

1. Write nblearn.py
nblearn.py is invoked in the following way:
>python3 nblearn.py input_data_path and output a model file called nbmodel.txt

1.1 Reading data
The argument is a data directory. The script  searches through the directory recursively looking for subdirectories containing the folders: "ham" and "spam". Note that there can be multiple "ham" and "spam" folders in the data directory. Emails are stored in files with the extension ".txt" under these directories. 

ham and spam folders contain emails failing into the category of the folder name (i.e., a spam folder will contain only spam emails and a ham folder will contain only ham emails). Each email is stored in a separate text file. The emails have been preprocessed removing HTML tags, and leaving only the body and the subject. The files have been tokenized such that white space always separates tokens.

1.2 Learning the model
Estimates and stores P(spam) and P(ham) as well as conditional probabilities P(token|spam) and P(token|ham) for all unique tokens. These probabilities are then  stored in the model file nbmodel.txt. 
For smoothing add-one smoothing is used. During testing, unknown tokens not seen in training (i.e., pretend they did not occur) are ignored.

2. Write nbclassify.py
nbclassify.py is invoked in the following way:
>python3 nbclassify.py input_data_path
The argument is again a data directory . nbclassify.py reads the parameters of the naïve Bayes model from the file nbmodel.txt, and classify each ".txt" file in the data directory as "ham" or "spam", and write the result to a text file called nboutput.txt in the format below:
LABEL path_1
LABEL path_2
⋮
In the above format, LABEL is either “spam” or “ham” and path is the absolute path to the file including the filename (e.g., on Windows a path might be: "C:\dev\4\ham\0026.2000-01-17.beck.ham.txt").
nbclassify.py  ignores any unknown tokens not seen in training (i.e., pretend they did not occur).

3. Write nbevaluate.py
nbevaluate.py is invoked in the following way:
>python3 nbevaluate.py nboutput_filename
nboutput_filename is the output file of nbclassify.py described above. For each line in the file,
nbevaluate.py will split the line into the guessed label and file path. nbevaluate.py will search for ham or
spam in the path to determine the true label of the example (i.e., “spam” or “ham”). If neither is found,
then it will skip to the next line in the file. Otherwise, the true label will be compared to the guessed
label. 


Similar logic is followed for the Perceptron model as well.
