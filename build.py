from conan.packager import ConanMultiPackager
from conans import __version__ as conan_version
from conans.model.version import Version


if __name__ == "__main__":
    builder = ConanMultiPackager()
    if conan_version < Version("0.99"):
        builder.add({"os": "Windows", "arch": "x86"}, {}, {}, {})
        builder.add({"os": "Windows", "arch": "x86_64"}, {}, {}, {})
    else:
        builder.add({"os_build": "Windows", "arch_build": "x86"}, {}, {}, {})
        builder.add({"os_build": "Windows", "arch_build": "x86_64"}, {}, {}, {})

    builder.run()
