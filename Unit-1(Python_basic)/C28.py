import os;os.system('cls')
# """
# number paladrome
# """
# def pal():
#     ls =[121,234,252]
#     for i in ls :
#         a = str(i)
#         if a==a[::-1]:
#             print("paladrome")
#         else:
#             print("not paladrome")
            
# pal()
"""
counting vowel
"""
def vowel():
    ls1 ="aeiouAEIOU"
    word = "sophisticated"
    vowel_count =0
    consonant_count= 0
    for i in word:
        if i.isalpha():
            if i in ls1:
                vowel_count+=1
            else:
                consonant_count+=1
                
    
    print(vowel_count)
    print(consonant_count)

print(vowel())