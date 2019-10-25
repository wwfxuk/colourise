# -*- coding: utf-8 -*-

name = 'colourise'

version = '0.3.0'

description = (
    'If output to Terminal, colourise the piped input '
    'text base off some rules.'
)

authors = ['WWFX UK']

# Technically needs bash. Tested rez on Linux and OSX CI with bash
requires = ['platform-linux|osx']

tools = ['colourise', 'colour-test']  # Names of executables from this package
# ---- OR ----
# @late()
# def tools():
#     """Dynamically get a list of binaries/wrappers from our bin folder.
#
#     Returns:
#         list[str]: Names of binaries from the bin folder.
#     """
#     import os
#     exe_names = []
#
#     for name in os.listdir(this.root):
#         full_path = os.path.join(this.root, name)
#         if os.access(full_path, os.X_OK) and not os.path.isdir(full_path):
#             exe_names.append(name)
#
#     return exe_names

# # Technically needs tar, gzip and curl but they tend to come with OS
# build_requires = []  # Build-time packages required by this package

# To Do: Fails on Windows, rez will run build_command with cmd
build_command = r'''
set -euf -o pipefail

if [[ $REZ_BUILD_INSTALL -eq 1 ]]
then
    cp -v \
        $REZ_BUILD_SOURCE_PATH/colourise \
        $REZ_BUILD_SOURCE_PATH/colour-test \
        $REZ_BUILD_INSTALL_PATH
fi
'''


def commands():
    """Commands to set up environment for ``rez env colourise``"""
    env.PATH.append('{root}')
