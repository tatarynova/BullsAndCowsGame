
# TEST CASES:
# 1
# Creating data sets for each level of difficulty. Main task is to create 3,4,5-digit numbers, where non of digits are reapeted inside the number itself.
# EASY:
# Should contain 720 possible combinations of 3-digit numbers.
# if difficulty=="easy":
# print(len(get_all_answers_3()))
# NORMAL:
# Should contain 5040 possible combinations of 4-digit numbers.
# elif difficulty=="normal":
# print(len(get_all_answers_4()))
# HARD:
# Should contain 30240 possible combinations of 5-digit numbers.
# elif difficulty=="hard":
# print(len(get_all_answers_5()))
# 2
# ORIGINAL CODE: num_str = ''.join(map(str, enemy_normal))
# PROBLEM: SyntaxError: f-string: unmatched '('
# DEBBUGGING: breaking down the code:
# num_str = ''.join(map(str, enemy_easy))  # First convert to string
# num = int(num_str)  # Then convert to integer
# print(f"The number was: {num}")  # Finally print


# CITATION:
# [1] zfill string method: https://www.w3schools.com/python/ref_string_zfill.asp
# [2] map function: https://www.w3schools.com/python/ref_func_map.asp ; https://youtu.be/8q2vICb89ys?si=r9BgBO-Wenoe0h6p
# [3] enumerate function: https://www.w3schools.com/python/ref_func_enumerate.asp


import random
import time

# NORMAL LEVEL OF DIFFICULTY:
def get_all_answers_4():
    """Creates the list of all the possible answers"""
    ans = []
# Will create 9999 numbers and delete ones that contain reapeted digits inside them.
    for i in range(10000):
        tmp = str(i).zfill(4) #[1]
        if len(set(map(int, tmp))) == 4: # [2]
            ans.append(list(map(int, tmp)))
    return ans

def input_number_normal():
    """Communicates with the user and gets the answer (user's guesses) of 4-digit number.
    Digits inside the number should not repeat themself, otherwise the program will ask for a new guess."""
    while True:
        nums = input('Enter a number with 4 different digits:')
        if len(nums) != 4 or not nums.isdigit():
            print('The number is not valid.')
            continue
        nums = list(map(int, nums)) 
        if len(set(nums)) == 4:
            break
    return nums


# EASY LEVEL OF DIFFICULTY:
def get_all_answers_3():
    """Creates the list of all the possible answers"""
    ans = []
# Will create 999 numbers and delete ones that contain reapeted digits inside them.
    for i in range(1000): 
        tmp = str(i).zfill(3)
        if len(set(map(int, tmp))) == 3:
            ans.append(list(map(int, tmp)))
    return ans

def input_number_easy():
    """Communicates with the user and gets the answer (user's guesses) of 3-digit number.
    Digits inside the number should not repeat themself, otherwise the program will ask for a new guess."""
    while True:
        nums = input('Enter a number with 3 different digits:')
        if len(nums) != 3 or not nums.isdigit():
            print('The number is not valid.')
            continue
        nums = list(map(int, nums)) 
        if len(set(nums)) == 3:
            break
    return nums

# HARD LEVEL OF DIFFICULTY:
def get_all_answers_5():
    """Creates the list of all the possible answers"""
    ans = []
# Will create 99999 numbers and delete ones that contain reapeted digits inside them.
    for i in range(100000):
        tmp = str(i).zfill(5)
        if len(set(map(int, tmp))) == 5:
            ans.append(list(map(int, tmp)))
    return ans

def input_number_hard():
    """Communicates with the user and gets the answer (user's guesses) of 5-digit number.
    Digits inside the number should not repeat themself, otherwise the program will ask for a new guess."""
    while True:
        nums = input('Enter a number with 5 different digits:')
        if len(nums) != 5 or not nums.isdigit():
            print('The number is not valid.')
            continue
        nums = list(map(int, nums)) 
        if len(set(nums)) == 5:
            break
    return nums

# OTHER FUNCTIONS:
def get_one_answer(ans):
    """Chooses one answer from the list of all possibilities created in get_all_answers functions."""
    num = random.choice(ans)
    return num

def check(nums, true_nums):
    """Compares two number and tells the user the amount of bulls and cows they have scored."""
    bulls, cows = 0, 0
    for i, num in enumerate(nums): #[3]
        if num in true_nums:
            if nums[i] == true_nums[i]:
                bulls +=1
            else:
                cows +=1
    return bulls, cows

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
    time.sleep(2)
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

