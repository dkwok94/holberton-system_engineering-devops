"""
Fabric file for transferring a file to a remote server from local machine
"""

from fabric.api import *
env.user = 'ubuntu'
env.key_filename = '~/.ssh/dhk'

def pack():
    """
    Packages the current directory into a .tar.gz archive
    """

    local("tar --exclude='*.tar.gz' -cvzf dhkwebapp.tar.gz .")


def deploy():
    """
    Deploys the archive onto the remote server in /tmp/,
    creates a dhkwebapp folder, and extracts the
    archive contents into this directory
    """
    put("dhkwebapp.tar.gz", "/tmp")
    run("mkdir /tmp/dhkwebapp/")
    run("tar -zxvf /tmp/dhkwebapp.tar.gz -C /tmp/dhkwebapp/")


def clean():
    """
    Removes the archive from the local machine
    """

    local("rm dhkwebapp.tar.gz")
