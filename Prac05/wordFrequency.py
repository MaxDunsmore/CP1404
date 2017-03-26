string = input("Enter a sentence: ")
split_string = string.split()
count_dict = {}
for word in split_string:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

count_list = list(count_dict)
count_list.sort()
sorted_length = sorted(count_list, key=len)

print("Text: {}".format(string))
for word in count_list:
    print("{:{}} : {}".format(word, len(sorted_length[-1]), count_dict[word]))
