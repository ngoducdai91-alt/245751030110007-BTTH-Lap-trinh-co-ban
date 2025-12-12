print("NGÔ ĐỨC ĐAI")
print("msv:245751030110007")
print("21)")
print("Vui lòng nhập chuỗi các số nhị phân gồm 4 số (phân tách bởi dấu phẩy):")
binary_input = input()
numbers = binary_input.split(',')
divisible_by_5 = []
for num_str in numbers:
    num_str = num_str.strip()
    try:
        decimal_num = int(num_str, 2)
        if decimal_num % 5 == 0:
            divisible_by_5.append(num_str)      
    except ValueError:
        pass
print(",".join(divisible_by_5))
print("22)")
def check_even_digits(number):
    s_num = str(number)
    for digit_char in s_num:
        digit = int(digit_char)
        if digit % 2 != 0:
            return False
    return True
even_digit_numbers = []
for i in range(1000, 3001):
    if check_even_digits(i):
        even_digit_numbers.append(str(i))
print(",".join(even_digit_numbers))
print("23)")
print("Vui lòng nhập một câu:")
input_string = input()
letters_count = 0
digits_count = 0
for char in input_string:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1
print(f"Số chữ cái là: {letters_count}")
print(f"Số chữ số là: {digits_count}")
