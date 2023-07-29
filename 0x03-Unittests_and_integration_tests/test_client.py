#!/usr/bin/env python3
"""Tests for clients.py"""

import unittest
from unittest.mock import patch, MagicMock
from client import GithubOrgClient
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestGithubOrgClient(unittest.TestCase):
    """TODO: """

    ORG_URL = "https://api.github.com/orgs/{org}"

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: MagicMock):
        """TODO: """
        New_org = GithubOrgClient(org_name)
        New_org.org()

        mock_get_json.assert_called_once_with(
            self.ORG_URL.format(org=org_name))
