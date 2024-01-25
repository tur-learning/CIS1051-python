# 9.1
def longWords(fileName):
    words = []

    with open(fileName, "r") as file:
        for line in file:
            words.append(line)

    for i in words:
        if len(i) > 20:
            print(i)

# 9.2
def has_no_e(word):
    if "e" not in word:
        return True

def no_e_total(fileName):
    words = []
    total = 0

    with open(fileName, "r") as file:
        for line in file:
            words.append(line)
            total += 1
    
    count = 0
    for i in words:
        if has_no_e(i):
            print(i)
            count += 1
    
    print("\nPercentage of words with 'e':", round((count/total)*100, 2), "%")

# 9.3
def avoids(word, forbiddenString):
    for i in word:
        if i in forbiddenString:
            return False
        elif i not in forbiddenString and i == word[-1]:
            return True

def forbiddenCheck(fileName):
    forbiddenStringInput = input("Give me a string of forbidden words: ")

    words = []

    with open(fileName, "r") as file:
        for line in file:
            words.append(line)
    
    count = 0
    for i in words:
        if avoids(i, forbiddenStringInput):
            count += 1
    
    print("Number of non-forbidden words:", count)

# 9.4
def uses_only(word, letters):
    for item in word:
        if item not in letters:
            return False
    return True

def uses_only_test(fileName):
    words = []

    with open(fileName, "r") as file:
        for line in file:
            words.append(line.strip())
    
    count = 0
    for i in words:
        if uses_only(i, "acefhlo"):
            print(i)
            count += 1
    
    print("\nNumber of applicable words:", count)
# There are 188 applicable words with acefhlo, so you can make many sentences

# 9.5
def uses_all(word, required):
    return all(letter in word for letter in required)

def uses_all_test(fileName):
    words = []

    with open(fileName, "r") as file:
        for line in file:
            words.append(line.strip())
    
    count = 0
    required_letters = "aeiouy"
    for i in words:
        if uses_all(i, required_letters):
            print(i)
            count += 1
    
    print("\nNumber of applicable words:", count)
# 598 words use all letters "aeiou"
# 42 words use all letters "aeiousy"

# 9.6
def is_abecedarian(word):
    for i in range(1, len(word)):
        if word[i] < word[i-1]:
            # If a letter is not in alphabetical order, return False
            return False
    
    # If all letters are in alphabetical order, return True
    return True

def abecedarian_words(fileName):
    words = []

    with open(fileName, "r") as file:
        for line in file:
            words.append(line.strip())
    
    count = 0
    for i in words:
        if is_abecedarian(i):
            print(i)
            count += 1
    
    print("\nNumber of abecedarian words:", count)
# There are 596 abecedarian words