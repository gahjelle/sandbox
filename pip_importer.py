from importlib.abc import MetaPathFinder
from importlib import util
import subprocess
import sys

class PipFinder(MetaPathFinder):
    @staticmethod
    def find_spec(fullname, path, target=None):
        print(f"Module {fullname!r} not installed.  Attempting to pip install")
        cmd = f"{sys.executable} -m pip install {fullname}"
        try:
            subprocess.run(cmd.split(), check=True)
        except subprocess.CalledProcessError:
            return None

        return util.find_spec(fullname)

sys.meta_path.append(PipFinder)
