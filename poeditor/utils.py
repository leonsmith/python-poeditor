from datetime import datetime


def parse_datetime(dt_string):
    return datetime.strptime(dt_string, "%Y-%m-%dT%H:%M:%S%z")
