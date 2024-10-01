"""
Codeforces Submission Tool
Author: @asibhossen897
Date: 2024-10-01
A script that uses SeleniumBase's BaseCase for Codeforces login and submission.
"""

from seleniumbase import BaseCase
from seleniumbase.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
from config import LANGUAGES, PROBLEM_SET_URL, DEFAULT_LANGUAGE_ID, LOGIN_URL
from utils import get_solution_file_path

load_dotenv()

BaseCase.main(__name__, __file__, "--uc", "--headed", "-s")


class CodeforceSubmit(BaseCase):
    def setUp(self):
        super().setUp()
        self.username = os.getenv("CODEFORCES_USERNAME")
        self.password = os.getenv("CODEFORCES_PASSWORD")

    def login(self):
        self.uc_open_with_reconnect(LOGIN_URL, 4)
        self.wait_for_element("#handleOrEmail")
        self.type("#handleOrEmail", self.username)
        self.type("#password", self.password)
        self.click('input[type="submit"]')
        self.wait_for_element(f"a[href='/profile/{self.username}']")

    def submit_solution(self):
        self.uc_open_with_reconnect(PROBLEM_SET_URL, 4)
        self.wait_for_element_visible("form.submitForm")

        source_file_path = get_solution_file_path("main.cpp")

        self.click(
            f'select[name="programTypeId"] option[value="{DEFAULT_LANGUAGE_ID}"]'
        )
        self.choose_file('input[type="file"]', source_file_path)
        self.click('input.submit[type="submit"]')

        if self.is_element_visible("span.error.for__sourceFile"):
            error_message = self.get_text("span.error.for__sourceFile")
            print(f"Error: {error_message}")
            return

        self.wait_for_and_check_result()

    def wait_for_and_check_result(self):
        result_table = "table.status-frame-datatable"
        self.wait_for_element_visible(result_table, timeout=20)

        submission_tag = f"{result_table} tr:nth-child(2) td:nth-child(1) a.view-source"
        submission_link = self.get_attribute(submission_tag, "href")

        result = self.get_text(f"{result_table} tr:nth-child(2) td:nth-child(6)")
        if "Running" in result:
            self.sleep(20)
            print(f"Submission result: {result}")
            print(f"Submission link: {submission_link}")
        else:
            print(f"Submission result: {result}")
            print(f"Submission link: {submission_link}")

    def test_submit_solution(self):
        self.login()
        self.submit_solution()
