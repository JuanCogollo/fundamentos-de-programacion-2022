from datetime import timedelta


def time_in(registers):
    time_in_barber = []
    h, m, s = "", "", ""
    for r in registers:
        date, time_go, time_back = r
        h0, m0, s0 = time_go.split(":")
        h1, m1, s1 = time_back.split(":")
        time_go = timedelta(hours=int(h0), minutes=int(m0), seconds=int(s0))
        time_back = timedelta(hours=int(h1), minutes=int(m1), seconds=int(s1))
        time_left = time_back - time_go

        time_in_barber.append(time_left)

    print(time_in_barber)


def main():
    c = int(input())
    registers = []

    for i in range(c):
        entry = input()
        date, place, time_go, time_back = entry.split(", ")

        if place == "barberia":
            registers.append([date, time_go, time_back])

    time_in(registers)


main()

# 6
# 2000-06-10, barberia, 14:00:00, 18:30:00
# 2000-06-12, supermercado, 08:00:00, 12:00:00
# 2000-06-20, taller mecanico, 16:20:00, 17:35:00
# 2000-06-25, barberia, 09:45:00, 12:10:40
# 2000-07-08, barberia, 15:33:20, 20:00:55
# 2000-7-13, supermercado, 12:34:56, 14:54:32
