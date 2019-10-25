# -*- coding: utf-8 -*-

name = 'colourise'

version = '0.2.0'

description = (
    'If output to Terminal, colourise the piped input '
    'text base off some rules.'
)

authors = ['WWFX UK']

requires = ['platform-linux|osx']  # As tested by CI

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
#     bin_folder = os.path.join(this.root, 'bin')
#
#     for name in os.listdir(bin_folder):
#         full_path = os.path.join(bin_folder, name)
#         if os.access(full_path, os.X_OK) and not os.path.isdir(full_path):
#             exe_names.append(name)
#
#     return exe_names

# # Technically needs tar, gzip and curl but they tend to come with OS
# build_requires = []  # Build-time packages required by this package

build_command = r'''
set -euf -o pipefail

# ---- Setup for: curl $CURL_FLAGS ... ----
# Silent/no progress bar curl if not terminal (e.g. CI stdout or file logs)
[ -t 1 ] && CURL_FLAGS="-#" || CURL_FLAGS="-sS"
CURL_FLAGS+=" -L"

if [[ $REZ_BUILD_INSTALL -eq 1 ]]
then
    curl $CURL_FLAGS \
        https://github.com/wwfxuk/colourise/archive/{version}.tar.gz \
    | tar -C "$REZ_BUILD_INSTALL_PATH" --strip-components=1 -xz \
        colourise \
        colour-test
fi
'''.format(version=version)


def commands():
    """Commands to set up environment for ``rez env colourise``"""
    env.PATH.append('{root}')
