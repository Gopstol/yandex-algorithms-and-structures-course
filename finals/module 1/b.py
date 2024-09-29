def main(k) -> int:
    matrix: list = []
    nums: list = [0] * 9
    counter: int = 0

    for i in range(4):
        matrix.append(list(input()))
        for j in matrix[i]:
            if j != ".":
                nums[int(j) - 1] += 1
    
    for i in nums:
        if i <= 2 * k and i != 0:
            counter += 1

    return counter


if __name__ == "__main__":
    kol = int(input())
    print(main(kol))

