from collections import Counter
def is_isomorphic(a,b):
    a_counts = list(Counter(a).values())
    a_counts.sort()
    b_counts = list(Counter(b).values())
    b_counts.sort()
    if a_counts == b_counts:
        return 'yes'
    return 'no'
a,b=input().split()
print(is_isomorphic(a,b))
