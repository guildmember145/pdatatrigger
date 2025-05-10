from pydantic import BaseModel


class ScanRequest(BaseModel):
    target: str


class ScanResult(BaseModel):
    target: str
    vulnerabilities: list[str]
