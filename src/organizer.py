import shutil
from pathlib import Path
from datetime import datetime, timedelta
from config import FILE_CATEGORIES, PROTECTED_FOLDERS, ARCHIVE_OLDER_THAN_DAYS

def organize_files():
    """Main function to organize files in Downloads folder"""
    downloads_path = Path.home() / "Desktop"
    archive_path = downloads_path / "Archive"
    archive_path.mkdir(exist_ok=True)

    for item in downloads_path.iterdir():
        if should_process(item, PROTECTED_FOLDERS):
            process_item(item, downloads_path, archive_path)

def should_process(item, protected_folders):
    """Check if item should be processed"""
    return item.is_file() and item.name not in protected_folders

def process_item(item, base_path, archive_path):
    """Process individual file item"""
    if not categorize_file(item, base_path, FILE_CATEGORIES):
        archive_old_file(item, archive_path, ARCHIVE_OLDER_THAN_DAYS)

def categorize_file(file, base_path, categories):
    """Attempt to categorize file"""
    ext = file.suffix.lower()
    
    for category, extensions in categories.items():
        if ext in extensions:
            move_file(file, base_path / category)
            return True
    return False

def move_file(file, dest_folder):
    """Handle file moving with duplicate protection"""
    dest_folder.mkdir(exist_ok=True)
    destination = get_unique_filename(file, dest_folder)
    shutil.move(str(file), str(destination))

def get_unique_filename(file, dest_folder):
    """Generate unique filename if destination exists"""
    destination = dest_folder / file.name
    if not destination.exists():
        return destination
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return dest_folder / f"{file.stem}_{timestamp}{file.suffix}"

def archive_old_file(file, archive_path, days_threshold):
    """Archive files older than threshold"""
    file_age = datetime.now() - datetime.fromtimestamp(file.stat().st_mtime)
    if file_age.days > days_threshold:
        move_file(file, archive_path)

if __name__ == "__main__":
    organize_files()
    print("✅ Files organized successfully!")
