import os
import platform

class Install:
    def __init__(self):
        if platform.system().lower().startswith('win'):
            self.pip = "pip"
            self.python = "python"
            self.clear_s = "cls"
        else:
            self.pip = "pip3"
            self.python = "python3"
            self.clear_s = "clear"

    def _pip_install(self, module_name: str, clear: bool = False):
        if clear:
            os.system(self.clear_s)
        os.system(f"{self.pip} install {module_name}")

    def install_all(self, clear_screen: bool = True):
        _all_module_names = [
            ""
        ]
        if len(_all_module_names) == 0:
            print("- Something is wrong in emailspammer.utils: No modules are given to install!")
            return
        for _module_name in _all_module_names:
            self._pip_install(_module_name, clear=clear_screen)

        



