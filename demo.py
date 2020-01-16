import click
import os, sys
import os.path
import IPython.core.ultratb
from os.path import dirname, abspath

@click.command()
@click.option('--name', prompt='Project name',
              help='The person to greet.')
def FileExists(name):
    if os.path.exists(name):
        path = os.getcwd()
        raise FileExistsError(path,"already exists")
        
    else:
        return CreateProject(name)


def CreateProject(name):

    # base_dir = os.mkdir(name)
    path = name+'/'+name
    os.makedirs(path, exist_ok=False)

    os.mknod(path+"/__init__.py")
    os.mknod(path+"/core.py")
    os.mknod(path+"/helpers.py")
    return MetaFiles(name)


def MetaFiles(name):
    os.mknod(name+"/__init__.py")
    os.mknod(name+"/.gitignore")
    os.mknod(name+"/LICENSE")
    os.mknod(name+"/MANIFEST.in")
    os.mknod(name+"/Makefile")
    os.mknod(name+"/README.rst")
    os.mknod(name+"/requirements.txt")
    os.mknod(name+"/setup.py")
    return Tests(name)


def Tests(name):
    test_dir = name+"/tests"
    os.makedirs(test_dir, exist_ok=False)
    os.mknod(test_dir+"/__init__.py")
    os.mknod(test_dir+"/context.py")
    os.mknod(test_dir+"/test_advanced.py")
    os.mknod(test_dir+"/test_basic.py")
    return Docs(name)


def Docs(name):
    docs_dir = name+"/docs"
    os.makedirs(docs_dir, exist_ok=False)
    os.mknod(docs_dir+"/__init__.py")
    os.mknod(docs_dir+"/Makefile")
    os.mknod(docs_dir+"/conf.py")
    os.mknod(docs_dir+"/index.rst")
    os.mknod(docs_dir+"/make.bat")
    return root(name)

from treelib import Node, Tree
def root(name):
    print("Your Project Structure")    
    os.system('tree '+name)

if "__main__" == __name__:
    sys.tracebacklimit = 0
    sys.excepthook = IPython.core.ultratb.ColorTB()
    FileExists()
    cli()

    
    