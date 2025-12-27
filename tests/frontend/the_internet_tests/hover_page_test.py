import pytest

from pages.the_internet_app.hover_page import HoverPage
from pages.the_internet_app.user_profile_page import UserProfilePage
from src.config.config_reader import ConfigReader

BASE_URL = f"{ConfigReader.get_base_url()}/hovers"


@pytest.mark.parametrize(
    "user_id, expected_user_name",
    [
        (1, "user1"),
        (2, "user2"),
        (3, "user3")
    ]
)
def test_hover(browser, user_id, expected_user_name):
    hover_page = HoverPage(browser)
    user_page = UserProfilePage(browser)

    browser.get(BASE_URL)
    hover_page.wait_for_open()

    hover_page.hover_profile(user_id)
    actual_user_name = hover_page.get_user_name(user_id)
    assert expected_user_name in actual_user_name, (
        f"Ожидалось [{expected_user_name}] в [{actual_user_name}]\n"
    )

    expected_profile_link = hover_page.get_profile_link(user_id)
    hover_page.click_profile_button(user_id)

    user_page.wait_for_open()
    actual_url = browser.get_url()
    assert expected_profile_link in actual_url, (
        f"Ожидалось [{expected_profile_link}] в [{actual_url}]\n"
    )

    browser.back()
    hover_page.wait_for_open()