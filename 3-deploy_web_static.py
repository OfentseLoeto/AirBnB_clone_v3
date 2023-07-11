#!/usr/bin/python3
"""
The script that creates and distributes an archive to your web servers.
"""
from fabric.api import env, run
from fabric.state import output
from datetime import datetime
from os.path import exists
from fabric.api import put

def do_deploy():
    """
    Create and distribute an archive to the web sever
    Return:
          bool: True if all operations are successful, False otherwise.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

