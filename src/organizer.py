import os
import shutil
from pathlib import Path
from datetime import datetime, timedelta

def organize_files():
    # Set paths
    downloads_path = Path.home() / "Downloads"
    archive_path = downloads_path / "Archive"
    archive_path.mkdir(exist_ok=True)

    # File categories (customize these!)
    categories = {
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Images": [".jpg", ".png", ".gif", ".svg"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Archives": [".zip", ".rar", ".7z"],
        "Code": [".py", ".js", ".html", ".css"],
        "Audio": [".mp3", ".wav"],
        "Executables": [".exe", ".msi", ".dmg"]
    }

    # Protected folders (won't be touched)
    protected = ["Projects", "Work", "Important"]

    # Organize files
    for item in downloads_path.iterdir():
        if item.is_file() and item.name not in protected:
            ext = item.suffix.lower()
            moved = False
            
            # Move to category folder
            for category, exts in categories.items():
                if ext in exts:
                    dest = downloads_path / category / item.name
                    if dest.exists():
                        # Handle duplicates
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        dest = downloads_path / category / f"{item.stem}_{timestamp}{ext}"
                    shutil.move(str(item), str(dest))
                    moved = True
                    break
            
            # Archive old files (>180 days)
            if not moved and item.is_file():
                file_age = datetime.now() - datetime.fromtimestamp(item.stat().st_mtime)
                if file_age.days > 180:
                    shutil.move(str(item), str(archive_path / item.name))

if __name__ == "__main__":
    organize_files()
    print("✅ Files organized successfully!")