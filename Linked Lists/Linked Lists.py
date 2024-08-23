class link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is link.empty or isinstance(rest, link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def square(x):
    return x * x

def odd(x):
    return x % 2 == 1

def range_link(start, end):
    """Return a link containing consecutive integers from start to end."""
    if start >= end:
        return link.empty
    else:
        return link(start, range_link(start+1, end))

def map_link(f, s):
    """Return a link that contains f(x) for each x in link s."""
    if s is link.empty:
        return s
    else:
        return link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """Return a link that contains only the elements x of link s for which f(x)
    is a true value."""
    if s is link.empty:
        return s
    filter_rest  = filter_link(f, s.rest)
    if f(f.rest):
        return link(f.first, filter_rest)
    else:
        return filter_rest

def add(s, v):
    """Add v to s, returning modified s."""
    assert s is not link.empty
    if s.first > v:
        s.first, s.rest = v, link(s.first, s.rest)
    elif s.first < v and s.rest is link.empty:
        s.rest = link(v)
    elif s.first < v:
        add(s.rest, v)
    return s
