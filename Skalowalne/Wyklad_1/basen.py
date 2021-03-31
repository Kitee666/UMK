
#
#    Dawid Sikorski 291951
#

x = input()
y = input()

n = int(x)
p = [int(i) for i in y.split()]

out = 1
prev = -1
step = "inc"

for i in p:
    if step == "inc" and prev > i:
        out += 1
        step = "dec"
    else:
        if step == "dec" and prev < i:
            out += 1
            step = "inc"
    prev = i

print(out)
