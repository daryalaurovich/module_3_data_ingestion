SMALL_BATCH_LIMIT = 500


def calculate_batch(weight, price, discount=0.0):
    final_sum = weight * price * (1 - discount)
    is_limit_exceeded = final_sum > SMALL_BATCH_LIMIT
    return final_sum, is_limit_exceeded


print(calculate_batch(100, 4))

total_sum_carrot, is_limit_exceeded_carrot = calculate_batch(100, 4)
print(
    f"Партия 1 (Морковь): Сумма {total_sum_carrot}. Превышение лимита: {is_limit_exceeded_carrot}"
)

total_sum_apple, is_limit_exceeded_apple = calculate_batch(50, 20, 0.1)
print(
    f"Партия 2 (Яблоки): Сумма {total_sum_apple}. Превышение лимита: {is_limit_exceeded_apple}"
)
