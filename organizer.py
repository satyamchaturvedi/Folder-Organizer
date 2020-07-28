import os
import collections

DOWNLOADS = os.path.join(os.path.expanduser('~'), 'Downloads')

mapping = collections.defaultdict()
for f in os.listdir(DOWNLOADS):
    if not os.path.isdir(os.path.join(DOWNLOADS, f)):
        file_type = f.split('.')[-1]
        mapping.setdefault(file_type, []).append(f)

for folder_name, folder_items in mapping.items():
    folder_path = os.path.join(DOWNLOADS, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    for folder_item in folder_items:
        source = os.path.join(DOWNLOADS, folder_item)
        destination = os.path.join(folder_path, folder_item)
        print(f'Moving {source} to {destination}')
        os.rename(source, destination)