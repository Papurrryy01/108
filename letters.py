words = ["apple", "breeze", "sun", "mountain", "cat", "python"]

count_five_or_more = sum(1 for word in words if len(word) >= 5)

print(count_five_or_more)
