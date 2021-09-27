import subprocess
import os

def isServiceStatus(name,system):
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


def findSystem():
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

