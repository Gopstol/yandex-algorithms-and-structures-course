def broken_search(nums, target) -> int:

    half_length: int = len(nums) // 2
    left = 0
    right = len(nums) - 1
    var: int = 0

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] < target:
            if target > nums[right] > nums[middle]:
                right = middle - 1
            elif nums[right] == target:
                return right
            else:
                left = middle + 1

        elif nums[middle] > target:

            if nums[left] < target or nums[left] > nums[middle]:
                right = middle - 1

            elif nums[left] > target:
                left = middle + 1

            elif nums[left] == target:
                return left
        else:
            return middle
    return -1


def test():
    arr = [1, 2, 3, 5, 6, 7, 9, 0]
    assert broken_search(arr, 3) == 2
