def calculate_purchase(product_name, weight, price):
    try:
        numeric_weight = float(weight)
        total_cost = numeric_weight * price
        technical_index = 100 / numeric_weight
        print(f'Товар: {product_name}. Итоговая стоимость: {total_cost}$')
    except ValueError as e:
        print(f"Тип ошибки: {type(e)}")
        print(f"Сообщение: {e}")
    except ZeroDivisionError as e:
        print(f"Тип ошибки: {type(e)}")
        print(f"Сообщение: {e}")
    except TypeError as e:
        print(f"Тип ошибки: {type(e)}")
        print(f"Сообщение: {e}")   
    finally:
        print("--- Проверка партии завершена ---")

# 1. Корректные данные
calculate_purchase("Томаты", 100, 2.5)

# 2. Ошибка значения веса (строка вместо числа)
calculate_purchase("Огурцы", "пятьдесят", 1.8)

# 3. Ошибка деления на 0 (нулевой вес)
calculate_purchase("Перец", 0, 4)

# 4. Ошибка типа данных (список вместо числа)
calculate_purchase("Зелень", [10], 5)
