from elements.button import Button
from elements.label import Label
from elements.web_element import WebElement
from pages.base_page import BasePage


class FramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@class, 'text-center') and text()='Frames']"

    NESTED_FRAMES_BUTT0N_LOC = "//*[text()='Nested Frames']"
    SAMPLE_FRAMES_BUTT0N_LOC = "//*[text()='Frames']"

    FIRST_FRAME = "frame1"
    SECOND_FRAME = "frame2"

    FRAME_LABEL = "sampleHeading"

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "Frames Page"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Frames Page -> Main Header"
        )

        self.nested_frames_button = Button(
            self.browser,
            self.NESTED_FRAMES_BUTT0N_LOC,
            description="Frames Section -> Nested Frames"
        )

        self.sample_frames_button = Button(
            self.browser,
            self.SAMPLE_FRAMES_BUTT0N_LOC,
            description="Frames Section -> Frames"
        )

        self.first_frame = WebElement(
            self.browser,
            self.FIRST_FRAME,
            description="Frames Section -> First Frame"
        )

        self.second_frame = WebElement(
            self.browser,
            self.SECOND_FRAME,
            description="Frames Section -> First Frame"
        )

        self.frame_label = Label(
            self.browser,
            self.FRAME_LABEL,
            description="IFrame -> Label"
        )

    def click_nested_frames(self) -> None:
        self.nested_frames_button.click()

    def click_sample_frames(self) -> None:
        self.sample_frames_button.click()

    def get_first_frame_text(self) -> str:
        self.browser.switch_to_frame(self.first_frame)
        text = self.frame_label.get_text()
        self.browser.switch_to_default_content()
        return text

    def get_second_frame_text(self) -> str:
        self.browser.switch_to_frame(self.second_frame)
        text = self.frame_label.get_text()
        self.browser.switch_to_default_content()
        return text
