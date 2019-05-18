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
index = 0
sentenceId = '0'
wordNum = 0
sentiment = 0.0
phraseNum = 0
phraseSentiment = 0.0
sentenceSentiment = []

f = open('testphrase.txt', 'r') 
for line in f.readlines():
    words = line.split(' ')
    for i in range(len(words)):
        word = words[i]
        if i == 0:
            if word != sentenceId:
                sentenceId = word
                if phraseNum != 0:
                    sentenceSentiment.append(phraseSentiment / phraseNum)
                    phraseNum = 0
                    phraseSentiment = 0.0
        else:
            if word in vocabulary:
                wordNum += 1
                sentiment += grade[vocabulary.index(word)]
    if wordNum != 0:
        phraseSentiment += (sentiment / wordNum)
    phraseNum += 1
    sentiment = 0.0
    wordNum = 0
if phraseNum != 0:
    sentenceSentiment.append(phraseSentiment / phraseNum)
f = open('test.txt', 'r') 
for line in f.readlines():
    sentence = line.split(' ')
    if round(sentenceSentiment[index]) == int(sentence[1]) >= 0:
        correct += 1
    index += 1
print("accuracy: ", correct / index)
f.close()
