def main(file_path: str):
    with open(file_path) as f:
        lines = f.readlines()

    count, pos = 0, 50

    for cmd in lines:
        dir, qty = cmd[0], int(cmd[1:]) % 100
        if dir == "L":
            if pos - qty < 0:
                pos = 100 + (pos - qty)
            else:
                pos -= qty
        else:
            if pos + qty > 100:
                dif = pos + qty - 100
                pos = dif
            else:
                pos += qty
        print(pos)
        if pos in (0, 100):
            count += 1

    return count


if __name__ == "__main__":
    print(main("input.txt"))
