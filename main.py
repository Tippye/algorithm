# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
from bubbleSort import bubble_sort
from insertionSort import insertion_sort
from selectionSort import selection_sort

arr = [4, 6, 1, 9, 3, 5]

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print(arr)
    print(insertion_sort(arr))
