class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches

def tree(label, branches=[]):
    return Tree(label, branches)

def label(t):
    return t.label

def branches(t):
    return t.branches

def is_leaf(t):
    return len(t.branches) == 0

# 定义树结构
numbers = tree(3, [tree(4), tree(5, [tree(6)])])
haste = tree('h', [tree('a'), tree('s', [tree('t')]), tree('e')])

# 打印路径和的函数
def print_sums(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)

print_sums(numbers, 0)