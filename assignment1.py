str1 = "Hello "
str2 = input("Enter your Name: ")

result = str1 + str2
print(result)

str3 = ", welcome to Python programming"
result = result + str3

print(result)
str1 = "Hello Zara, welcome to Python programming"

# a. First character
print(str1[0])

# b. Last character
print(str1[-1])

# c. First 5 characters
print(str1[:5])

# d. Last 11 characters
print(str1[-11:])

# e. Reverse the string
print(str1[::-1])

# f. Print Python
print(str1[20:26])
strM = "Python beginner tutorial"

# a. Convert to uppercase
print(strM.upper())

# b. Convert to lowercase
print(strM.lower())

# c. Capitalize the sentence
print(strM.capitalize())

# d. Count occurrences of 't'
print(strM.count('t'))

# e. Replace Python with Machine Learning
print(strM.replace("Python", "Machine Learning"))
# Q4 - Tuples

t1 = (10, 20, 30)
t2 = (40, 50, 60)

# a. Concatenate two tuples
t_combine = t1 + t2

print(t_combine)
# b. Repeat elements 3 times
print(t_combine * 3)

# c. Access the 3rd element
print(t_combine[2])

# d. First three elements
print(t_combine[:3])

# e. Last three elements
print(t_combine[-3:])