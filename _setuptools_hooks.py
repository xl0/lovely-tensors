import os

from setuptools.command.install_lib import install_lib


LOVELY_TENSORS_PTH = "_lovely_tensors_hook.pth"
LOVELY_TENSORS_PY = "_lovely_tensors_hook.py"


class InstallLibWithHook(install_lib):
    def run(self):
        super().run()
        outputs = []
        for filename in (LOVELY_TENSORS_PTH, LOVELY_TENSORS_PY):
            source = os.path.join(os.path.dirname(__file__), filename)
            destination = os.path.join(self.install_dir, filename)
            self.copy_file(source, destination)
            outputs.append(destination)
        self.outputs = outputs

    def get_outputs(self):
        return [*super().get_outputs(), *getattr(self, "outputs", [])]
