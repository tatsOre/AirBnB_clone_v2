#!/usr/bin/python3
"""Module for pack_web_static"""
from datetime import datetime
from fabric.api import local, cd
from os import path

def do_pack():
    """
    Module that generates a .tgz archive from the contents of the web_static
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
            return file
        else:
            print('Failed')
            return None
