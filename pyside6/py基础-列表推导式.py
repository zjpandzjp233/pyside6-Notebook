# 当然！列表推导式是Python中一种简洁且高效的创建列表的方法。下面是一些常见的列表推导式的例子，以及它们的具体应用。

### 基本示例

#### 示例1：生成一个简单的数字列表
# ```python
numbers = [i for i in range(10)]
print(numbers)
# 输出: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ```

#### 示例2：生成一个平方数列表
# ```python
squares = [i**2 for i in range(10)]
print(squares)
# 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# ```

### 条件过滤

#### 示例3：生成偶数列表
# ```python
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)
# 输出: [0, 2, 4, 6, 8]
# ```

#### 示例4：生成大于5的平方数列表
# ```python
large_squares = [i**2 for i in range(10) if i**2 > 5]
print(large_squares)
# 输出: [9, 16, 25, 36, 49, 64, 81]
# ```

### 多重循环

#### 示例5：生成所有可能的组合
# ```python
combinations = [(x, y) for x in range(3) for y in range(3)]
print(combinations)
# 输出: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# ```

#### 示例6：生成特定条件下的组合
# ```python
filtered_combinations = [(x, y) for x in range(3) for y in range(3) if x != y]
print(filtered_combinations)
# 输出: [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
# ```

### 使用现有列表

#### 示例7：转换列表中的元素
# ```python
words = ['apple', 'banana', 'cherry']
uppercase_words = [word.upper() for word in words]
print(uppercase_words) # 这个方法的作用是将字符串 word 中的所有小写字母转换为大写字母。
# 输出: ['APPLE', 'BANANA', 'CHERRY']
# ```

#### 示例8：过滤和转换列表中的元素
# ```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [i**2 for i in numbers if i % 2 == 0]
print(even_squares)
# 输出: [4, 16, 36, 64, 100]
# ```

### 嵌套列表推导式

#### 示例9：扁平化嵌套列表
# ```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)
# 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ```

# 这些示例展示了列表推导式的灵活性和强大功能。你可以根据需要调整这些示例来满足你的具体需求。希望这些示例对你有帮助！





import math

# 浮点数向上取整
print(math.ceil(3.14))  # 输出: 4

# 整数向上取整（如果已经是整数，则返回相同值）
print(math.ceil(5))     # 输出: 5

# 负数向上取整
print(math.ceil(-3.14)) # 输出: -3