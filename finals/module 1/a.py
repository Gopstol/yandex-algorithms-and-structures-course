def main(n, town) -> str:
    nulls: list = []
    antwort: list = []

    # Находим индексы всех нулей
    for i in range(n):
        if town[i] == 0:
            nulls.append(i)

    # Находим расстояния домов до первого нуля
    for i in range(0, nulls[0]):
        antwort.append(nulls[0] - i)

    # Находим расстояния до остальных нулей
    for i in range(1, len(nulls)):
        antwort.append(0)
        diameter = nulls[i] - nulls[i - 1] - 1
        radius = diameter // 2
        radius_str: list = []
        for j in range(radius):
            radius_str.append(j + 1)

        antwort += radius_str
        if diameter % 2 == 1:
            antwort.append(radius + 1)
        antwort += radius_str[::-1]

    antwort.append(0)

    # Если после последнего нуля есть ещё дома, находим их
    if n != nulls[-1]:
        diameter = n - nulls[-1] - 1
        for i in range(diameter):
            antwort.append(i + 1)

    return " ".join(list(map(str, antwort)))


if __name__ == "__main__":
    num = int(input())
    town_arr = list(map(int, input().split()))

    print(main(num, town_arr))

