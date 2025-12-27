from random import randrange

from pages.the_internet_app.slider_page import SliderPage
from src.config.config_reader import ConfigReader

BASE_URL = f"{ConfigReader.get_base_url()}/horizontal_slider"


def get_random_slider_step(
        min_value: float,
        max_value: float,
        step: float
) -> tuple[int, float]:
    first_inner_step = int(min_value // step)
    last_inner_step = int(max_value // step)

    random_step = randrange(first_inner_step, last_inner_step)
    expected_result = random_step * step

    return random_step, expected_result


def test_slider(browser):
    slider_page = SliderPage(browser)
    browser.get(BASE_URL)
    assert slider_page.wait_for_open(), "Страница не открылась"

    step = slider_page.get_step_value()
    min_value = slider_page.get_min_value() + step
    max_value = slider_page.get_max_value()

    presses, expected_result = get_random_slider_step(min_value, max_value, step)

    slider_page.move_slider(presses)

    actual_result = slider_page.get_indicator_value()

    assert actual_result == expected_result, (
        f"Ожидалось: {expected_result}\n"
        f"Получено {actual_result}"
    )
