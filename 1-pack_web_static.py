#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static folder.
"""
from datetime import datetime
from fabric.api import local
import os

def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.
    Returns the archive path if successful, None otherwise.
    """
    try:
       current_time = datetime.now().strftime("%Y%m%d%H%M%S")
       archive_path = "versions/web_static_{}.tgz".format(current_time)
       if not os.path.exists("versions"):
           os.makedirs("versions")
       local("tar -czvf {} web_static".format(archive_path))
       return archive_path
    except:
        return None
