import sys

while True:
    try:
        r_w = input()
        if not r_w:
            break
        process = int(input())

        clock_cpu = 0
        clock_rw = 0

        for _ in r_w:
            if _ == 'R':
                clock_rw += 1
                if clock_rw == process:
                    clock_cpu += 1
                    clock_rw = 0
            if _ == 'W':
                if clock_rw > 0:
                    clock_cpu += 1
                    clock_rw = 0
                clock_cpu += 1

        if clock_rw > 0:
            clock_cpu += 1

        print(clock_cpu)
    except EOFError:
        break
