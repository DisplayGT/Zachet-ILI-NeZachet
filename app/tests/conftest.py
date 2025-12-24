import sys
from pathlib import Path
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.models.tables import db
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "LOGIN_DISABLED": True
    })

    with app.app_context():
        db.create_all()
        yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()