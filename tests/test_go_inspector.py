# -*- coding: utf-8 -*-
#
# Copyright (c) nexB Inc. and others. All rights reserved.
# ScanCode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/scancode-plugins for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

import json
import os

import pytest

from src.go_inspector.plugin import collect_and_parse_symbols

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def test_goresym_with_windows_exe():
    go_binary = os.path.join(TEST_DATA_DIR, "windows.exe")
    with pytest.raises(Exception) as e:
        collect_and_parse_symbols(go_binary)


def test_goresym_with_elf():
    go_binary = os.path.join(TEST_DATA_DIR, "arm_gentoo_elf")
    with pytest.raises(Exception) as e:
        collect_and_parse_symbols(go_binary)


@pytest.mark.parametrize(
    "path",
    [
        "app_lin_exe",
        "app_mac_exe",
        "app_win_exe",
    ],
)
def test_goresym_with_mini_go_app_linux(path):
    go_binary = os.path.join(TEST_DATA_DIR, path)
    goresym_output = collect_and_parse_symbols(go_binary)
    with open(os.path.join(TEST_DATA_DIR, f"gore_sym_{path}_output.json")) as f:
        expected_output = json.load(f)
        assert expected_output == goresym_output
