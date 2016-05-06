# Varsity

Varsity helps you define your application's settings, read them from environment
variables, parse them into native Python types, and validate them.

## Load a simple string

Assume the FOO environment variable as been set to '3'.  Here we define a
loader, use it to give our 'foo' setting a name, and tie it to the 'FOO'
environment variable.  We get back a dictionary with a key for each setting
we've added to the loader.

    >>> from varsity import Loader
    >>> 
    >>> l = Loader()
    >>> l.add('foo', 'FOO')
    >>> settings = l.load()
    >>> settings['foo']
    '3'

The object returned from .load() also provides attribute-style access to
settings.

    >>> settings.foo
    '3'

You can provide a 'typ' callable that will be used to convert the environment
variable string into the type of your choice.

    >>> l.add('foo', 'FOO', typ=int)
    >>> settings = l.load()
    >>> settings.foo
    3

You can provide defaults that will be returned if the environment variable is
not present.

    >>> l.add('some_unset_var', 'SOME_UNSET_VAR', default=0)
    >>> settings = l.load()
    >>> settings.some_unset_var
    0

If you don't provide a default, and the environment variable is not set,
ValueError will be raised.

You can provide your own callable as the 'typ' argument.  Assume the 'TODAY'
environment variable is set to '2016-05-05'.

    >>> from varsity import Loader
    >>> from iso8601 import parse_date
    >>> l = Loader()
    >>> l.add('today', 'TODAY', typ=lambda x: parse_date(x).date())
    >>> settings = l.load()
    >>> settings.today
    datetime.date(2016, 5, 5)

If you don't provide a 'typ', but you do provide a default, then the environment
variable will be cast to the same type as the default.  (Here we get back an
int 3 instead of the string '3', because the default is an int.)

    >>> l.add('foo', 'FOO', default=0)
    >>> settings = l.load()
    >>> settings.foo
    3

If you access a setting with the attribute-style syntax, then nested
dictionaries can also be accessed with that syntax.  In this example, the FOO
environment variable is set to '{"bar": {"baz": 1.23}}'

    >>> l.add('foo', 'FOO', typ=json.loads)
    >>> settings = l.load()
    >>> settings.foo.bar.baz
    1.23

