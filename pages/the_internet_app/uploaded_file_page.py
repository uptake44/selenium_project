from elements.label import Label
from pages.base_page import BasePage


class UploadedFilePage(BasePage):
    UNIQUE_ELEMENT_LOC = "uploaded-files"

    STATUS_LABEL_LOC = "//div[contains(@class, 'example')]//*[1]"
    UPLOADED_FILE_NAME_LABEL_LOC = "uploaded-files"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Uploaded File Page"
        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Uploaded File Page -> File Name Container"
        )

        self.status_message_element = Label(
            self.browser,
            self.STATUS_LABEL_LOC,
            description="Uploaded File Page -> Status Label"
        )

        self.uploaded_file_name_element = Label(
            self.browser,
            self.UPLOADED_FILE_NAME_LABEL_LOC,
            description="Uploaded File Page -> File Name Container"
        )

    def get_file_name(self) -> str:
        return self.uploaded_file_name_element.get_text()

    def get_status(self) -> str:
        return self.status_message_element.get_text()
