import sys

from typing import List, Optional


def run(args: Optional[List[str]] = None):
    print(args or sys.argv[1:])


if __name__ == '__main__':
    run(sys.argv[1:])
