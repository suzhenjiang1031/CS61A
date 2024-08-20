# def count_partitions(n, m):
#     """Count partitions
#     >>>conut_partitions(6, 4)
#     9
#     """
#     if n < 0 or m == 0:
#         return 0
#     else:
#         exact_match = 0
#         if n == m:
#             exact_match = 1
#     with_m = count_partitions(n - m, m)
#     without_m = count_partitions(n, m - 1)
#     return exact_match + with_m +without_m

# def list_partitions(n, m):
#     """list partitions
#     #>>>list_partitions(6, 4)
#     [[2, 4]
#      [1, 1, 4]
#      [3, 3]
#      [1, 2, 3]
#      [1, 1, 1, 3]
#      [2, 2, 2]
#      [1, 1, 2, 2]
#      [1, 1, 1, 1, 2]
#      [1, 1, 1, 1, 1, 1]]
#     """
#     if n < 0 or m == 0:
#         return []
#     else:
#         exact_match = []
#         if n == m:
#             exact_match = [[m]]
#     with_m = [p + [m] for p in list_partitions(n - m, m)]
#     without_m = list_partitions(n, m - 1)
#     return exact_match + with_m +without_m
#
# def partitions(n, m):
#     if n < 0 or m == 0:
#         return []
#     else:
#         exact_match = []
#         if n == m:
#             exact_match = [str(m)]
#     with_m = [p + ' + ' + str(m) for p in partitions(n - m, m)]
#     without_m = partitions(n, m - 1)
#     return exact_match + with_m +without_m

def partitions(n, m):
    """ Yield partitions"""
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n-m, m):
            yield p + '+' + str(m)
        yield from partitions(n, m-1)