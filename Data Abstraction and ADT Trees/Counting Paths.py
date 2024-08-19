class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches

def label(tree):
    return tree.label

def branches(tree):
    return tree.branches

def count_paths(t, total):
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - label(t)) for b in branches(t)])