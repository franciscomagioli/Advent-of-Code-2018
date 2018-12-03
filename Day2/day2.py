import time
start_time = time.time()

# part 1 - didnt try in read//counter creation to try to reuse the structures in day2(blindly)
from collections import Counter

inputList = []
with open(r'C:\Users\franc\Desktop\Advent of Code\Day2\day2.txt') as inputs:
    for line in inputs:
        inputList.append(line.rstrip())

counterList = []
for inp in inputList:
    counterList.append(Counter(inp))

counter_2 = 0
counter_3 = 0
for counterTest in counterList:
    if(2 in counterTest.values()):
        counter_2 += 1
    if(3 in counterTest.values()):
        counter_3 += 1
print("Counter 2: " + str(counter_2))
print("Counter 3: " + str(counter_3))
print("Result: "+str(counter_2*counter_3))

# day 2 - Levenshtein distance = 1
# 250 strings
# 249+248+247...+2+1 string comparisons (if it doesnt stop when it finds the distance as 1)
# 250*125 = 31250 comparisons

def compareStrings(a,b):
    levDist = 0
    for i in range(len(a)):
        if(a[i] != b[i]):
            levDist+=1
    return levDist

def findDistEqual1(inputList):
    for i in range(249):
        for j in range(i,250):
            if(compareStrings(inputList[i],inputList[j]) ==1):
                return inputList[i],inputList[j]

def buildAnswerString(a,b):
    newString = ""
    for i in range(len(a)):
        if(a[i] == b[i]):
            newString += a[i]
    return newString

string1, string2 = findDistEqual1(inputList)
newString = buildAnswerString(string1,string2)
print(newString)
print("--- %s seconds ---" % (time.time() - start_time))
