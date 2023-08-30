# Find Smaller Numbers
# Given the array nums, for each num find out how many numbers in the array are smaller than it. 
# Return the answer in an array.

# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:
# For nums = 8 there exist four smaller numbers than it (1, 2, 2 and 3).
# For nums = 1 does not exist any smaller number than it.
# For nums = 2 there exist one smaller number than it (1).
# For nums = 2 there exist one smaller number than it (1).
# For nums = 3 there exist three smaller numbers than it (1, 2 and 2).

# Example 2:
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3] 

# Example 3:
# Input: nums = [7,7,7,7]
# Output: nums = [0,0,0,0]

#question1
def find_num(arr):
    #this solution is quadratic
    output = []
    for j in arr: #linear
        num = 0
        for i in arr: #linear
            if j > i:
                num += 1 #constant 
        output.append(num)
    return output
print(find_num([7,7,7,7]))

def find_num2(arr):
    #this solution is linear logarethmic 
    d = {}
    for i, n in enumerate(sorted(arr)): #linear
        if n not in d:
            d[n] = i
    return [d[n] for n in arr]
print(find_num2([7,7,7,7]))


#question2
   #This code is T = C S = C
def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2} #T - C  S - C
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]

#One is faster by miliseconds!

def rps(p1, p2):
    #This code is T=C S = C
    if p1 == 'rock' and p2 == 'scissors': # T = C # S = C
        return "Player 1 won!"
    elif p1 == 'scissors' and p2 == 'paper':
        return "Player 1 won!"
    elif p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    elif p1 == p2:
        return 'Draw!'
    else:
        return "Player 2 won!"


#question3
#This problem  T=linear  S=C
def square_sum(numbers):
    sum = 0
    for loop in numbers : # T = linear S = linear  
        loop = loop ** 2 # T = 
        sum = sum + loop
    return sum
#This problem T=linear S = C not really storing anything 

def square_sum(numbers):
    return sum([i * i for i in numbers]) #Linear for loop