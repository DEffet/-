#РЕШЕНИЕ ЗАДАЧИ "Найдите наибольшее и наименьшее пятизначные числа M и m , кратные 7, которые при делении на 2, 3, 4, 5, 6, 13 дают остаток 1. В ответе запишите разность M−m"
# Функция для проверки условий
def satisfies_conditions(n):
    divisors = [2, 3, 4, 5, 6, 13]
    return all(n % d == 1 for d in divisors) and n % 7 == 0

# Найти все подходящие числа
min_value = None
max_value = None

for number in range(10000, 100000):  # Перебор пятизначных чисел
    if satisfies_conditions(number):
        if min_value is None or number < min_value:
            min_value = number
        if max_value is None or number > max_value:
            max_value = number

# Вычислить разность
if min_value is not None and max_value is not None:
    result = max_value - min_value
    print("Разность M - m:", result)
else:
    print("Подходящих чисел не найдено")
