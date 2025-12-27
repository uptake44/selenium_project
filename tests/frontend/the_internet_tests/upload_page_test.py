import os

import pytest

from pages.the_internet_app.upload_page import UploadPage
from pages.the_internet_app.uploaded_file_page import UploadedFilePage
from src.config.config_reader import ConfigReader

BASE_URL = f"{ConfigReader.get_base_url()}/upload"
DEFAULT_PATH = f"{os.getcwd()}{os.sep}screenshots{os.sep}"


@pytest.mark.parametrize(
    "path, file_name, expected_status",
    [
        (
                DEFAULT_PATH,
                "1.xml",
                "File Uploaded!"
        )
    ]
)
def test_direct_upload(browser, path, file_name, expected_status):
    upload_page = UploadPage(browser)
    uploaded_file_page = UploadedFilePage(browser)
    browser.get(BASE_URL)
    assert upload_page.wait_for_open(), "Страница не открылась"

    upload_page.direct_upload(
        file_name=file_name,
        path=path,
    )

    uploaded_file_page.wait_for_open()

    actual_status = uploaded_file_page.get_status()
    assert actual_status == expected_status, (
        f"Ожидалось: {expected_status}\n"
        f"Получено: {actual_status}\n"
    )

    actual_file_name = uploaded_file_page.get_file_name()
    assert actual_file_name == file_name, (
        f"Ожидалось: {file_name}\n"
        f"Получено: {actual_file_name}\n"
    )


@pytest.mark.parametrize(
    "path, file_name",
    [
        (DEFAULT_PATH, "1.xml")
    ]
)
def test_dialog_window_upload(browser, path, file_name):
    upload_page = UploadPage(browser)
    browser.get(BASE_URL)
    upload_page.wait_for_open()

    upload_page.dialog_window_upload(path=path, file_name=file_name)

    actual_file_name = upload_page.get_uploaded_file_name()
    assert actual_file_name == file_name, (
        f"Ожидалось: {file_name}\n"
        f"Получено: {actual_file_name}\n"
    )

    upload_page.wait_for_check_mark()
