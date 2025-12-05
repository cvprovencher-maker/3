#Remove Duplicates (Keep Order)
#Return the values in the order they first appeared, without duplicates.
#Example:
#Input: ["apple", "banana", "apple", "kiwi", "banana"]
#Output: ["apple", "banana", "kiwi"]

def remove_duplicates_keep_order(values):
    seen = set()
    result = []
    for v in values:
        if v not in seen:
            seen.add(v)
            result.append(v)
    return result


if __name__ == "__main__":
    test_input = ["apple", "banana", "apple", "kiwi", "banana"]
    print("Input:", test_input)
    print("Output:", remove_duplicates_keep_order(test_input))
