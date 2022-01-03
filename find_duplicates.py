import os
from pathlib import Path
from filecmp import cmp

# list all documents
DATA_DIR = Path('./data/data')
files = sorted(os.listdir(DATA_DIR))

# list containing the classes of documents with the same content
duplicates = []
dups = []

# comparison of the documents
for file in files:
    is_duplicate = False

    for class_ in duplicates:
        is_duplicate = cmp(
            DATA_DIR / file,
            DATA_DIR / class_[0],
            shallow=False
        )
        if is_duplicate:
            class_.append(file)
            break

    if not is_duplicate:
        duplicates.append([file])

    # show results
