import time
start_time = time.time()
#part 1
total = 0
with open(r'C:\Users\franc\Desktop\Advent of Code\Day1\day1.txt') as inputs:
    for line in inputs:
        total += int(line)
print(total)
part1time = time.time() - start_time

#part 2 fixed
start_time = time.time()
inputList = []
with open(r'C:\Users\franc\Desktop\Advent of Code\Day1\day1.txt') as inputs:
    for line in inputs:
        inputList.append(int(line))

freqRN = 0
freqSet = {0}
notFound = True
while(notFound):
    for i in inputList:
        freqRN+=i 
        if(freqRN in freqSet):
            notFound = False
            break
        else:
            freqSet.add(freqRN)
print(freqRN)
part2time = time.time() - start_time

print("Timetable")
print("Part 1: " + str(part1time) + "\nPart 2: "+ str(part2time))