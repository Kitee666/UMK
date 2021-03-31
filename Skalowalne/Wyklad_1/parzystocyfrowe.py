
#
#    Dawid Sikorski 291951
#

def write(value, step):
    if value == 0:
        return
    write(value // 5, step + 1)
    if step % 3 == 0:
        print(" ", end='')
    print(2 * (value % 5), end='')


x = input()

n = int(x)

write(n, 1)
