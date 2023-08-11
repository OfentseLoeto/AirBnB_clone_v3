
import shutil
import os

source_dir = 'web_static/styles/'
destination_dir = 'web_flask/static/styles/'

os.makedirs(destination_dir, exist_ok=True)


# Copy individual files
files_to_copy = ['6-filters.css']
for file_name in files_to_copy:
    source_path = os.path.join(source_dir, file_name)
    destination_path = os.path.join(destination_dir, file_name)
    shutil.copy(source_path, destination_path)

