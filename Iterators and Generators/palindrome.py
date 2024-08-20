def palindrome(s):
    """Return whether s is the same backward and forward."""
    #return list(s) == list(reversed(s))
    return all([a == b for a, b in zip(s, reversed(s))])