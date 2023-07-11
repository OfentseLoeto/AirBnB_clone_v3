#!/usr/bin/python3
"""
Script that distributes an archive to your web servers
"""

from fabric.api import env, put, run
import os

env.hosts = [52.3.220.1 , 52.91.124.243]
env.user = 'ubuntu'
env.key_filename = '<path_to_ssh_key>'

def do_deploy(archive_path):
    '''
    Destribute an archive to the web server and deploy it
   
    Args:
        archive_path = path to an archive to be deployed.
    Return:
          bool: True if all the operations are successful, False otherwise.
    '''
    if not os.path.exists(archive_path)
        return False
    put(archive_path, "/tmp/")
    
    archive_filename = os.path.basename(archive_path)
    archive_folder = "/data/web_static/releases/{}".format(
        archive_filename.split(".")[0])

    run("mkdir -p {}".format(archive_folder))

    run("tar -zxf /tmp/{} -C {}".format(archive_filename, archive_folder))
    
    run("rm /tmp/{}".format(archive_filename))

    run("mv {}/web_static/* {}".format(archive_folder, archive_folder))

    run("rm -rf {}/web_static".format(archive_folder))
    
    run("rm -rf /data/web_static/current")

    run("ln -s {} /data/web_static/current".format(archive_folder))

    return True
  except Exception:
    return False
    
