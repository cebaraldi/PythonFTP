import ftputil
import os

from ftputil.error import FTPOSError, PermanentError

USER = "anonymous"
PASS = "guest"
SERVER = "opendata.dwd.de"
LOCAL = "/media/datalake/"
REMOTE = "climate_environment/CDC/observations_germany/climate/daily/kl"

REC = "recent"
if not os.path.exists(REC):
    os.mkdir(REC)
HIST = "historical"
if not os.path.exists(HIST):
    os.mkdir(HIST)
try:
    with ftputil.FTPHost(SERVER, USER, PASS) as host:
        host.chdir(REMOTE)

        host.chdir(REC)
        os.chdir(REC)
        files = host.listdir(host.curdir)[0:11]
        for f in files:
            host.download_if_newer(f, f)
            print(f)

        host.chdir("../historical")
        os.chdir(f"../{HIST}")
        files = host.listdir(host.curdir)[22:33]
        for f in files:
            host.download_if_newer(f, f)
            print(f)
except FTPOSError as e:
    print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
except PermanentError as e:
    print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
except Exception as e:
    print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")