import pytest
import sys

from rest_api.app import throw_exception, ExpectedError


def test_throw_exception():
    with pytest.raises(ExpectedError):
        throw_exception()