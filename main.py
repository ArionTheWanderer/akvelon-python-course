def my_decorator(func):
    def wrapper(sentence):
        frequency = func(sentence)
        max_frequency = 0
        most_frequent_word = ''
        for key in frequency:
            if frequency[key] > max_frequency:
                max_frequency = frequency[key]
                most_frequent_word = key
        print(f'Most frequent word is "{most_frequent_word}", count = {max_frequency}')
        return frequency
    return wrapper


@my_decorator
def calculate_frequency(sentence):
    words = sentence.split(" ")
    frequency = {}
    for word in words:
        lower_word = word.lower()
        new_word = frequency.get(lower_word)
        if new_word is not None:
            frequency[lower_word] += 1
        else:
            frequency[lower_word] = 1
    return frequency


# Единственное условие - разделитель должен быть пробелом
my_string = "Never gonna give you up Never gonna let you down Never gonna run around never"
word_frequency = calculate_frequency(my_string)
for name in word_frequency:
    print(f'Word = "{name}", count = {word_frequency[name]}')
