#1
def myfunction(start=0 , length=10):
    for i in range(start,length):
        print (f"{i+1}")
myfunction()

#2
def function2(num):
    x=num%3
    y=num%5
    if x==0 and y==0 :
        print("fuzzBuzz")
    elif y==0 :
        print("fuzz")
    elif x==0 :
        print("buzz")


function2(15)
#3
def function3(name):
    print(name[::-1])

function3("amira")


#4
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def get_nonempty_name():
    while True:
        name = input("Enter your name: ").strip()
        if name and not name.isdigit():
            return name
        else:
            print("Invalid input. Please enter a non-empty name that is not a number.")

def get_email():
    email = input("Enter your email: ").strip()
    return email
name = get_nonempty_name()
email = get_email()

print("\n--- User Information ---")
print(f"Name: {name}")
print(f"Email: {email}")
if is_valid_email(email):
    print("Email is valid.")
else:
    print("Email is invalid.")


#5
def longest_alphabetical_substring(s):
    longest = ""
    current = ""

    for i in range(len(s)):
        if i == 0 or s[i] >= s[i - 1]:
            current += s[i]
        else:
            current = s[i]
        if len(current) > len(longest):
            longest = current
    print("Longest substring in alphabetical order is:", longest)
longest_alphabetical_substring("abdulrahman")

#6
total = 0
count = 0

while True:
    user_input = input("Enter a number (or 'done' to finish): ")

    if user_input.lower() == "done":
        break

    try:
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Error: Please enter a valid number!")

if count > 0:
    average = total / count
    print(f"total: {total}")
    print(f"Count: {count}")
    print(f"Average: {average}")
else:
    print("No numbers were entered.")

#7
import random

word_list = ['python', 'hangman', 'programming', 'developer', 'keyboard', 'laptop']

chosen_word = random.choice(word_list)
guessed_letters = []
turns = 7

player_name = input("Welcome! What's your name? ")
print(f"Hello {player_name}! Let's play Hangman 😄\n")

while turns > 0:
    display_word = ''
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '_'

    print("Word: " + ' '.join(display_word))

    if '_' not in display_word:
        print(" Congrats! You guessed the word correctly!")
        break

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter. Try another one!")
        continue

    guessed_letters.append(guess)

    if guess not in chosen_word:
        turns -= 1
        print(f"❌ Wrong guess! You have {turns} turn(s) left.")
        if turns == 0:
            print("Game Over! You ran out of turns.")
            print(f"The word was: {chosen_word}")
