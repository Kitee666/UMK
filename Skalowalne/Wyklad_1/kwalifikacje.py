
#
#    Dawid Sikorski 291951
#
def binary_search(left, right, val, tab):
    if left > right:
        return left + 1
    if tab[(left + right) // 2] >= val:
        right = (left + right) // 2 - 1
    else:
        left = (left + right) // 2 + 1
    return binary_search(left, right, val, tab)


x = input()
y = input()
z = input()

n = int(x)
v = [int(i) for i in y.split()]
q = int(z)
test = [int(input()) for _ in range(q)]

v.sort(reverse=True)

sums = [v[0]]
for i in range(1, n):
    sums.append(sums[-1] + v[i])

for t in test:
    print(binary_search(0, n - 1, t, sums))
