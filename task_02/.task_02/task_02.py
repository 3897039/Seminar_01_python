# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

print('Введите общее количество журавликов')
SumAll = int(input())
SumPeter = 0
SumSerg = 0
SumKate = 0
SumKate = (SumAll//6)*4
SumSerg = SumAll//6
SumPeter = SumSerg
print(SumPeter)
print(SumKate)
print(SumSerg)
