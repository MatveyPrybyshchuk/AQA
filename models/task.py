"""
TaskResponseCollapse allobject
Схема ответа с данными задачи

id integer
titlestring
descriptionCollapse all(string | null)
Any ofCollapse all(string | null)
#0string
#1null
statusstring
prioritystring
board_idinteger
created_byinteger
assignee_idCollapse all(integer | null)
Any ofCollapse all(integer | null)
#0integer
#1null
created_atstringdate-time
updated_atstringdate-time
"""

from pydantic import BaseModel


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    priority: str
    board_id: int
    created_by: int
    assignee_id: int | None
    created_at: str
    updated_at: str
    