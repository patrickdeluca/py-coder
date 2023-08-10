```python
import os
from utils import chunk_string

def ingest_file(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"No such file: '{filepath}'")

    with open(filepath, 'r') as file:
        content = file.read()

    return content

def split_file_by_name(content):
    file_dict = {}
    lines = content.split('\n')
    current_file = ''

    for line in lines:
        if line.startswith('##'):  # Assuming file names in the text file are prefixed with '##'
            current_file = line[2:]
            file_dict[current_file] = ''
        else:
            file_dict[current_file] += line + '\n'

    return file_dict

def chunk_and_store(file_dict, chunk_size):
    for filename, content in file_dict.items():
        chunks = chunk_string(content, chunk_size)
        for i, chunk in enumerate(chunks):
            # Assuming a function 'store_chunk' in 'database_handler.py' that stores a chunk in the database
            from database_handler import store_chunk
            store_chunk(filename, i, chunk)
```