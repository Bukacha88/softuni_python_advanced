numbers = [int(el) for el in input().split(', ')]
positive = [str(el) for el in numbers if el >= 0]
negative = [str(el) for el in numbers if el < 0]
even = [str(el) for el in numbers if el % 2 == 0]
odd = [str(el) for el in numbers if not el % 2 == 0]
print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
