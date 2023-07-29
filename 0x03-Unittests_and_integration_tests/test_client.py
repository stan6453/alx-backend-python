#!/usr/bin/env python3
"""Tests for clients.py"""

import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Union,
    Dict,
    Callable,
)
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ("google",
         {
             "url": "https://api.github.com/orgs/google",
             "repos_url": "https://api.github.com/orgs/google/repos",
         }, "https://api.github.com/orgs/google/repos"),
        ("abc", {
            "message": "Not Found",
            "documentation_url":
            "https://docs.github.com/rest/orgs/orgs#get-an-organization"
        }, KeyError)
    ])
    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, org_name: str, org_fun_result: Mapping,
                              _public_repos_url_result,
                              mock_org_fn: MagicMock):
        """TODO: """
        New_org = GithubOrgClient(org_name)
        mock_org_fn.return_value = org_fun_result
        if type(_public_repos_url_result) is str:
            return_value = New_org._public_repos_url
            self.assertEqual(return_value, _public_repos_url_result)
        else:
            with self.assertRaises(KeyError):
                return_value = New_org._public_repos_url
