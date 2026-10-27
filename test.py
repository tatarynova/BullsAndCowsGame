# def get_all_answers_4():
#     """Creates the list of all the possible answers"""
#     ans = []
#     # Will create 9999 numbers and delete ones that contain reapeted digits inside them.
#     for i in range(10000):
#         tmp = str(i).zfill(4) #[1]
#         if len(set(map(int, tmp))) == 4: # [2]
#             ans.append(list(map(int, tmp)))
#     return ans
#
# ans=[]
# for i in range(10000):
#     tmp = str(i).zfill(4)  # [1]
#     # if len(set(map(int, tmp))) == 4:  # [2]
#     #     ans.append(list(map(int, tmp)))
# print(set(map(int, tmp)))
# # print(ans)

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