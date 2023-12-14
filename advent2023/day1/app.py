def open_file(file_path):
    lines = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            lines.append(line.strip())

    return lines


def find_digit(line):
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9','0']
    for char in line:
        if char in digits:
            return char


i = open_file('input.txt')
numbers = []

for j in i:
    k = list(j)
    first_digit = find_digit(k)
    k.reverse()
    last_digit = find_digit(k)
    combined = int(first_digit + last_digit)
    numbers.append(combined)

print(sum(numbers))
