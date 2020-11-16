sentence = input('Напиши предложение из нескольких слов, разделённых пробелами: ')

sentence = sentence.split()
for i, word in enumerate(sentence, 1):
    if len(word) > 10:
        print(i, word[:10])
        continue
    print(i, word)
