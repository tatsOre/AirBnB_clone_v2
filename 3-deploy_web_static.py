#!/usr/bin/python3
"""Module for 3-deploty_web_static"""
from datetime import datetime
from fabric.api import local, cd, env, put, run
from os import path

env.hosts = ['35.229.36.239', '54.157.244.143']


def do_pack():
    """
    Script that generates a .tgz archive from the contents of the web_static
    File Format: web_static_<year><month><day><hour><minute><second>.tgz
    """
    directory = 'versions'
    source = 'web_static'
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    file = "{}_{}.tgz".format(source, date)
    if not path.exists(directory):
        local("mkdir {}".format(directory))
    with cd('/{}'.format(directory)):
        print("Packing {} to {}/{}".format(source, directory, file))
        pack = local("tar -czvf {}/{} {}".format(directory, file, source))
        if pack.succeeded:
            print("web_static packed: {}/{}".format(directory, file))
            return "{}/{}".format(directory, file)
        else:
            print('Failed')
            return None


def do_deploy(archive_path):
    """
    Script that distributes an archive to your web servers.
    """
    if not path.exists(archive_path):
        return False

    print("Executing task 'do_deploy'")
    put(archive_path, '/tmp/')
    filename = archive_path.split('/')[1]
    directory = '/data/web_static/releases/' + filename[:-4]
    run("mkdir -p {}".format(directory))
    run('tar -xzf /tmp/{} -C {}'.format(filename, directory))
    run('rm /tmp/{}'.format(filename))
    run("mv {}/web_static/* {}".format(directory, directory))
    run("rm -rf {}/web_static".format(directory))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(directory))
    print("New version deployed!")
    return True


def deploy():
    """Full deployment"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
