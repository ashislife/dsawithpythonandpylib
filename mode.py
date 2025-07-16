
def calculate_mode(data):

    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())
    mode = [num for num, freq in frequency.items() if freq == max_freq]

    return mode

numbers = [1, 2, 2, 3, 3, 4, 5]
print(calculate_mode(numbers))