#!/usr/bin/env python3
import os
import pytest
import socket
import shutil
import pathlib
from typing import List, Dict

import mmpm.mmpm
import mmpm.core
import mmpm.utils
import mmpm.consts
import mmpm.color
import mmpm.models

MagicMirrorPackage: mmpm.models.MagicMirrorPackage = mmpm.models.MagicMirrorPackage
get_env = mmpm.utils.get_env

MAGICMIRROR_ROOT: str = get_env(mmpm.consts.MMPM_MAGICMIRROR_ROOT_ENV)

VALID_PACKAGES: List[MagicMirrorPackage] = [
    MagicMirrorPackage(
        title='MMM-COVID19',
        author='bibaldo',
        repository='https://github.com/bibaldo/MMM-COVID19',
        description='Keep track of Corona Virus (COVID-19) cases via rapidapi API'
    ),
    MagicMirrorPackage(
        title='MagicMirror-Module-Template',
        author='MichMich',
        repository='https://github.com/roramirez/MagicMirror-Module-Template',
        description='Module to help developers to start building their own modules for the MagicMirror.'
    )
]


INVALID_PACKAGES: List[MagicMirrorPackage] = [
    MagicMirrorPackage(
        title='ThisPackageNameBetterNotExistOtherwiseItWouldExtremelyWeird',
        author='bsdfasadfasdfa',
        repository='this_isnt_a_valid_url',
        description='This description does not matter at all'
    ),
    MagicMirrorPackage(
        title='ThisPackageNameBetterNotExistOtherwiseItWouldExtremelyWeirdAlso',
        author='asdfasdfasdfasdfas',
        repository='this_also_isnt_a_valid_url',
        description='This description does not matter at all'
    )
]


def test_internet_connection():
    assert socket.create_connection(
        ('1.1.1.1', 80)) and socket.create_connection(('1.1.1.1', 443))


def test_module_file_exists():
    assert os.path.exists(mmpm.consts.MMPM_CLI_LOG_FILE)


def test_module_dir_exists():
    assert os.path.exists(os.path.join(MAGICMIRROR_ROOT, 'modules'))


def test_magic_mirror_installation_found():
    assert os.path.exists(MAGICMIRROR_ROOT)


def test_retrieve_packages():
    assert len(mmpm.core.load_packages()) > 0


def test_search_packages_with_valid_query():
    assert mmpm.core.search_packages(mmpm.core.load_packages(), 'face')


def test_install_package():
    for pkg in VALID_PACKAGES:
        assert mmpm.core.install_package(pkg)
