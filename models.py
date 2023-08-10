```python
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CodeBase(Base):
    __tablename__ = 'codebase'

    id = Column(Integer, primary_key=True)
    filename = Column(String(100), nullable=False)
    chunk = Column(Text, nullable=False)

    def __init__(self, filename, chunk):
        self.filename = filename
        self.chunk = chunk
```