# ===================== 1. LeetCode20 括号匹配 Valid Parentheses =====================
def is_valid(s: str) -> bool:
    # 建立右括号到左括号的映射，遇到右括号，去匹配栈顶
    match_dict = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in s:
        # 如果是左括号，压入栈
        if char not in match_dict:
            stack.append(char)
        else:
            # 是右括号：栈为空（没有可以匹配的左括号） 或者 栈顶和当前右括号不匹配 → False
            if not stack or stack.pop() != match_dict[char]:
                return False
    # 遍历全部结束，栈必须是空，才代表全部匹配完毕
    return len(stack) == 0


# ===================== 2. LeetCode155 最小栈 MinStack O(1)获取最小值 =====================
class MinStack:
    def __init__(self):
        self.main_stack = []    # 主栈：正常存所有元素
        self.min_stack = []     # 辅助栈：保存每一步的最小值

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        # 辅助栈压入：当前值 和 辅助栈栈顶 更小的那一个
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # 出栈，两个栈一起弹出
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        # 直接拿辅助栈栈顶，O(1)
        return self.min_stack[-1]


# ===================== 3. LeetCode232 两个栈实现队列 MyQueue =====================
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        # 入队：直接加到in_stack
        self.in_stack.append(x)

    def transfer(self):
        # 只有out_stack空的时候，才把in_stack全部倒过来
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self.transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0


# ===================== 4. 递归演示：阶乘 factorial（理解函数调用栈） =====================
def factorial(n: int):
    print(f"进入 factorial({n})，压栈帧")
    if n == 1:
        print(f"factorial(1) 触底，返回 1")
        return 1
    res = n * factorial(n - 1)
    print(f"factorial({n}) 计算完成：{n} * factorial({n-1}) = {res}，弹出栈帧")
    return res


# ===================== 5. 递归经典：汉诺塔 Hanoi =====================
def hanoi(n, source, target, assist):
    """
    n:圆盘数量
    source:源柱子
    target:目标柱子
    assist:辅助柱子
    """
    if n == 1:
        print(f"移动圆盘 1：{source} → {target}")
        return
    # 第一步：把上面 n-1 个，从源 → 辅助
    hanoi(n - 1, source, assist, target)
    # 第二步：把最底下第n个，源 → 目标
    print(f"移动圆盘 {n}：{source} → {target}")
    # 第三步：把 n-1 个，从辅助 → 目标
    hanoi(n - 1, assist, target, source)


# ===================== 测试入口：运行所有功能 =====================
if __name__ == "__main__":
    print("======= 测试1：括号匹配 =======")
    test_str1 = "(()())("
    test_str2 = "(()())"
    print(f"{test_str1} 是否合法：{is_valid(test_str1)}")
    print(f"{test_str2} 是否合法：{is_valid(test_str2)}")

    print("\n======= 测试2：最小栈 =======")
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(f"当前最小值：{min_stack.getMin()}")
    min_stack.pop()
    print(f"栈顶元素：{min_stack.top()}")
    print(f"当前最小值：{min_stack.getMin()}")

    print("\n======= 测试3：双栈实现队列 =======")
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(f"队首peek：{q.peek()}")
    print(f"出队pop：{q.pop()}")
    print(f"队列是否为空：{q.empty()}")

    print("\n======= 测试4：阶乘（观察函数调用栈打印） =======")
    factorial(3)

    print("\n======= 测试5：汉诺塔 3个圆盘 =======")
    hanoi(3, "A", "C", "B")
