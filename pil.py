import random
s1 = set(random.randint(1, 100) for b in range(10))
s2 = set(int(input('Введите 10 случайных целых чисел в диапозоне от 1 до 100: ')) for i in range(10))
s3 = s1&s2
values = (list(s3))
key = []
for i in range(len(values)):
    key.append(i)
dd = dict(zip(key, values))
print('Словарь: ', dd)