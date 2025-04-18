# File categories with all common extensions
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Executables": [".exe", ".msi", ".dmg", ".pkg", ".app", ".apk"],
    "Code": [".py", ".js", ".java", ".c", ".cpp", ".html", ".css", ".php"],
    "Data": [".csv", ".json", ".xml", ".yaml", ".yml"],
    "eBooks": [".epub", ".mobi", ".azw3"]
}

# Folders to never modify
PROTECTED_FOLDERS = [
    "Projects", 
    "Work", 
    "Important", 
    "Personal"
]

# Days before archiving (180 = 6 months)
ARCHIVE_OLDER_THAN_DAYS = 200
