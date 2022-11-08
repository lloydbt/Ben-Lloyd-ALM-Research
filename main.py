verbsSet = open("LibraryOfVerbs_V1.txt")

verbs = {}

for line in verbsSet:
  verbs.update({line.strip(): 0})


inputSet = open("ROCStories__spring2016 - ROCStories_spring2016.csv")

verbCount = 0

line = inputSet.readline()
for line in inputSet:
  story = line.split(",")
  for i in range(2,6):
    sentence = story[i].split(" ")
    for j in range(len(sentence)):
      if sentence[j].strip().lower() in verbs:
        verbs[sentence[j].strip().lower()] += 1
        verbCount += 1


for verb in verbs:
  print("" + verb + " " + str(verbs[verb]))