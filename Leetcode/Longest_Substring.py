def longest_substring(i_string):
    length = len(i_string)
    word = ""
    checker = ""
    last_seen = {}
    x = 0
    start = 0
    while x < length:

        element = i_string[x]

        if element in last_seen and last_seen[element] >= start:
            start = last_seen[element] + 1
        word = i_string[start:x + 1]
        if len(word) > len(checker):
            checker = word
        last_seen[element] = x
        x += 1

    return len(checker)

print(longest_substring("dvdf"))
    
