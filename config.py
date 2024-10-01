"""
Configuration for Codeforces submission.
Author: @asibhossen897
Date: 2024-10-01
"""

LANGUAGES = {
    "C++ 17": "54",
    "Python 3.10": "70",
    "Java 21": "87",  # Java 21 64bit
    "C": "31",  # GNU GCC C11 5.1.0
    "C# 10": "79",  # C# 10, .NET SDK 6.0
    "Ruby 3.2.2": "67",  # Ruby 3.2.2
    "Bash": "114",  # Bash
    "Kotlin 1.9.21": "88",  # Kotlin 1.9.21
    "GNU GCC C11 5.1.0": "43",
    "GNU G++20 13.2 (64 bit, winlibs)": "89",
    "GNU G++23 14.2 (64 bit, msys2)": "91",
    "C# 8": "65",  # C# 8, .NET Core 3.1
    "C# Mono 6.8": "9",
    "D DMD32 v2.105.0": "28",
    "Go 1.22.2": "32",
    "Haskell GHC 8.10.1": "12",
    "Java 8 32bit": "36",
    "Kotlin 1.7.20": "83",
    "OCaml 4.02.1": "19",
    "Delphi 7": "3",
    "Free Pascal 3.2.2": "4",
    "PascalABC.NET 3.8.3": "51",
    "Perl 5.20.1": "13",
    "PHP 8.1.7": "6",
    "Python 2.7.18": "7",
    "Python 3.8.10": "31",
    "PyPy 2.7.13 (7.3.0)": "40",
    "PyPy 3.6.9 (7.3.0)": "41",
    "PyPy 3.10 (7.3.15, 64bit)": "70",
    "Rust 1.75.0 (2021)": "75",
    "Scala 2.12.8": "20",
    "JavaScript V8 4.8.0": "34",
    "Node.js 15.8.0 (64bit)": "55",
}

LANGUAGE_IDS = {int(v): k for k, v in LANGUAGES.items()}

# Contest configuration
CONTEST_ID = "1916"
CONTEST_PROBLEM_INDEX = "A"
CONTEST_URL = (
    f"https://codeforces.com/contest/{CONTEST_ID}/problem/{CONTEST_PROBLEM_INDEX}"
)

# Problem set configuration
PROBLEM_SET_ID = "4"
PROBLEM_SET_INDEX = "A"
PROBLEM_SET_URL = (
    f"https://codeforces.com/problemset/problem/{PROBLEM_SET_ID}/{PROBLEM_SET_INDEX}"
)

# Default language for submission
DEFAULT_LANGUAGE_ID = "54"  # C++ 17

# Codeforces URLs
LOGIN_URL = "https://codeforces.com/enter"
