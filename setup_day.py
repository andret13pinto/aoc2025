import argparse
import os
import dotenv
from urllib.request import Request, urlopen
import shutil


def download_input(day: int) -> None:
    # Placeholder for input downloading logic
    dotenv.load_dotenv()
    session_cookie = os.getenv("AOC_SESSION")
    if not session_cookie:
        raise ValueError(
            "AOC_SESSION environment variable is not set. Please set it to your session cookie."
        )

    print(f"Downloading input for day {day:02d}...")

    request = Request(url=f"https://adventofcode.com/2024/day/{day}/input")
    request.add_header("Cookie", f"session={session_cookie}")

    with urlopen(request) as response:
        input_text = response.read().decode("utf-8").strip()

    with open(f"day{day:02d}/input.txt", "w") as f:
        f.write(input_text)


def create_day_subdirectory(day: int, part: int) -> None:
    part_dir = os.path.join(f"day{day:02d}", f"part{part}")
    if not os.path.exists(part_dir):
        os.makedirs(part_dir)
        with open(os.path.join(part_dir, "__init__.py"), "w") as f:
            f.write(f"# Day {day:02d} Part {part} module\n")
        print(f"Created directory and __init__.py for day {day:02d} part {part}")
    else:
        print(f"Directory for day {day:02d} part {part} already exists.")


def create_day_directory(day: int) -> None:
    day_dir = f"day{day:02d}"
    if not os.path.exists(day_dir):
        os.makedirs(day_dir)
        create_day_subdirectory(day, 1)
        create_day_subdirectory(day, 2)
        with open(os.path.join(day_dir, "__init__.py"), "w") as f:
            f.write(f"# Day {day:02d} module\n")
        print(f"Created directory and __init__.py for day {day:02d}")
    else:
        print(f"Directory for day {day:02d} already exists.")


def create_day_files(day: int) -> None:
    day_dir = f"day{day:02d}"
    if not os.path.exists(day_dir):
        print(f"Directory for day {day:02d} does not exist. Please create it first.")
        return

    with open(os.path.join(day_dir, "part1/solution.py"), "w") as f:
        shutil.copy("templates/solution.py", f.name)

    with open(os.path.join(day_dir, "part2/solution.py"), "w") as f:
        shutil.copy("templates/solution.py", f.name)

    with open(os.path.join(day_dir, "part1/test.py"), "w") as f:
        shutil.copy("templates/test.py", f.name)

    with open(os.path.join(day_dir, "part2/test.py"), "w") as f:
        shutil.copy("templates/test.py", f.name)

    with open(os.path.join(day_dir, "test_input.txt"), "w") as f:
        shutil.copy("templates/test_input.txt", f.name)

    print(f"Created part1.py, part2.py and test files for day {day:02d}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--day", type=int, required=True, help="Day of the Advent of Code challenge"
    )
    args = parser.parse_args()

    create_day_directory(args.day)
    download_input(args.day)
    create_day_files(args.day)


if __name__ == "__main__":
    main()
