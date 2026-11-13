from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Request:
    method: str
    uri: str
    version: str
    headers: defaultdict = defaultdict()
    body: bytes = b''