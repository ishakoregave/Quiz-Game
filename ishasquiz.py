print("Welcome to Isha's general knowledge quiz!")

playing = input("Should we begin playing? ")

if playing.lower() != "yes":
    quit()

print("Let's play then!!")
score = 0

answer = input("Who is the president of the United States? ")
if answer.lower() == "joe biden":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Biggest state in the US? ")
if answer.lower() == "alaska":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Capital of Texas? ")
if answer.lower() == "austin":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")



print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + "%. answers right!")