def main():
    a = input().split()
    stack: list = []  # стек, хранящий числа
    result: int = 0   # в этой переменной будет храниться результат операций
    for symbol in a:
        if symbol.lstrip("-").isdigit():  # данная инструкция выполняется для цифр
            stack.append(int(symbol))

        else:   # а эта инструкция выполняется для знаков операций
            if symbol == "*":
                result = stack[-2] * stack[-1]    # здесь и далее проводятся операции для последних двух чисел стека
            elif symbol == "/":
                result = stack[-2] // stack[-1]
            elif symbol == "+":
                result = stack[-2] + stack[-1]
            else:
                result = stack[-2] - stack[-1]

            stack.pop()
            stack.pop()
            stack.append(result)

    print(stack[-1])  # выводим последний элемент стека - наш ответ


if __name__ == "__main__":
    main()
