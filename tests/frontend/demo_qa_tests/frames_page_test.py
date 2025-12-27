import pytest

from pages.demo_qa.frames_page import FramesPage
from pages.demo_qa.nested_frames_page import NestedFramesPage

BASE_URL = "https://demoqa.com/frames"


@pytest.mark.parametrize(
    "exp_parent_text, exp_child_text",
    [
        ("Parent frame", "Child Iframe")
    ]
)
def test_nested_frames(browser, exp_parent_text, exp_child_text):
    frames_page = FramesPage(browser)
    nested_frames_page = NestedFramesPage(browser)
    browser.get(BASE_URL)
    frames_page.wait_for_open()

    frames_page.click_nested_frames()

    actual_parent_frame_text = nested_frames_page.get_parent_frame_text()
    assert actual_parent_frame_text == exp_parent_text, (
        f"Ожидалось: {exp_parent_text}\n"
        f"Получено: {actual_parent_frame_text}"
    )

    actual_child_frame_text = nested_frames_page.get_child_frame_text()
    assert actual_child_frame_text == exp_child_text, (
        f"Ожидалось: {exp_child_text}\n"
        f"Получено: {actual_child_frame_text}"
    )


def test_sample_frames(browser):
    frames_page = FramesPage(browser)
    browser.get(BASE_URL)
    frames_page.wait_for_open()

    frames_page.click_sample_frames()

    first_frame_text = frames_page.get_first_frame_text()
    second_frame_text = frames_page.get_second_frame_text()

    assert first_frame_text == second_frame_text, (
        f"Текст не совпадает:\n"
        f"{first_frame_text} | {second_frame_text}"
    )
