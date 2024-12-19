#  "Сложные моменты и исключения в стеке вызовов функции"

def personal_sum(numbers):
    result = 0
    incorrect_data  = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            incorrect_data +=1
            print(f'Некорректный тип данных для подсчета суммы - {i}')
    return result, incorrect_data

def calculate_average(numbers):
    try:
        sum_, incorrect_= personal_sum(numbers)
        average_= sum_ / (len(numbers)- incorrect_)
    except(ZeroDivisionError):
        average_=0
    except(TypeError):
        average_= None
        print('В numbers записан некорректный тип данных')
    return average_

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "строка", 3, "еще строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([1,2,3,4])}')