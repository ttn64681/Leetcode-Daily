
strs=["bdddddddddd","bbbbbbbbbbc"]

hashmap = {}

for x in strs: # iterate each word
    print(x)
    key = [0] * 26
    for c in x: # count each character
        key[ord(c) - ord('a')] += 1 # char - ascii val of 'a' gives difference (c-a = 99-97= 2)
        print(key)

    keyStr = tuple(key) # tuple is immutable and hashable, while lists contain multiple objects
    print(keyStr)

    if keyStr in hashmap: # check if tuple is in hashmap
        hashmap[keyStr].append(x)
    else:
        hashmap[keyStr] = [x]
    print(hashmap)

    print(list(hashmap.values()))