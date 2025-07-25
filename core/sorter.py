import os
import shutil
from pathlib import Path

from core.logger import setup_logger

class FileSorter:
    FILE_TYPES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.fla'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Scripts': ['.py', '.js', '.java', '.cpp', '.c', '.html', '.css', '.json'],
        'Others': []
    }

    @staticmethod
    def sort_by_type(folder_path, logger):
        if not os.path.isdir(folder_path):
            print(f"ERROR Path does not exists: {folder_path}")
            logger.error(f"Invalided Path: {folder_path}")
            return

        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                ext = Path(file).suffix.lower()
                moved = False

                for folder, extentions in FileSorter.FILE_TYPES.items():
                    if ext in extentions:
                        FileSorter.move_file(file_path, folder_path, folder, logger)
                        moved = True
                        break

                if not moved:
                    FileSorter.move_file(file_path, folder_path, "Others", logger)

    @staticmethod
    def move_file(file_path, base_path, folder_name, logger):
        dest_folder = os.path.join(base_path, folder_name)
        os.makedirs(dest_folder, exist_ok=True)
        dest_path = os.path.join(dest_folder, os.path.basename(file_path))

        try:
            shutil.move(file_path, dest_path)
            print(f"Moved: {file_path} -> {folder_name}/")
            logger.info(f"Moved: {file_path} → {dest_path}")
        except Exception as e:
            print(f"Error moving file {file_path}: {e}")
            logger.error(f"Error moving {file_path}: {e}")