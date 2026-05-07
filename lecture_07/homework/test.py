def security_check(func):
    """
    Декоратор для проверки прав доступа (имитация).
    """

    # wrapper принимает любые аргументы (*args, **kwargs)
    def wrapper(*args, **kwargs):
        print("[SECURITY] Проверка прав доступа для пользователя...")
        # Передаем аргументы дальше в оригинальную функцию и ОБЯЗАТЕЛЬНО сохраняем её результат
        result = func(*args, **kwargs)
        # ВОЗВРАТ №1: wrapper возвращает результат в точку вызова
        return result

    # ВОЗВРАТ №2: сам декоратор возвращает функцию wrapper наружу
    return wrapper


@security_check
def get_farmer_payout(farmer_id, period, amount):
    """
    Возвращает сумму выплаты поставщику.
    """
    return f"Выплата поставщику #{farmer_id} за {period}: {amount}$."


# Вызов функции с аргументами
print(get_farmer_payout(105, "01.2026", 2500))
