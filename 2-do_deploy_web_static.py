#!/usr/bin/python3
"""
Fabric script to destribute archive to web server
"""
from fabric.api import run, put, env
import os

env.hosts = '54.144.134.143'
env.user = 'ubuntu'

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
       release_path = "/data/web_static/release/{}".format(archive_no_ext)

       put(archive_path, archive_dest)
       run("mkdir -p {}".format(release_path))
       run("tar -xzf {} -C {}".format(archive_dest, releases_path))
       run("rm {}".format(archive_dest))
       run("mv {}/web_static/* {}".format(releases_path, releases_path))
       run("rm -rf {}/web_static".format(releases_path))
       run("rm -rf /data/web_static/current")
       run("ln -s {} /data/web_static/current".format(releases_path))
       return True
    except:
       return False
