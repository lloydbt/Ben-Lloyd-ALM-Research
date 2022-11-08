# Number of sentences that AT LEAST must have a match
sentenceSensitivity = 1; 
# Number of verbs that AT LEAST must match
verbSensitivity = 3; 
# Limit to number of stories to be output
outputLimit = 2500000;
# Input file for set of verbs
verbsSet = open("LibraryOfVerbs_V3.txt")
# Input file for dataset
inputSet = open("ROCStories__spring2016.tsv")

# Store verbs from file
verbs = []
# Store stories from dataset
stories = []

# Read in the verbs from file
for line in verbsSet:
  if(line[0] == ' '):
    continue
  else:
    verbs.append(line.strip())
verbsSet.close()

# Get rid of formatting first line
line = inputSet.readline()

# Parse dataset
for line in inputSet:
  # Ensure that the outputLimit has not been reached
  if (len(stories) == outputLimit):
    break

  # Split the story into a sentences in a list
  story = line.split("\t")

  # Variable used to track number of setences 
  sentenceCount = 0

  # Parse the sentences of the story
  for i in range(2,6):
    # Check if the sentenceSensitivity is met yet
    if (sentenceCount == sentenceSensitivity):
      # Add the Title and sentences to output list
      stories.append(story[1:7])
      break
    
    # Split the sentence up into words in a list
    sentence = story[i].split(" ")

    # Variable to track number of matching verbs found
    verbCount = 0

    # Parse the words of the sentence
    for j in range(len(sentence)):
      # Check if the word matches a desired verb
      if sentence[j] in verbs:
        verbCount += 1
    
    # If the verbCount is AT LEAST the verbSensitivity, up the sentenceCount
    if (verbCount >= verbSensitivity):
      sentenceCount += 1
inputSet.close()

# Parse the output list and print to file in title-paragraph format
with open("Stories_of_50_verbs_conjugated.txt", "w") as output:
  print(len(stories), file=output)
  for i in range(0,len(stories)):
    print(stories[i][0], file=output)
    print(stories[i][1] + " " + stories[i][2] + " " + stories[i][3] + " " + stories[i][4] + " " + stories[i][5], file=output)
