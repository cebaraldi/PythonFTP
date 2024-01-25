import ftputil
import os

from ftputil.error import FTPOSError, PermanentError

USER = "anonymous"
PASS = "guest"
SERVER = "ftp.ncdc.noaa.gov"
LOCAL = "/media/datalake/"
REMOTE = "pub/data/ghcn/daily/by_year"

DATA = "ncdc" # LOCAL
if not os.path.exists(DATA):
    os.mkdir(DATA)

try:
    with ftputil.FTPHost(SERVER, USER, PASS) as host:
        host.chdir(REMOTE)

        os.chdir(DATA)
        files = host.listdir(host.curdir)[0:11]
        for f in files:
            host.download_if_newer(f, f)
            print(f)
except FTPOSError as e:
    print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
except PermanentError as e:
    print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
except Exception as e:
    print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")