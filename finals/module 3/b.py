# средняя скорость работы - O(nlogn), худшая - О(n^2)
# дополнительная память O(1)

def quicksort(nums, left_offset, right_offset) -> list:
    if right_offset - left_offset <= 1:
        return nums
    pivot: int = min(nums[left_offset][1], nums[left_offset + (right_offset - left_offset) // 2][1])
    left: int = left_offset
    right: int = right_offset - 1
    # print(nums[left_offset:right_offset], pivot, left_offset, right_offset)
    while left < right:
        if nums[left][1] == nums[right][1]:
            if nums[left][2] > nums[right][2]:
                nums[left], nums[right] = nums[right], nums[left]
                if nums[left][1] >= pivot:
                    left += 1
            elif nums[left][2] == nums[right][2]:
                if nums[left][0] > nums[right][0]:
                    nums[left], nums[right] = nums[right], nums[left]
            else:
                if nums[left][1] == pivot:
                    left += 1
        if nums[left][1] <= pivot < nums[right][1]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left][1] > pivot:
            left += 1
        if nums[right][1] <= pivot:
            right -= 1

    # print(nums[left_offset:right_offset])
    # print("___")
    if right == right_offset - 1 or right == left_offset or right_offset - left_offset == 2:
        return nums
    offset = min(left, right)
    if nums[offset][1] > pivot:
        offset += 1

    nums = quicksort(nums, left_offset, offset)
    nums = quicksort(nums, offset, right_offset)
    return nums


if __name__ == "__main__":
    n = int(input())
    results: list = []

    for i in range(n):
        results.append(input().split())
        results[-1][1] = int(results[-1][1])
        results[-1][2] = int(results[-1][2])

    results = quicksort(results, 0, n)
    for user in results:
        print(user[0])
