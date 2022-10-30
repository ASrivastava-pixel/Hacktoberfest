def add(i, j):
    return i + j
def subtract (i, j):
    return i - j

# test cases
# test cases for add method
result1 = add(10, 70)
print(result1)
if result1 == 80:
    print("add test case passed")
else:
    print("add test case failed")
#test cases for subtract method
result2 = subtract (20, 10)
print(result2)
if result2 == 10:
    print("subtract test case passed")
else: 
    print("subtract test case failed")