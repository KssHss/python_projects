'''Problem Statement and Explanation
Kevin and Stuart have decided to play a game called ‘The Minion Game’. The game has some rules that they both must follow.

Here are the rules:

Both players will receive the exact same string.
Using the letters from the string, both players must create as many substrings as possible.
Stuart can only create words that start with consonants.
Kevin can only create words that start with vowels.
The game ends when both players have created all possible substrings.'''



def minion_game(string): 

    vowels = "AEIOU"

    kevin_score = stuart_score = 0

    length = len(string)
    print(f"length of strig is {length}")

    list_range= list(range(length))
    print(f"length of string is {list_range}")

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score: 
        print(f'Kevin scored {kevin_score}')
    elif stuart_score > kevin_score:
        print(f'Stuart scored {stuart_score}')
    else: 
        print("Tie!!! You can play Again")

if __name__  == '__main__':
    s = input()
    minion_game(s)