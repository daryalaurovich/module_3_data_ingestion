def calculate_total_delivery_cost(
    product_name: str,
    weights: list[float] | tuple[float, ...],
    prices: list[float] | tuple[float, ...],
    discount: float | None,
    currency_rate: int | float = 1,
    *extra_costs: float,
) -> dict[str, float]:
    if len(weights) != len(prices):
        raise ValueError("Списки весов и цен должны быть одинаковой длины.")

    base_sum: float = 0.0
    final_sum: float = 0.0
    extra_sum: float = sum(extra_costs)

    for i in range(len(weights)):
        base_sum += weights[i] * prices[i]

    if discount is not None:
        final_sum = base_sum * (1 - discount)
    else:
        final_sum = base_sum

    final_sum = (final_sum + extra_sum) * currency_rate

    return f"Товар: {product_name}, итоговая стоимость: {final_sum} "


veg_data = calculate_total_delivery_cost(
    "Овощная партия", [100, 50], [4, 6], 0.1, 1, 20, 15
)

fruit_data = calculate_total_delivery_cost(
    "Фруктовая партия", (30, 20, 10), (15, 12, 18), None, 1.2, 25
)

print(veg_data)
print(fruit_data)
