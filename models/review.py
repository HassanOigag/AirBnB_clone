#!/usr/bin/python3
"""create review class"""
from models.base_model import BaseModel


class review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
