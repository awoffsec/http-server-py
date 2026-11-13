from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Response:
    status: int
    reason: str
    headers: defaultdict = defaultdict()
    body: bytes = b""