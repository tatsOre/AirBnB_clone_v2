#!/usr/bin/python3
"""Module for 2-do_deploy_web_static.py"""
from datetime import datetime
from fabric.api import local, cd, env, put, run
from os import path


env.hosts = ['35.229.36.239', '54.157.244.143']


def do_deploy(archive_path):
    """
    Module that distributes an archive to your web servers.
    """
    if not path.exists(archive_path):
        return False

    print("Executing task 'do_deploy'")
    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, '/tmp/')
    # filename: name without path
    filename = archive_path.split('/')[1]
    # folder: /data/web_static/releases/<archive filename without extension>
    directory = '/data/web_static/releases/' + filename[:-4]
    # Create folder
    run("mkdir -p {}".format(directory))
    # Uncompress file to the on the web server
    run('tar -xzf /tmp/{} -C {}'.format(filename, directory))
    # Delete the archive from the web server
    run('rm /tmp/{}'.format(filename))
    # something else
    run("mv {}/web_static/* {}".format(directory, directory))
    # Delete the symbolic link /data/web_static/current from the web server
    run("rm -rf {}/web_static".format(directory))
    run("rm -rf /data/web_static/current")
    # Create a new the symlink /data/web_static/current on the web server,
    # linked to the new version ot the code --->
    # (/data/web_static/releases/<filename without extension>)
    run("ln -s {} /data/web_static/current".format(directory))
    print("New version deployed!")
    return True
