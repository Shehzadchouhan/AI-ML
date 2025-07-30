def rem(l,word):
    n=[ ] #empty list to store the result
    for item in l: #irwe through the list
        if not(item == word):# if the item is not equal to the word
            n.append(item.strip(word)) # append the item to the result list
    return n

l=["apple", "banana", "cherry", "apple", "date","an"]
print(rem(l,"an"))

