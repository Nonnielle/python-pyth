 #STR
text=("learning python basics")
title=text.title()
index=len(text.split())
reverse= text[::-1]
replace= text.replace("a" ,"@")
print (index) 
print (title)
print (reverse)
print (replace)





#NUM
import random
guess_number = random.randint(1,100)
attempts = 7
for attempt in range (1, attempts + 1):
    guess =int(input(f"Attempt {attempt}/{attempts}: Enter your guess ( 1- 100):"))
    if guess < guess_number:
        print ("Too low!  Try again later")
    elif guess > guess_number:
        print ("Too high! Try again.")
    else:
        print (f"Congratulations! You guessed the correct number {guess_number} in {attempts} attempts.")
        break
else:
    print (f"Sorry you've used all {attempts} attempts. the correct answer was  {guess_number}")






#LIST
my_number= [1,2,3,5,4,7,6,8,2,2]
my_number.sort()
my_number= sorted(set(my_number))
evn= [num for num in my_number if num % 2 == 0]
evn=(sum(evn))
max= (max(my_number))
min= (min(my_number))
print(my_number)
print(evn)
print(max)
print(min)


#Dict
text= "hello world hello python world"
text= text.split()
text_count ={}
for word in text:
    if word in text_count:
        text_count[word]+=1
    else:
        text_count[word]=1
print ("Word Occurance")
for word, count in text_count.items():
    print (f"{word}: {count}")



    #Fibonacci
def fibonacci(n):
        """Return the nth Fibonacci number using recursion"""
        if n == 0:
             return 0
        elif n == 1:
             return 1
        else:
             return fibonacci (n - 1) + fibonacci (n - 2)
    
        
def print_fib_scq(terms):
        """Print Fibonacci sequence up to n terms using recursion."""
        scq = [fibonacci(i) for i in range(terms)]
        print(",".join(map(str,scq)))
print_fib_scq(6)



            #File Handling
name = input("Enter your name;")
age = input("Enter your age:")
with open("user_data.txt", "w") as file:
           file.write(f"{name}, Age:{age}")
print("Data saved successfully!")
print("\nReading File...")
with open("user_data.txt","r") as file:
      content = file.read()
      print(content)     


import random
def play_game():
    choices = ["rock","paper","scissors"]
    user_choice = input("Enter your choice( rock,paper"
    ",scissors):").strip().lower()
    if  user_choice not in choices:
        print("Invalid choice! Please choose rock,paper,scissors.")
        return
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}") 
    if user_choice == computer_choice:
            print("It's a tie!")
    elif(user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock" ) or \
            (user_choice == "scissors" and computer_choice == "paper"):
            print("You Win!")
    else:
            print("Computer wins!")
    
play_game()


    #Palindrome checker
def text(word):
      """Check if a word is a palindrome."""
      word= word.lower()
      return word == word[::-1]
print(text("mum"
))

print(text("come"))



   #Prime
def prime(n):
      """Check if a number is prime."""
      if n< 2 :
            return False
      for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                  return False
            return True
print("* Prime")      
print(prime(9))
print(prime(12))


     #Leap year
def leap_year(year):
      """Check if a given year is a leap year."""
      if(year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
            return True
      return False 
print('* Leap year')
print(leap_year(2024))




     # Tic-Tac-Toe

def print_board(board):
    """Print the current Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Check if the given player has won the game."""
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Check if the board is full (tie)."""
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0  

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}, enter your move (row and column: 1-3 1-3):")
        
        try:
            row, col = map(int, input().split())
            row, col = row - 1, col - 1  

            if board[row][col] != " ":
                print("Cell already taken! Choose a different move.")
                continue

            board[row][col] = player  

            if check_winner(board, player):
                print_board(board)
                print(f" Player {player} wins! ")
                break
            elif is_full(board):
                print_board(board)
                print("It's a tie!")
                break

            turn += 1  

        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as two numbers between 1 and 3.")

tic_tac_toe()




        
            
 
