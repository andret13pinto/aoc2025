def main(file_path: str) -> int:
    START_POSITION = 50
    TRACK_SIZE = 100

    with open(file_path) as f:
        lines = [line.strip() for line in f]

    position = START_POSITION
    boundary_crossings = 0

    for command in lines:
        direction = command[0]
        quantity = int(command[1:])

        # Track has 101 positions (0-100) with cycle size 100
        # Moving right: position 101 wraps to 1
        # Moving left: position -1 wraps to 99
        # Boundaries are at positions 0 and 100

        if direction == "R":
            # Calculate final raw position
            end_pos = position + quantity
            # Count boundary crossings: we cross at 100, 200, 300, ...
            crossings = end_pos // TRACK_SIZE
            # Special case: if we start AT position 100, the first crossing doesn't count
            # because we're moving away from the boundary
            if position == TRACK_SIZE:
                crossings -= 1
            boundary_crossings += crossings
            # Calculate wrapped position
            # end_pos % 100 gives: 0 for 100/200/300, 1 for 101/201, etc.
            position = end_pos % TRACK_SIZE
            if position == 0:
                position = TRACK_SIZE
        else:  # direction == "L"
            # Calculate final raw position
            end_pos = position - quantity
            # Count boundary crossings: we cross at 0, -100, -200, ...
            if end_pos <= 0:
                # Use divmod to find how many complete cycles and remainder
                cycles, remainder = divmod(-end_pos, TRACK_SIZE)
                # We cross once when leaving position range, then once per cycle
                crossings = cycles + 1
                # Special case: if we start AT position 0, the first crossing doesn't count
                if position == 0:
                    crossings -= 1
                boundary_crossings += crossings
                # Calculate wrapped position
                position = TRACK_SIZE if remainder == 0 else TRACK_SIZE - remainder
            else:
                # Calculate wrapped position (no crossing)
                position = end_pos

    return boundary_crossings


if __name__ == "__main__":
    print(main("input.txt"))
