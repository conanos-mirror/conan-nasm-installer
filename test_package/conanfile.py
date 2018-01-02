from conans.model.conan_file import ConanFile
import os

class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "arch"

    def test(self):
        self.run("nasm --version")
        assert os.path.exists(os.path.join(self.deps_cpp_info["nasm"].rootpath, "LICENSE"))
