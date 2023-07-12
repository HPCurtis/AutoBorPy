# Create a magic 8 ball function
# Import random function
import random

# Generate getAnswer function
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is Certain'
    elif answerNumber == 2:
        return 'It is decidely so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again Later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook is not so  good'
    elif answerNumber == 9:
        return 'Very doubtful'

# Print magic eight ball outcome
print(getAnswer(random.randint(1,9)))