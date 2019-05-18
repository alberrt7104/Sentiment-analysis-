import csv
import copy
import math

stoplist = []
trainlabel = []
vocabulary = []
grade = []
num = []

print("================================================================================")
print("preprocessing...")
#preprocessing
f = open('stoplist.txt', 'r') #stoplist
for line in f.readlines():
    stoplist.append(line.strip().upper())    
f.close()

print("training...")
f = open('train.txt', 'r') #training
for line in f.readlines(): # for each sentence
    words = line.split(' ')
    trainlabel.append(copy.deepcopy(int(words[1])))
    for i in range(len(words)):
        word = words[i].strip()
        if i > 1:
            if (word not in stoplist) and (word not in vocabulary) and (word != ''):
                vocabulary.append(word)
vocabulary.sort()
for i in range(len(vocabulary)):
    grade.append(0.0)
    num.append(0)
f.close()
f = open('train.txt', 'r')
temp = 1
for line in f.readlines():
    words = line.split(' ')
    for i in range(len(words)):
        word = words[i].strip()
        if i == 0:
            temp = int(word)
        elif i != 1:
            if word in vocabulary:
                grade[vocabulary.index(word)] += trainlabel[temp - 1]
                num[vocabulary.index(word)] += 1
f.close()
for i in range(len(grade)):
    grade[i] = grade[i] / num[i]
    
print("testing...")
#test 
correct = 0
total = 0
sign1 = 0
p = 0
f = open('test.txt', 'r')
for line in f.readlines(): # for each sentence
    sign1 = 0
    sentiment = 0.0
    words = line.split(' ')
    p = words[1]
    for i in range(len(words)):
        word = words[i].strip()
        if i > 1:
            if word in vocabulary:
                sentiment += grade[vocabulary.index(word)]
                sign1 += 1
    if sign1 > 0:
        sentiment = sentiment / sign1
    if round(sentiment) == int(p):
        correct += 1
    total += 1
print("accuracy: ", correct / total)
f.close()
