#!/usr/bin/python3
"""The init file to instantiate FileStorage cls & reload method"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
