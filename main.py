import argparse
import os
import sys
from core.sorter import FileSorter

def main():
    # Creating Parser
    parser = argparse.ArgumentParser(
        description="Smart File Automation system - Organize and Clean your files"
    )

    # Adding arguments
    parser.add_argument(
        "--path", type=str, required=True,
        help="Path to the target folder"
    )

    parser.add_argument(
        "--sort", action="store_true",
        help="Sort files by type"
    )

    # Parse the arguments
    args = parser.parse_args()

    # validate Path
    if not os.path.exists(args.path):
        print(f"Error: The provided path doesn't exists")
        sys.exit(1)

    # display arguments
    print(f"Target path: {args.path}")
    if args.sort:
        print(f"[INFO] Sorting files by type...")
        FileSorter.sort_by_type(args.path)


if __name__ == '__main__':
    main()