from pydantic import BaseModel

class SuccessResponse(BaseModel):
    message: str = "Success"
    data: dict | list
    status_code: int = 200
    success: bool = True