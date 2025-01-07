# iter inbuilt command iter the sequence of string or items in a list till the last element itered when we use next word at the time of print.

abc = ('danny', 'bunny', 'money')

res = iter(abc)

print(next(res))
print(next(res))
print(next(res))

# if we keep printing print(next(res)) on fourth line then, the iteration gets stopped after sequences of elemenst are finnished.
