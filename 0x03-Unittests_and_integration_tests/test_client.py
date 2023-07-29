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
        (
            "google",
            {
                "url": "https://api.github.com/orgs/google",
                "repos_url": "https://api.github.com/orgs/google/repos",
            },
            "https://api.github.com/orgs/google/repos"
        ),
        (
            "abc",
            {
                "message": "Not Found",
                "documentation_url":
                "https://docs.github.com/rest/orgs/orgs#get-an-organization"
            },
            KeyError
        )
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

    @parameterized.expand([
        ("google", TEST_PAYLOAD[0][1],
         "https://api.github.com/orgs/google/repos", 'bsd-3-clause'),
        ("google", TEST_PAYLOAD[0][1],
         "https://api.github.com/orgs/google/repos", 'apache-2.0'),
        ("google", TEST_PAYLOAD[0][1],
         "https://api.github.com/orgs/google/repos", ''),
        ("google", TEST_PAYLOAD[0][1],
         "https://api.github.com/orgs/google/repos", None),
        # ("abc")
    ])
    @patch('client.get_json')
    def test_public_repos(self, org_name: str, get_json_return_val: list,
                          _public_repos_url_result: str, license: str,
                          mock_get_json: MagicMock):
        """TODO: """
        New_org = GithubOrgClient(org_name)
        mock_get_json.return_value = get_json_return_val
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url_fn:
            mock_public_repos_url_fn.return_value = _public_repos_url_result
            # test when license exists
            expected_result = [
                repo["name"] for repo in get_json_return_val
                if license is None or (repo['license'] and
                                       repo['license']['key'] == license)
            ]
            result = New_org.public_repos(license)
            self.assertEqual(expected_result, result)
            mock_public_repos_url_fn.assert_called_once()
            mock_get_json.assert_called_once()
