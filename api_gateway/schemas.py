from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    text: str

class TaskResponse(BaseModel):
    task_id: str
    status: str
    summary: str | None = None
    text: str | None = None