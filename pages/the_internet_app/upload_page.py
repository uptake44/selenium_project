from elements.button import Button
from elements.input import Input
from elements.label import Label
from pages.base_page import BasePage
from src.utils.pyautogui_utils import PyAutoGuiUtilities


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = "file-upload"

    UPLOAD_ELEMENT_LOC = "file-upload"
    SUBMIT_ELEMENT_LOC = "file-submit"

    DRAG_DROP_ELEMENT_LOC = "drag-drop-upload"

    INNER_FILENAME_ELEMENT_LOC = "//*[@id='drag-drop-upload']//div[contains(@class, 'dz-filename')]"
    INNER_ICON_ELEMENT_LOC = "//*[@id='drag-drop-upload']//div[contains(@class, 'dz-success-mark')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Upload Page"
        self.unique_element = Button(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Upload Page -> Upload File Button"
        )

        self.upload_button = Input(
            self.browser,
            self.UPLOAD_ELEMENT_LOC,
            description="Upload Page -> Upload File Button"
        )

        self.submit_button = Button(
            self.browser,
            self.SUBMIT_ELEMENT_LOC,
            description="Upload Page -> Submit Button"
        )

        self.drag_drop_button = Button(
            self.browser,
            self.DRAG_DROP_ELEMENT_LOC,
            description="Upload Page -> Drag-Drop Field"
        )

        self.uploaded_file_name_element = Label(
            self.browser,
            self.INNER_FILENAME_ELEMENT_LOC,
            description="Upload Page -> Inner Filename Label"
        )

        self.check_mark_element = Label(
            self.browser,
            self.INNER_ICON_ELEMENT_LOC,
            description="Upload Page -> Inner Success Icon Element"
        )

    def direct_upload(self, file_name: str, path: str) -> None:
        self.upload_button.send_keys(path + file_name)
        self.submit_button.click()

    def dialog_window_upload(self, path, file_name) -> None:
        agui = PyAutoGuiUtilities()
        self.drag_drop_button.click()
        agui.upload_file(path + file_name)

    def get_uploaded_file_name(self) -> str:
        return self.uploaded_file_name_element.get_text()

    def get_status_icon(self) -> str:
        return self.check_mark_element.get_text()

    def wait_for_check_mark(self) -> None:
        self.check_mark_element.wait_for_presence()