answers_easy = get_all_answers_3()    # all the possible answers for easy level
answers_normal = get_all_answers_4()    # all the possible answers for normal level
answers_hard = get_all_answers_5()  # all the possible answers for hard level
# player = input_number()     #he number guessed by player
enemy_easy = get_one_answer(answers_easy)     # the number randomised by program on easy level
enemy_normal = get_one_answer(answers_normal)   # the number randomised by program on normal level
enemy_hard = get_one_answer(answers_hard)   # the number randomised by program on hard level

# START OF PLAYING:
print("Welcome to the game 'Bulls and Cows'")
time.sleep(1)
user_name=input("Enter your name for personalized experience:")

# displaying of rules (optional)
while True:
    user_experience=input(f"Hello, {user_name}, are you familliar with the rules of 'Bulls and Cows'? Please, answer 'yes' or 'no': ") 
# aim is to make rule explanation optional in case the user has already played this game before
    user_experience=user_experience.lower()
    if user_experience not in ("yes", "no"):
        print("Please, enter 'Yes' or 'No'.")
        continue
    if user_experience=="yes":
        break
    else:
        display_rules()
        break

# difficulty decision-making
while True:
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
        print(f"Great choice, {user_name}! You're playing more complicated persion of classic 'Bulls and Cows'. The secret number will be 5-digits long.")
    time.sleep(1)
    print("Let's get started.")
    time.sleep(1)
    break

# THE GAME ITSELF
score=0
while True:
    if difficulty=="easy":
        print(f"{'='*15}{user_name}'s Turn{'='*15}")
        time.sleep(2)
        print("Guess a number generated by the computer.")
        time.sleep(1)
        number = input_number_easy()
        bulls, cows = check(number, enemy_easy)
# printing score table
        if bulls!=0:
            score+=2
        elif cows!=0:
            score+=1
        print(f"Good guess, {user_name}! Your score is shown bellow:")
        print("+-------+-----+------+")
        print("| Guess |Bulls| Cows |")
        print("+-------+-----+------+")
        print(f"|  {int(''.join(map(str, number)))}  |  {bulls}  |   {cows}  |")
        print("+-------+-----+------+")
        if bulls==3:
            print('You won!')
# TEST-CASE #2
# print(f"The number was: {int(''.join(map(str, enemy_easy)))}")
            num_str = ''.join(map(str, enemy_easy))
            num = int(num_str)
            print(f"The number was: {num}")
            print(f'Your score is: {score}.')
            break
    if difficulty=="normal":
        print(f"{'='*15}{user_name}'s Turn{'='*15}")
        time.sleep(2)
        print("Guess a number generated by the computer.")
        time.sleep(1)
        number = input_number_normal()
        bulls, cows = check(number, enemy_normal)
# print(f"Good guess, {user_name}! You have {bulls} bulls and {cows} cows.")
# printing score table
        if bulls!=0:
            score+=2
        elif cows!=0:
            score+=1
        print(f"Good guess, {user_name}! Your score is shown bellow:")
        print("+-------+-----+------+")
        print("| Guess |Bulls| Cows |")
        print("+-------+-----+------+")
        print(f"|  {int(''.join(map(str, number)))} |  {bulls}  |   {cows}  |")
        print("+-------+-----+------+")
        if bulls==4:
            print('You won!')
# TEST-CASE #2:
# print(f'The number was: {int(''.join(map(str, enemy_normal)))}') 
            num_str = ''.join(map(str, enemy_normal))
            num = int(num_str)
            print(f"The number was: {num}") 
            print(f'Your score is: {score}.')
            break
    if difficulty=="hard":
        print(f"{'='*15}{user_name}'s Turn{'='*15}")
        time.sleep(2)
        print("Guess a number generated by the computer.")
        time.sleep(1)
        number = input_number_hard()
        bulls, cows = check(number, enemy_hard)
# print(f"Good guess, {user_name}! You have {bulls} bulls and {cows} cows.")
# printing score table
        if bulls!=0:
            score+=2
        elif cows!=0:
            score+=1
        print(f"Good guess, {user_name}! Your score is shown bellow:")
        print("+-------+-----+------+")
        print("| Guess |Bulls| Cows |")
        print("+-------+-----+------+")
        print(f"| {int(''.join(map(str, number)))} |  {bulls}  |   {cows}  |")
        print("+-------+-----+------+")
        if bulls==5:
            print('You won!')
# TEST-CASE #2
# print(f'The number was: {int(''.join(map(str, enemy_hard)))}')
            num_str = ''.join(map(str, enemy_hard))
            num = int(num_str)
            print(f"The number was: {num}")
            print(f'Your score is: {score}.')
            break