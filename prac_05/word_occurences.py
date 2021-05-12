word_count = {}
input_text = input("Text: ")
input_text = input_text.split(' ')
word_list = []
word_length = 0
for word in input_text:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
        word_list.append(word)
        if len(word) > word_length:
            word_length = len(word)
word_list.sort()

for word in word_list:
    print('{:{}}: {}'.format(word,word_length,word_count[word]))
