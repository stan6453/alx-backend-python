#!/usr/bin/env python3
"""Tests for utils.py"""

import unittest
from unittest.mock import patch, MagicMock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """Test for utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected_result: Mapping) -> None:
        """Test if right output is returned"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected_result: str) -> None:
        """Test if right errors are raised"""
        with self.assertRaises(KeyError, msg=expected_result):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test for utils.get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("requests.get")
    def test_get_json(self, test_url: str,
                      test_payload: Dict, mock_get: MagicMock) -> None:
        """Mock get network request"""
        get_return_value = MagicMock()
        get_return_value.json.return_value = test_payload
        mock_get.return_value = get_return_value

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """TODO: """

    def test_memoize(self):
        """TODO: """

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Mock the a_method
        with patch.object(TestClass, 'a_method') as mocked_method:
            test_obj = TestClass()
            # Set the return value of the mocked a_method
            mocked_method.return_value = 42

            # Call the a_property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            # Assert that the a_method was called only once
            mocked_method.assert_called_once()

            # Assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
