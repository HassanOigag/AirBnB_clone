#!/usr/bin/env python3
"""the review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """the Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
