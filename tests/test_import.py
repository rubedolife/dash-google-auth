"""
Test Dash Google Auth.
"""

import pytest

from dash_google_auth import GoogleOAuth

from dash import Dash
from flask import Flask


@pytest.fixture
def app(name='dask'):
    """Dash App."""

    return Dash(name, server=Flask(name),
                url_base_pathname='/', auth='auth')


def test_init(app):
    """Test initialisation."""

    authorized_emails = ['joshbode@fastmail.com']
    authorized_domains = []
    auth = GoogleOAuth(app, authorized_emails, authorized_domains)

    assert auth.app is app
    assert auth.authorized_emails == authorized_emails
    assert auth.authorized_domains == authorized_domains
