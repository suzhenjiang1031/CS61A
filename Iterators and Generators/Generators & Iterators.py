def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)
    else:
        yield 'Blast off'

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def substring(s):
    if s:
        yield from prefixes(s)
        yield from substring(s[1:])