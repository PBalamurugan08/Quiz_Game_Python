# Mini Quiz game
 
print("Welcome to Cricket Quiz Game")

name=input("Please, Enter your name :")

player=input("Do you want to start the game..?")

if player.lower() == "yes":
    print("Ok Let's play the game..")
    score=0
   
else:
    quit()
    
question=input(" 1. Who is the ICC ODI Cricketer of the Year for 2019 ?")

if question.lower() == "rohit sharma":
    print("Super..! Your answer is correct...")
    score +=1
    
else:
    print("Sorry.! Incorrect answer...")
    
    
question=input(" 2. Which Indian Cricketer became the fastest batsman in the world to reach 20,000 international runs mark ?")

if question.lower() == "virat kohli":
    print("Super..! Your answer is correct...")
    score +=1
    
else:
    print("Sorry.! Incorrect answer...")
    
question=input(" 3. Who amongst the following is the Indian player to make fastest century in the T20 ?")

if question.lower() == "rishabh pant":
    print("Super..! Your answer is correct...")
    score +=1
    
else:
    print("Sorry.! Incorrect answer...")

question=input(" 4. Which cricketer has scored the most centuries in Test cricket ?")

if question.lower() == "sachin tendulkar":
    print("Super..! Your answer is correct...")
    score +=1
    
else:
    print("Sorry.! Incorrect answer...")
    
question=input(" 5. Who holds the record for the fastest century in ODI cricket ?")

if question.lower() == "ab de villiers":
    print("Super..! Your answer is correct...")
    score +=1
    
else:
    print("Sorry.! Incorrect answer...")
        
question=input(" 6. Which cricketer has the most stumpings in international cricket ?")

if question.lower() == "ms dhoni":
    print("Super..! Your answer is correct...")
    score +=1
    
else:
    print("Sorry.! Incorrect answer...")

question=input(" 7. Who was the first cricketer to hit 6 sixes in an over in T20I cricket ?")

if question.lower() == "yuvraj singh":
    print("Super..! Your answer is correct...")
    score +=1
    
else:
    print("Sorry.! Incorrect answer...")

question=input(" 8. Which team won the first T20 World Cup ?")

if question.lower() == "india":
    print("Super..! Your answer is correct...")
    score +=1
    
else:
    print("Sorry.! Incorrect answer...")

question=input(" 9. Which team has won the most fairplay awards in IPL ?")

if question.lower() == "csk":
    print("Super..! Your answer is correct...")
    score +=1
    
else:
    print("Sorry.! Incorrect answer...")
    
print(name,"your score "+ str(score))



