"""
    API Client Interface for POEditor API (https://poeditor.com).

    Usage:

    >>> from poeditor import Client
    >>> client = Client(api_token='my_token')
    >>> projects = client.list_projects()
"""

__version__ = "1.1.2"

try:
    from .client import Client
    from .exceptions import POEditorArgsException, POEditorException
except ImportError:
    pass
