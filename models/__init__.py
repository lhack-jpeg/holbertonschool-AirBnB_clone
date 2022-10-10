#!/bin/usr/python3
"""
This module creates a unique FileStorage instance
for our application
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
