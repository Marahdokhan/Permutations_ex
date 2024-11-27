#Permutations of a String
#Problem: Write a function to generate all possible permutations of a given string.
#Example Input: permutations("abc")
#Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# first option
def generate_permut(string):
    result = ['']
    for char in string:
        new_result = []
        for change in result:
            for i in range(len(change) + 1):
                new_result.append(change[:i] + char + change[i:])
        result = new_result
    return result

result = generate_permut("abc")
print(result)

# second option
def generate_permutations(s):
    def stepover(start, chars):
        if start == len(chars) - 1:
            result.append("".join(chars))
            return
        for i in range(start, len(chars)):
            chars[start], chars[i] = chars[i], chars[start]
            stepover(start + 1, chars)
            chars[start], chars[i] = chars[i], chars[start]

    result = []
    stepover(0, list(s))
    return result

result = generate_permutations("abc")
print(result)