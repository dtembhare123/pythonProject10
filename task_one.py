import argparse
import random from randrange
from typing import list
def rand_range(start:int=1,stop:int=83, limit: int= 15) -> list[int]:


if __name__ == "__main__":
    example = """example:

   python task_one.py --max 87  --any 15
   """

    parser = argparse.ArgumentParser(
        description="CLI tool to fetch resource(s) from API",
        epilog=example
    )

    parser.add_argument(
        "-m",
        "--max",
        type=int,
        default=87,
        help="max number of resources to be fetched"
    )

    parser.add_argument(
        "-a",
        "--any",
        type=int,
        default=15,
        help="random sized chunk of resources to be fetched"
    )

    args = parser.parse_args()
    print(args)
    print(args.any)

    print(args.max)


