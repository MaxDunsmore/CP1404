string = input("Enter a sentence: ")
split_string = string.split()
count_dict = {}
for word in split_string:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

print("Text: {}".format(string))
for word in count_dict:
    print("{} : {}".format(word, count_dict[word]))
