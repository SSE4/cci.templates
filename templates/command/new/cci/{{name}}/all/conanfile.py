import os
from conans import ConanFile, tools


required_conan_version = ">=1.37.0"

class {{package_name}}Conan(ConanFile):
    name = "{{ name }}"
    license = ""
    url = "https://github.com/conan-io/conan-center-index"
    homepage = ""
    description = ""
    topics = ("conan",)
    no_copy_source = True

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version], strip_root=True, destination=self._source_subfolder)

    def package(self):
        self.copy("COPYING", dst="licenses", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
