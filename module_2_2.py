programm = input( 'Введите три целых числа:')
first = int(programm[0:4])
second = int(programm[4:7])
third = int(programm[8:12])
set = first, second, third
print(set)
if first == second == second == third:
    print(3)
elif first == second:
    print(2)
elif third == first:
    print(2)
elif second == third:
    print(2)
else:
    print(0)


