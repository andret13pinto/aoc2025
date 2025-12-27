def main(file_path: str) -> int:
    TRACK_SIZE = 100
    START_POSITION = 50

    with open(file_path) as f:
        lines = [line.strip() for line in f]

    position = START_POSITION
    boundary_crossings = 0

    for command in lines:
        direction = command[0]
        quantity = int(command[1:]) % TRACK_SIZE

        # Update position with modulo for automatic wrapping
        if direction == "L":
            position = (position - quantity) % TRACK_SIZE
        else:  # direction == 'R'
            position = (position + quantity) % TRACK_SIZE

        # Position 0 and 100 are the same on a circular track
        if position == 0:
            boundary_crossings += 1

    return boundary_crossings


if __name__ == "__main__":
    print(main("input.txt"))
