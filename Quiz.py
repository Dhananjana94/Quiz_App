print("Welcome to the Quiz")

play = input("Do you want to play(yes/no)? ")

if play.lower() != "yes":
    quit()

print("Let's Play")

score =0

problem = input("What is cpu stand for : ")


#if we use lower() or Upper() method we need to write whole the sentenses either simple or capital
if problem.lower() == "central processing unit":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer")



problem = input("What is GPU stand for : ")

if problem.lower() == "graphics processing unit":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer")



problem = input("What is RAM stand for : ")

if problem.lower() == "random access memory":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer")



problem = input("What could cause a fixed disk error : ")

if problem.lower() == "incorrect cmos settings":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer")


problem = input("Which motherboad form factor use one 20 pin connector : ")

if problem.lower() == "atx":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer")


# Final score
if score >=3:
    print("Your score "+str(score))
    print("Congratulations you have pass the exam!! ")

elif score < 3:
    print("Your score " + str(score))
    print("Let's try again")

