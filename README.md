# templates for Conan Center Index

The collection of useful [templates](https://docs.conan.io/en/latest/extending/template_system/command_new.html#template-command-new) for [conan new](https://docs.conan.io/en/latest/reference/commands/creator/new.html) command.
The templates are mainly useful for [Conan Center Index](https://github.com/conan-io/conan-center-index) package creators.

## installation

use [conan config install](https://docs.conan.io/en/latest/reference/commands/consumer/config.html#conan-config-install) command:

```
$ conan config install https://github.com/SSE4/cci.templates.git -sf templates -tf templates
```

## usage

mostly, templates are used in conjunction with [cci.new](https://github.com/SSE4/cci.new) utility.
however, they could be used on its own:

```
$ conan new zip/0.1.30 -m cci.cmake -d license=Unlicense
```

## available templates

- [header-only](templates/command/new/cci)
- [CMake](templates/command/new/cci.cmake)

## TODO

there are several frequently encountered patterns (e.g. build system types) which we would like to have templates for:

- [AutoTools](https://www.gnu.org/savannah-checkouts/gnu/autoconf/manual/autoconf-2.70/autoconf.html#The-GNU-Build-System)
- [MSBuild](https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild?view=vs-2019)
- [Meson](https://mesonbuild.com/)
