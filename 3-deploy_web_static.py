#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers.
"""

from fabric.api import local, run, put, env
from datetime import datetime
import os


env.hosts = '54.144.134.143'
env.user = 'ubuntu'


def do_pack():
    """
    Creates a compressed archive of web_static folder.
    Returns the archive path if successful, None otherwise.
    """
    now = datetime.now()
    archive_filename = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    local("mkdir -p versions")
    result = local("tar -czvf versions/{} web_static".format(archive_filename))
    if result.failed:
        return None
    return "versions/{}".format(archive_filename)


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    Returns True if successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_filename)[0]
        archive_dest = "/tmp/{}".format(archive_filename)
        releases_path = "/data/web_static/releases/{}".format(archive_no_ext)

        put(archive_path, archive_dest)
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(archive_dest, releases_path))
        run("rm {}".format(archive_dest))
        run("mv {}/web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}/web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        return True
    except:
        return False


def deploy():
    """
    Creates and distributes an archive to web servers.
    Returns True if successful, False otherwise.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
