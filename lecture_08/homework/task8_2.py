branches = [
    {"city": "Minsk", "revenue": 15000},
    {"city": "Warsaw", "revenue": 32000},
    {"city": "London", "revenue": 12000},
]


def audit_logger(func):
    def wrapper(*args, **kwargs):
        print("[AUDIT] Запуск анализа...")
        result = func(*args, **kwargs)
        print("[AUDIT] Анализ завершен.")
        return result

    return wrapper


@audit_logger
def get_sorted_report(branches):
    sorted_branches = sorted(
        branches, key=lambda branch: branch["revenue"], reverse=True
    )
    return sorted_branches


branches_sorted_list = get_sorted_report(branches)
print(branches_sorted_list)
print("Топ филиалов:")
for i, branch in enumerate(branches_sorted_list):
    print(f"{i + 1}. {branch['city']}: {branch['revenue']}")
