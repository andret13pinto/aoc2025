def main(file_path: str) -> int:
    TRACK_SIZE = 100
    START_POSITION = 50

    with open(file_path) as f:
        lines = [line.strip() for line in f]

    position = START_POSITION
    boundary_crossings = 0

    for command in lines:
        direction = command[0]
        quantity = int(command[1:])

        # Update position with modulo for automatic wrapping
        for i in range(quantity):
            if direction == "L":
                position -= 1
                if position == -1:
                    position = 99
            else:
                position += 1
                if position == 101:
                    position = 1
            if position in (0, 100):
                boundary_crossings += 1

        print(command, boundary_crossings)

    return boundary_crossings


if __name__ == "__main__":
    print(main("input.txt"))
