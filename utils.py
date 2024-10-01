"""
Utility functions for Codeforces submission.
Author: @asibhossen897
Date: 2024-10-01
"""

import os


def get_solution_file_path(filename):
    dir_name = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir_name, f"solutions/{filename}")
