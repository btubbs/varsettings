import json
from decimal import Decimal

import pytest

from varsity import Loader


def test_simple_var():
    l = Loader()
    l.add('foo', 'FOO')
    settings = l.load(environ={'FOO': 'bar'})
    assert settings.foo == 'bar'


def test_default():
    l = Loader()
    l.add('foo', 'FOO', default='bar')
    settings = l.load(environ={})
    assert settings.foo == 'bar'


def test_default_type():
    l = Loader()
    l.add('foo', 'FOO', default=0)
    settings = l.load(environ={'FOO': '3'})
    assert settings.foo == 3


def test_explicit_type():
    l = Loader()
    l.add('foo', 'FOO', typ=Decimal)
    settings = l.load(environ={'FOO': '3.0'})
    assert settings.foo == Decimal(3.0)


def test_var_or_default_required():
    l = Loader()
    l.add('foo', 'FOO')
    with pytest.raises(ValueError):
        l.load(environ={})


def test_nested_attributes():
    l = Loader()
    l.add('foo', 'FOO', typ=json.loads)
    settings = l.load(environ={'FOO': '{"bar": 2}'})
    assert settings.foo.bar == 2
