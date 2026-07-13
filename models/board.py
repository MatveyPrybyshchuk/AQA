"""
BoardResponseCollapse allobject
Схема ответа с данными доски

id integer
title string
description Expand all(string | null)
public boolean
archived boolean
created_by integer
created_a tstring date-time
"""

from pydantic import BaseModel


class BoardResponse(BaseModel):
    id: int
    title: str
    description: str | None
    public: bool
    archived: bool
    created_by: int
    created_at: str
    