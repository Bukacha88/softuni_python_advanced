numbers = list(map(int, input().split()))
positive_sum = 0
negative_sum = 0
for num in numbers:
    if num >= 0:
        positive_sum += num

    else:
        negative_sum += num
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
elif abs(negative_sum) < positive_sum:
    print("The positives are stronger than the negatives")