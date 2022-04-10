__all__ = ["POEditorException", "POEditorArgsException"]


class POEditorException(Exception):
    """
    POEditor API exception
    """

    def __init__(self, error_code, status, message):
        self.exp = "POEditorException"
        self.error_code = error_code
        self.message = "Status '{}', code {}: {}".format(status, error_code, message)

    def __str__(self):
        return self.message


class POEditorArgsException(Exception):
    """
    POEditor args method exception
    """

    def __init__(self, message):
        self.exp = "POEditorArgsException"
        self.message = message
