arr = [10, 20, 30, 20, 40, 10, 50, 30]
print("Original Array:", arr)

arr.append(60)
print("After Append:", arr)

str_arr = [str(x) for x in arr]
joined_string = ",".join(str_arr)
print("\nArray as String:")
print(joined_string)

unique_elements = set(arr)
print("\nUnique Elements:")
print(unique_elements)

frequency = {}
for item in arr:
    frequency[item] = frequency.get(item, 0) + 1
print("\nFrequency of Elements:")
print(frequency)

result_tuple = (min(arr), max(arr))
print("\nTuple (Minimum, Maximum):")
print(result_tuple)

summary = {
    "Total Elements": len(arr),
    "Unique Elements": len(unique_elements),
    "Minimum": min(arr),
    "Maximum": max(arr)
}
for key, value in summary.items():
    print(key, ":", value)
