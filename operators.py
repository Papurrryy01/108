# operators are like symbols or shortcuts 
# that represent specific operations or functions in programming languages.

# 1. Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)          # +
print("Subtraction:", a - b)       # -
print("Multiplication:", a * b)    # *
print("Division:", a / b)          # /
print("Modulus:", a % b)           # %
print("Exponentiation:", a ** b)   # **
print("Floor Division:", a // b)    # //

# 2. Comparison Operators
print("Equal to:", a == b)         # ==
print("Not equal to:", a != b)     # !=
print("Greater than:", a > b)      # >
print("Less than:", a < b)         # <
print("Greater than or equal to:", a >= b)  # >=
print("Less than or equal to:", a <= b)     # <=

# 3. Logical Operators
x = True
y = False
print("Logical AND:", x and y)     # and
print("Logical OR:", x or y)       # or
print("Logical NOT:", not x)       # not

# 4. Assignment Operators
c = 5
c += 2  # c = c + 2
print("c after += 2:", c)
c -= 1  # c = c - 1
print("c after -= 1:", c)
c *= 3  # c = c * 3
print("c after *= 3:", c)
c /= 2  # c = c / 2
print("c after /= 2:", c)
c %= 4  # c = c % 4
print("c after %= 4:", c)
c **= 2 # c = c ** 2
print("c after **= 2:", c)
c //= 3 # c = c // 3
print("c after //= 3:", c)

# 5. Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?", 3 in my_list)        # in
print("Is 6 not in my_list?", 6 not in my_list) # not in

# 6. Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)           # is
print("x is z:", x is z)           # is
print("x is not z:", x is not z)   # is not
print("y is not z:", y is not z)   # is not

# 7. Bitwise Operators
p = 5  # 0101 in binary
q = 3  # 0011 in binary
print("Bitwise AND:", p & q)       # &
print("Bitwise OR:", p | q)        # |
print("Bitwise XOR:", p ^ q)       # ^
print("Bitwise NOT of p:", ~p)     # ~
print("Left Shift p by 1:", p << 1) # <<
print("Right Shift p by 1:", p >> 1) # >>

# Note: Be cautious when using bitwise operators as they operate at the binary level.
# They are typically used in low-level programming, graphics programming, and performance optimization.
# Always ensure you understand their behavior before applying them in your code.
# End of operators.py