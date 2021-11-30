print('Вывести последнюю букву в слове')
word = 'Архангельск'
print(word[-1])
print()

print('Вывести количество букв "а" в слове')
word = 'Архангельск'
print(word.lower().count('а'))
print()

print('Вывести количество гласных букв в слове')
word = 'Архангельск'
vowels =set('аеёиоуэюя')
cnt = 0
for letters in word.lower():
    if letters in vowels:
        cnt +=1
print(f'количество гласных букв в слове - {cnt}')
print()

print('Вывести количество слов в предложении')
sentence = 'Мы приехали в гости'
print(len(sentence.strip().split(" ")))
print()

print('Вывести первую букву каждого слова на отдельной строке')
sentence = 'Мы приехали в гости'
for word in sentence.split(" "):
    print(word[0])
print()

print('Вывести усреднённую длину слова в предложении')
sentence = 'Мы приехали в гости'
length_words = [len(word) for word in sentence.lower().split(" ")]
print(int(sum(length_words)/len(length_words)))
print()