import os
from pathlib import  Path

class FileRenamer:
    @staticmethod
    def rename_files(folder_path, pattern, logger):
        count = 1
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                ext = Path(file).suffix
                new_name = f"{pattern}{count}{ext}"
                new_path = os.path.join(folder_path,new_name)
                try:
                    os.rename(file_path,new_path)
                    logger.info(f"Renamed: {file} -> {new_name}")
                    count +=1
                except e:
                    logger.error(f"Error renaming {file}: {e}")