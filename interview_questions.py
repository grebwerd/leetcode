# 5: Calculate the number of vowels and constants in a string
# Steps:
# create counter variables for vowels and constants
# iterate of over string by character and increase the correct counter

# constraints
# 1. Will there be non alphabetical characters and spaces to consider
# 2. Is Y considered a vowel?

# Big 0
# Space is constant because you are always declaring 2 variable regardless of the string size
# Time is the length of the string n

def calcuateVowels(string: str) -> tuple:
    vowel_counter = 0
    constances_counter = 0

    for char in string:
        if char in 'aeiou':
            vowel_counter += 1
        else:
            constances_counter += 1

    return vowel_counter, constances_counter


# 6: check if 2 strings are anagrams
# Steps:
# 1. sort each string
# 2. compare if the strings match

# Constraints
# 1. Does case matter

# Big O
# Space: is constant because you are sorting the string in place
# Time: time is nlogn because the sort method is most likely nlogn

def areAnagrams(string_1: str, string_2: str) -> bool:
    return sorted(string_1) == sorted(string_2)


# recursive
# 1, 1, 2, 3, 5, 8
def fibonacci(n: int) -> int:
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibnoacci_iterative(n: int):
    # 0, 1, 1, 2, 3, 5, 8
    if n <= 0:
        return 0
    if n == 1:
        return 1

    previous = 0
    current = 1

    for index in range(2, n):
        temp = current + previous
        previous = current
        current = temp

    return current


def reverseString(string: str) -> str:
    retval = ""

    for char in string:
        retval = char + retval

    return retval


def reverseStrSlice(string: str) -> str:
    return string[::-1]


def reveserStrList(string: list) -> list:
    string_len = len(string)
    if string_len <= 1:
        return string

    start = 0
    end = string_len - 1
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1

    return string


def fib(n: int) -> list:
    if n == 0:
        return []

    if n == 1:
        return [0]

    # 0,1,1,2,3,5

    prev = 0
    current = 1

    retval = []
    retval.append(0)
    retval.append(1)

    for i in range(2, n):
        new_val = prev + current
        prev = current
        current = new_val
        retval.append(new_val)

    print(f"retval: {retval}")
    return retval


def isPrime(number: int):
    if number <= 1:
        return False
    values = int(number / 2) + 1
    print(f"Values: {values}")
    for i in range(2, values):
        if number % i == 0:
            print(f"number: {number} is a multiple of: {i}")
            return False
    return True


def sieveOfErathothenes(n: int) -> list:
    values = n + 1
    prime = [True for i in range(values)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, values, p):
                prime[i] = False
        p += 1

    retval = []
    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            retval.append(p)
            print(p)

    return retval


def printCharactersInString(string: str) -> dict:
    charCount = {}

    for char in string:
        if char not in charCount.keys():
            charCount[char] = 0
        charCount[char] += 1
        print(f"charCount {charCount[char]}")

    for key in charCount:
        print(f"key: {key}, count: {charCount[key]}")

    return charCount


def isPalindrome(string: str) -> bool:
    return string == string[::-1]


def isAnagram(string_1: str, string_2) -> bool:
    if len(string_1) != len(string_2):
        return False

    return sorted(string_1) == sorted(string_2)


def countCharInWord(string: str) -> dict:
    if len(string) == 0:
        return {}

    charCountDict = {}

    for char in string:
        if charCountDict.get(char):
            charCountDict[char] += 1
        else:
            charCountDict[char] = 1

    return charCountDict

def countVowelsInString(string: str) -> dict:
    if len(string) == 0:
        return {}

    vowels = "aeiou"
    vowelCount = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

    for char in string:
        if char in vowels:
            vowelCount[char] += 1

    return vowelCount


def fizzBuzz(num: int) -> None:
    for n in range(1, num + 1):
        retval = ""
        if n % 3 == 0:
            retval = "Fizz"
        if n % 5 == 0:
            retval += "Buzz"
        elif n % 3 != 0 and n % 5 != 0:
            retval = f"{n}"
        print(f"{n}: {retval}")

def main():
    test = "hello world"
    printCharactersInString(test)
    test_empty = ""
    expect_empty = {}
    test_noncapitalized = "abc"
    expect_noncapitalized = {"a": 1, "b": 1, "c": 1}
    actual_noncapitalized = printCharactersInString("cba")
    assert expect_noncapitalized == actual_noncapitalized, f"expected_noncapitalized: {expect_noncapitalized},actual_noncapitalized: {actual_noncapitalized}"

    test_capitalized = "ABC"
    test_mixture_case_sensive = "aAbBBcCCC"
    test_number = "123"
    test_special_characters = "!@#"
    test_int = 3
    test_none = None

    test_char_count = "abbcccddd"
    print(f" the char count for: {test_char_count} is: {countCharInWord(test_char_count)}")

    test_char_count = "abbcccdddeeeeee"
    print(f" the vowel count for: {test_char_count} is: {countVowelsInString(test_char_count)}")

    test_fizz_buzz = 18

    print(f"FizzBuzz for: {test_fizz_buzz}: {fizzBuzz(test_fizz_buzz)}")



if __name__ == "__main__":
    main()
