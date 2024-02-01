#!/usr/bin/env python3

MAX_DIGITS = 8 #Global Constant

def convert_to_base(decimal, base):
    result = []

    while decimal > 0 and len(result) < MAX_DIGITS + 1:
        decimal *= base
        whole_part = int(decimal)
        decimal -= whole_part

        if base == 60:
            result.append(str(whole_part))
        else:
            result.append(str(whole_part))

    return result

def main():
    import sys

    if len(sys.argv) < 3:
        print("Usage: ./main.py <base> <decimal1> <decimal2> <decimal3>")

    base = int(sys.argv[1])

    print(f"| Base 10 | Base {base} |")
    print(f"| :-------| :--------|")

    for arg in sys.argv[2:]:
        decimal = float(arg)
        result = convert_to_base(decimal, base)

        if base == 2:
            base_str = f"0.{';'.join(result)}" if len(result) > 1 else f"0.{result[0]}"
        else:
            base_str = f"0.{result[0]}{''.join(result[1:])}" if base == 60 else f"(0{';'.join(result)})"

        print(f"| {arg.ljust(7)} | {base_str.ljust(8)} |")

if __name__ == "__main__":
    main()