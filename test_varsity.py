# Run these with py.test

import json
from decimal import Decimal

import pytest

from varsity import Loader


def test_simple_var():
    l = Loader()
    l.add('FOO')
    settings = l.load(environ={'FOO': 'bar'})
    assert settings.FOO == 'bar'


def test_simple_var_with_name():
    l = Loader()
    l.add('FOO', 'foo')
    settings = l.load(environ={'FOO': 'bar'})
    assert settings.foo == 'bar'


def test_default():
    l = Loader()
    l.add('FOO', 'foo', default='bar')
    settings = l.load(environ={})
    assert settings.foo == 'bar'


def test_default_type():
    l = Loader()
    l.add('FOO', 'foo', default=0)
    settings = l.load(environ={'FOO': '3'})
    assert settings.foo == 3


def test_explicit_type():
    l = Loader()
    l.add('FOO', 'foo', typ=Decimal)
    settings = l.load(environ={'FOO': '3.0'})
    assert settings.foo == Decimal(3.0)


def test_var_or_default_required():
    l = Loader()
    l.add('FOO')
    with pytest.raises(ValueError):
        l.load(environ={})


def test_nested_attributes():
    l = Loader()
    l.add('FOO', 'foo', typ=json.loads)
    settings = l.load(environ={'FOO': '{"bar": 2}'})
    assert settings.foo.bar == 2
