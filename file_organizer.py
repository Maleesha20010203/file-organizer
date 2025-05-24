import os
import shutil
from pathlib import Path

# Define file type categories at module level for easy modification
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".txt", ".rtf"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Video": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
    "Executables": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php", ".sh", ".json", ".xml"],
    "Spreadsheets": [".csv", ".xls", ".xlsx", ".ods"],
    "Presentations": [".ppt", ".pptx", ".odp"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
}

def create_category_folders(directory):
    """Create all necessary category folders in the target directory."""
    for category in FILE_CATEGORIES:
        os.makedirs(os.path.join(directory, category), exist_ok=True)
    os.makedirs(os.path.join(directory, "Others"), exist_ok=True)

def get_file_category(file_ext):
    """Determine the category for a given file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_ext in extensions:
            return category
    return "Others"

def move_file_with_feedback(file_path, dest_folder, file_name):
    """Handle file movement with error handling and user feedback."""
    try:
        shutil.move(file_path, dest_folder)
        print(f"✓ Moved: {file_name} → {os.path.basename(dest_folder)}")
        return True
    except Exception as e:
        print(f"✗ Error moving {file_name}: {e}")
        return False

def organize_directory(directory):
    """Organize files in the specified directory."""
    create_category_folders(directory)
    
    files = [f for f in os.listdir(directory) 
             if os.path.isfile(os.path.join(directory, f))]
    
    moved_files = 0
    skipped_files = 0

    for file in files:
        file_path = os.path.join(directory, file)
        
        # Skip the script file if it's in the same directory
        if file == os.path.basename(__file__):
            skipped_files += 1
            continue

        file_ext = Path(file).suffix.lower()
        category = get_file_category(file_ext)
        dest_folder = os.path.join(directory, category)
        
        if move_file_with_feedback(file_path, dest_folder, file):
            moved_files += 1

    print(f"\nOrganization complete! {moved_files} files were moved. {skipped_files} files were skipped.")
    return moved_files, skipped_files

def get_directory_from_user():
    """Get target directory from user input with validation."""
    print("\n" + "="*50)
    print("FILE ORGANIZER INSTRUCTIONS".center(50))
    print("="*50)
    print("\n1. Right-click your target folder in Explorer")
    print("2. Select 'Copy Path' or 'Copy Relative Path'")
    print("3. Paste it here (Ctrl+V or right-click paste)")
    print("\n(Enter 'q' to quit)")
    print("="*50 + "\n")

    while True:
        directory = input("\n📁 Paste folder path here: ").strip().strip('"\'')
        
        if directory.lower() == 'q':
            return None
        
        if not os.path.isdir(directory):
            print("\n❌ Error: Directory doesn't exist. Please try again.")
            print(f"(You entered: {directory})")
            continue
        
        return directory

def main():
    """Main program loop."""
    print("="*50)
    print("FILE ORGANIZER".center(50))
    print("="*50)
    
    while True:
        directory = get_directory_from_user()
        if not directory:
            break
        
        print(f"\n🔍 Organizing files in: {directory}")
        organize_directory(directory)
        
        choice = input("\nOrganize another folder? (y/n): ").lower()
        if choice != 'y':
            break
    
    print("\n✨ File organization complete. Happy coding!")

if __name__ == "__main__":
    main()