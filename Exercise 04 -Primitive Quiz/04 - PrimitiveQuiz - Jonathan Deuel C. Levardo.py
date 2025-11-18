score = (0)
print("Do you know them all?")

#Paris, France
question_France = input("Capital of France? ")
if question_France.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#London, UK
question_UK = input("Capital of the UK? ")
if question_UK.lower() == "london":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Moscow, Russia
question_Russia = input("Capital of Russia? ")
if question_Russia.lower() == "moscow":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Rome, Italy
question_Italy = input("Capital of Italy? ")
if question_Italy.lower() == "rome":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Madrid, Spain
question_Spain = input("Capital of Spain? ")
if question_Spain.lower() == "madrid":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Athens, Greece
question_Greece = input("Capital of Greece? ")
if question_Greece.lower() == "athens":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Berlin, Germany
question_Germany = input("Capital of Germany? ")
if question_Germany.lower() == "berlin":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Kiev, Ukraine
question_Ukraine = input("Capital of Ukraine? ")
if question_Ukraine.lower() == "kiev":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Helsinki, Finland
question_Finland = input("Capital of Finland? ")
if question_Finland.lower() == "helsinki":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Zagreb, Croatia
question_Croatia = input("Capital of Croatia? ")
if question_Croatia.lower() == "zagreb":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#Results
if score < 10:
    print(f"You got {score} out of 10 of them correct. Try again!")
else:
    print(f"You got {score} out of 10 of them correct. Awesome! Congratulations!")
