#!/usr/bin/env python3
"""this is the init file of the models package"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
