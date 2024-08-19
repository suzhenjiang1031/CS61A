from fractions import gcd

#Rational arithmetic
def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_ratinal(x, y):
    """Multiply rational numbers x and y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rational_are_equal(x, y):
    """Return whether rational numbers x and y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Print rational x."""
    print(numer(x), "/", denom(x))

#Constructor and selectors
def rational(n, d):
    """Construct a rational number x that represents n/d."""
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select

def rational(n, d):
    """Construct a rational number x that represent n / d."""
    g = gcd(n, d)
    return [n//g, d//g]

def numer(x):
    """Return the numertor of rational number x."""
    return x('n')

def denom(x):
    """Return the denominator of rational number x."""
    return x('d')