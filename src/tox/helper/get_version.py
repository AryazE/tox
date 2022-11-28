import json
import os
import platform
import sys

info = {
    "executable": sys.executable,
    "implementation": platform.python_implementation(),
    "version_info": list(sys.version_info),
    "version": sys.version,
    "is_64": sys.maxsize > 2**32,
    "sysplatform": sys.platform,
    "os_sep": os.sep,
    "extra_version_info": getattr(sys, "pypy_version_info", None),
}
info_as_dump = json.dumps(info)
print(info_as_dump)
