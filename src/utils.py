import os


def get_data_path(filename):
    """Return the full path for a data file in the data folder"""
    base_path = os.path.dirname(os.path.dirname(__file__))  # Go up one directory
    return os.path.join(base_path, "data", filename)
