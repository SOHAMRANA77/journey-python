import os
import shutil

def move_files_by_category(source_folder, destination_folder):
    categories = {
        # Documents
        '.txt': 'Documents',
        '.doc': 'Documents',
        '.docx': 'Documents',
        '.pdf': 'Documents',
        '.ppt': 'Documents',
        '.xls': 'Documents',
        '.xlsx': 'Documents',

        # Pictures
        '.jpg': 'Pictures',
        '.jpeg': 'Pictures',
        '.png': 'Pictures',
        '.gif': 'Pictures',

        # Music
        '.mp3': 'Music',
        '.wav': 'Music',
        '.flac': 'Music',

        # Videos
        '.mp4': 'Videos',
        '.avi': 'Videos',
        '.mov': 'Videos',
        '.mkv': 'Videos',

        # Archives
        '.zip': 'Archives',
        '.rar': 'Archives',
        '.7z': 'Archives',

        # Executables
        '.exe': 'Executables',
        '.msi': 'Executables',

        # Others
        '.': 'Others'  # For files with no extension or unrecognized extension
    }

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Get the file extension
            _, extension = os.path.splitext(file)

            # Determine the category for the file
            category = categories.get(extension.lower(), 'Others')

            # Create the destination folder if it doesn't exist
            dest_folder = os.path.join(destination_folder, category)
            os.makedirs(dest_folder, exist_ok=True)

            # Move the file to the respective folder based on its category
            shutil.move(os.path.join(root, file), os.path.join(dest_folder, file))

if __name__ == "__main__":
    # Replace with the actual source and destination folder paths
    source_folder = "C:\\Users\\soham\\OneDrive\\Pictures\\Camera Roll\\photo"
    destination_folder = "C:\\Users\\soham\\OneDrive\\Pictures\\Camera Roll\\Files"

    # Move files based on their categories
    move_files_by_category(source_folder, destination_folder)
