```python
import random
from models import Codebase

class CodeGenerator:
    def __init__(self, db):
        self.db = db

    def generate_code(self, filename):
        codebase = self.db.query(Codebase).filter(Codebase.filename == filename).all()
        if not codebase:
            return "No codebase found for the given filename."

        code_chunks = [code.chunk for code in codebase]
        return random.choice(code_chunks)
```