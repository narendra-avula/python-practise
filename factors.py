__author__ = 'narendra'


# def factors(n):
#     result = []
#     for i in range(1, n+1):
#         if n%i == 0:
#             result.append(i)
#     return result


# def factors(n):
#     for i in range(1, n+1):
#         if n%i==0:
#             yield i

def factors(n):
    k=1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k
print factors(100)