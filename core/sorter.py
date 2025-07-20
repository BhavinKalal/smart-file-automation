import os
import shutil
from pathlib import Path

class FileSorter:
    FILE_TYPES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Scripts': ['.py', '.js', '.java', '.cpp', '.c', '.html', '.css', '.json'],
        'Others': []
    }
    
    @staticmethod
    def sort_by_type(folder_path):
        if not os.path.isdir(folder_path):
            print(f"ERROR Path does not exists: {folder_path}")
            return
        
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                ext = Path(file).suffix.lower()
                moved = False
                
                for folder, extentions in FileSorter.FILE_TYPES.items():
                    if ext in extentions:
                        FileSorter.move_file(file_path, folder_path, folder)
                        moved = True
                        break
                
                if not moved:
                    FileSorter.move_file(file_path, folder_path, "Others")
                
    @staticmethod
    def move_file(file_path, base_path, folder_name):
        dest_folder = os.path.join(base_path, folder_name)
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(dest_folder, os.path.basename(file_path)))
        print(f"Moved: {file_path} -> {folder_name}/")