def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return sorted(list(duplicates))


print(find_duplicates([1, 2, 3, 4]))
print(find_duplicates([1, 2, 2, 3, 4, 4]))
print(find_duplicates([1, 1, 1, 1]))
print(find_duplicates([]))
