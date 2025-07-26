import argparse
import os
import sys
from core.sorter import FileSorter
from core.renamer import FileRenamer
from core.logger import setup_logger

def get_args():
    parser = argparse.ArgumentParser(description="Smart File Automation Tool")
    parser.add_argument('--path', required=True, help="Target directory path")
    parser.add_argument('--sort', action='store_true', help="Sort files by type")
    parser.add_argument('--rename', metavar='PATTERN', help="Rename files with a pattern, e.g., 'Document_'")
    return parser.parse_args()

def main():
    # Parse the arguments
    args = get_args()
    logger = setup_logger()

    # Adding arguments
    # parser.add_argument(
    #     "--path", type=str, required=True,
    #     help="Path to the target folder"
    # )

    # parser.add_argument(
    #     "--sort", action="store_true",
    #     help="Sort files by type"
    # )

    # validate Path
    if not os.path.exists(args.path):
        print(f"Error: The provided path doesn't exists")
        sys.exit(1)

    # display arguments
    print(f"Target path: {args.path}")
    if args.sort:
        print(f"[INFO] Sorting files by type...")
        FileSorter.sort_by_type(args.path, logger)

    if args.rename:
        print(f"Renaming files with pattern: {args.rename}")
        FileRenamer.rename_files(args.path, args.rename, logger)


if __name__ == '__main__':
    main()