#!/usr/bin/python3
"""
The script compresses the contents of web_static folder into a .tgz archive.
It then returns path to the archive if successfully generated, Otherwise None.
"""
from fabric.api import local
from datetime import datetime

def do_pack():

    try:
       current_time = datetime.now().strftime('%Y%m%d%H%M%S')
       archive_path = "version/web_static_{}.tgz".format(current_time)
       local("mkdir -p versions")
       local("tar -czvf {} web_static".format(archive_path))
       return archive_path
    except Exception:
       return None
