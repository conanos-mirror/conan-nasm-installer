import os

from conans import ConanFile
from conans.client import tools
from conans import __version__ as conan_version
from conans.model.version import Version


class NasmConan(ConanFile):
    name = "nasm"
    version = "2.13.01"
    license = "BSD-2-Clause"
    url = "https://github.com/lasote/conan-nasm-installer"
    if conan_version < Version("1.0.0"):
        settings = "os"
    else:
        settings = "os_build"
    build_policy = "missing"
    description="Nasm for windows. Useful as a build_require."
    
    def configure(self):
        if self.os != "Windows":
            raise Exception("Only windows supported for nasm")

    @property
    def os(self):
        return self.settings.get_safe("os_build") or self.settings.get_safe("os")

    @property
    def nasm_folder_name(self):
        return "nasm-%s" % self.version

    def build(self):
        def get_version(suffix):
            nasm_zip_name = "%s-%s.zip" % (self.nasm_folder_name, suffix)
            tools.download("http://www.nasm.us/pub/nasm/releasebuilds/"
                           "%s/%s/%s" % (self.version, suffix, nasm_zip_name), nasm_zip_name)
            self.output.warn("Downloading nasm: "
                             "http://www.nasm.us/pub/nasm/releasebuilds"
                             "/%s/%s/%s" % (self.version, suffix, nasm_zip_name))
            tools.unzip(nasm_zip_name)
            os.unlink(nasm_zip_name)
        os.mkdir("x86")
        with tools.chdir("x86"):
            get_version("win32")
            
        os.mkdir("x86_64")
        with tools.chdir("x86_64"):
            get_version("win64")

    def package(self):
        self.copy("*", dst="", keep_path=True)
        self.copy("license*", dst="", src=os.path.join(tools.detected_architecture(),
                                                       self.nasm_folder_name),
                  keep_path=False, ignore_case=True)

    def package_info(self):
        self.output.info("Using %s version" % tools.detected_architecture())
        self.env_info.path.append(os.path.join(self.package_folder, tools.detected_architecture(),
                                               self.nasm_folder_name))
