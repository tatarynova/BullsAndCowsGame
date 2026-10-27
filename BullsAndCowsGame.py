import random
import time

#FUNCTIONS
#LEVEL DICTIONARY
levels_dict = {"easy": 3, "normal": 4, "hard": 5}

#ANSWER GENERATORS:
def get_computers_answer(digits):
    """Creates the list of all the possible answers depending on a difficulty level chosen
    Easy == 720 unique combinations
    Normal == 5040 unique combinations
    Hard == 30240 unique combinations"""
    ans = []
    for i in range(10**digits):
        tmp = str(i).zfill(digits)
        if len(set(map(int, tmp))) == digits:
            ans.append(list(map(int, tmp)))
    random_num = random.choice(ans)
    return random_num

#TAKE AND CHECK USER'S GUESSES
def input_number(digits):
    """Communicates with the user and gets the answer (user's guesses).
    Digits inside the number should not repeat themselves, otherwise the program will ask for a new guess."""
    while True:
        nums = input(f"Enter a number with {digits} different digits:")
        if len(nums) != digits or not all(c in "0123456789" for c in nums):
            print('The number is not valid.')
            continue
        nums = list(map(int, nums)) 
        if len(set(nums)) == digits:
            break
    return nums

def check(nums, true_nums):
    """Compares two number and return the amount of bulls and cows the user have scored."""
    bulls, cows = 0, 0
    for i, num in enumerate(nums): #[3]
        if num in true_nums:
            if num == true_nums[i]:
                bulls +=1
            else:
                cows +=1
    return bulls, cows

def print_scoring(bulls, cows, digits, score):
    """Takes the amount of bulls and cows
    Returns: the game status (won either true or false), a table with amount of bulls and cows overall"""
    is_won = False
    if bulls == digits:
        is_won = True
        print('You won!')
        print(f"The number was: {''.join(map(str, computer_number))}")
        print(f"Your score is: {score}")
    print(f"Good guess, {user_name}! Your score is shown bellow:")
    print("+-------+-----+------+")
    print("| Guess |Bulls| Cows |")
    print("+-------+-----+------+")
    print(f"|  {''.join(map(str, number))}  |  {bulls}  |   {cows}  |")
    print("+-------+-----+------+")
    return is_won

# THIS IS NOT USED FOR MOW
def del_bad_answers(ans, enemy_try, bull, cow):
    """Deletes all the wrong answers from the list of all possible ones."""
    for num in ans[:]:
        temp_bull, temp_cow = check(num, enemy_try)
        if temp_bull != bull or temp_cow != cow:
            ans.remove(num)
    return ans

def display_rules():
    """Optional function that displays the rules of the game."""
    print('='*11, "Bulls and Cows: Rules", '='*11)
    time.sleep(1)
    print("Your task is to guess the secret number with UNIQUE digits.")
    time.sleep(1)
    print("After each guess, you'll get:")
    time.sleep(1)
    print("- 🐂 Bull = score +2. Corresponds to correct digit in the correct place.")
    print("- 🐄 Cow = score +1. Corresponds to correct digit but wrong place.")
    time.sleep(1)
    print('='*13, "Difficulty Levels:", '='*12)
    print('+', '-'*10, '+', '-'*58, '+' )
    print('|', ' ', "Level", ' '*2, '|' " Description", ' '*46, '|')
    print('+', '-'*10, '+', '-'*58, '+' )
    print('|', ' '*2, "Easy", ' '*2, '|' " The number you need to guess contains 3 UNIQUE digits.", ' '*3, '|')
    print('+', '-'*10, '+', '-'*58, '+' )
    print('|', ' ', "Normal", ' ', '|', "The number you need to guess contains 4 UNIQUE digits.", ' '*3, '|')
    print('+', '-'*10, '+', '-'*58, '+' )
    print('|', ' '*2, "Hard", ' '*2, '|', "The number you need to guess contains 5 UNIQUE digits.", ' '*3, '|')
    print('+', '-'*10, '+', '-'*58, '+' )

def display_levels():
    """Displays levels of difficulty in order to help user choose one"""
    print('='*13, "Difficulty Levels:", '='*12)
    print('+', '-'*10, '+', '-'*58, '+' )
    print('|', ' ', "Level", ' '*2, '|' " Description", ' '*46, '|')
    print('+', '-'*10, '+', '-'*58, '+' )
    print('|', ' '*2, "Easy", ' '*2, '|' " The number you need to guess contains 3 UNIQUE digits.", ' '*3, '|')
    print('+', '-'*10, '+', '-'*58, '+' )
    print('|', ' ', "Normal", ' ', '|', "The number you need to guess contains 4 UNIQUE digits.", ' '*3, '|')
    print('+', '-'*10, '+', '-'*58, '+' )
    print('|', ' '*2, "Hard", ' '*2, '|', "The number you need to guess contains 5 UNIQUE digits.", ' '*3, '|')
    print('+', '-'*10, '+', '-'*58, '+' )


# START OF PLAYING:
print("Welcome to the game 'Bulls and Cows'!")
time.sleep(1)
user_name=input("Enter your name for personalized experience: \n")
user_name = user_name.title()

# displaying of rules (optional)
while True:
    user_experience=input(f"Hello, {user_name}, are you familiar with the rules of 'Bulls and Cows'? Please, answer 'yes' or 'no': \n")
# aim is to make rule explanation optional in case the user has already played this game before
    user_experience = user_experience.lower()
    if user_experience not in ("yes", "no"):
        print("Please, enter 'Yes' or 'No'.")
        continue
    if user_experience=="yes":
        break
    else:
        display_rules()
        break

# difficulty decision-making
display_levels()
time.sleep(1)
difficulty = input(f"Enter the difficulty level you fancy to play: ")
difficulty = difficulty.lower()
while difficulty.lower()!='easy' and difficulty.lower()!='normal' and difficulty.lower()!='hard':
    print("Invalid option.")
    difficulty = input(f"Enter the difficulty level you fancy to play: ")
    difficulty = difficulty.lower()
if difficulty=="easy":
    print(f"Great choice, {user_name}! You're playing simplified version of 'Bulls and Cows'. The secret number will be 3-digits    long.")
elif difficulty=="normal":
    print(f"Great choice, {user_name}! You're playing the classical version of 'Bulls and Cows'. The secret number will be 4-digits long.")
elif difficulty=="hard":
    print(f"Great choice, {user_name}! You're playing more complicated version of classic 'Bulls and Cows'. The secret number will be 5-digits long.")
time.sleep(1)
print("Let's get started.")
time.sleep(1)

# THE GAME ITSELF
computer_number = get_computers_answer(levels_dict[difficulty])
score = 0
while True:
    user_name = user_name.title()
    print(f"{'=' * 20}{user_name}'s Turn{'=' * 20}")
    print("Guess a number generated by the computer!")
    number = input_number(levels_dict[difficulty])
    bulls, cows = check(number, computer_number)
    score += bulls*2 + cows
    result=print_scoring(bulls, cows, levels_dict[difficulty], score)
    if result is True:
        break