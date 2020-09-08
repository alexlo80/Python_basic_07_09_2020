"""6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км."""

user_reply_start = input("Введите расстояние в первый день: ")
if user_reply_start.isdigit():
    user_reply_goal = input("Введите сколько километров хотите бегать: ")
    if user_reply_goal.isdigit():
        km = int(user_reply_start)
        day = 1
        while km < int(user_reply_goal):
            km *= 1.1
            day += 1
        print("Цель будет достигнута на ", day, "-й день")
    else:
        print("insert just numbers!!")
else:
    print("insert just numbers!!")
