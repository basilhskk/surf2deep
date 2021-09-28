import subprocess
import os
import tempfile
import shutil
from pathlib import Path

def isServiceStatus(name:str,system:str)->bool:
    """
    Finds if service is running (parsing depending the system).
    :return: True,False
    """

    if system ==None:
        raise  OSError("Must run in wsl or unix like system")
        
    uname = subprocess.Popen(["service", name, "status"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    result = uname.stdout.read().decode().rstrip("\n")
    err = uname.stderr.read().decode()

    if err:
        Exception("Service error")

    if system == "wsl":
        if "tor is running" in result:
            return True
        else:
            raise SystemError("Tor service is not running.")
    else:
        if "Active: active" in result:
            return True
        else:
            raise SystemError("Tor service is not running.")


def findSystem()->str:
    """
    Finds system info from uname command.
    :return: wsl,linux,None
    """

    uname = subprocess.Popen(["uname","-a"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    result = uname.stdout.read().decode().rstrip("\n")
    err = uname.stderr.read().decode()

    if err:
        raise OSError("Not in unix like environment")

    if ("Microsoft" in result or "WSL" in result):
        return "wsl"
    elif "Linux" in result:
        return "linux"
    else:
        return None


def getTempDir()->str:
    """
    :return: temporary directory path
    """

    return tempfile.gettempdir()


def createTempDir(directory:str)->str:
    """
    Create a directory in temp directory 
    :return: created directory in tmp 
    """
    
    try:
        path = os.path.join(directory,"surf2deep")
        if os.path.exists(path):
            return path
        else:
            os.mkdir(path)
            return path
    except:
        return False


def createFoldersFromPath(tmp,path):
    path = os.path.join(tmp,path)
    Path(path).mkdir(parents=True, exist_ok=True)
    return path


def joinPaths(path1,path2):
    return os.path.join(path1,path2)

def fileExists(path):
    return os.path.exists(path)