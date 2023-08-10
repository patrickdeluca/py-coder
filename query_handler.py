```python
from models import Codebase
from utils import execute_query

def query_codebase(query):
    """
    Function to query the codebase
    """
    try:
        result = execute_query(query)
        return result
    except Exception as e:
        print(f"An error occurred while querying the codebase: {e}")
        return None

def get_code_by_filename(filename):
    """
    Function to get code by filename
    """
    query = f"SELECT * FROM Codebase WHERE filename = '{filename}'"
    return query_codebase(query)

def get_code_by_chunk(chunk):
    """
    Function to get code by chunk
    """
    query = f"SELECT * FROM Codebase WHERE chunk = '{chunk}'"
    return query_codebase(query)
```