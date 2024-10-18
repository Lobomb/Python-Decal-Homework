#Homework 3
#1 Oski Stole Your Power
def computepower(x,y):
    result = 1
    for _ in range(y):
        result *= x
    return  result
x = 2
y = 3
print(computepower(x,y))

#3 Check if its the Weekend
def isWeekend(day):
    return day == 6 or day == 7

#4 Fuel Efficiency Calculator
def fuel_efficiency(distance, fuel):
    return distance / fuel

#6 Min and Max But With Loops!
def find_min_with_for_loop(nums):
    min_value = nums[0]
    for num in nums:
        if num < min_value:
            min_value = num
    return min_value

def find_max_with_for_loops(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value

#7 Counting Vowels
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    return (num_vowels, num_consonants)

#8 Calculate Digital Root
def digital_root(num):
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num //= 10
    return sum_digits