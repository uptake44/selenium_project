import logging
import time

import pyautogui

from src.logger.logger import Logger


class PyAutoGuiUtilities:
    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info("Handle File Dialog for uploading file")
        time.sleep(2)

        logging.debug(f"Write [{file_path}] to search File Dialog field")
        pyautogui.typewrite(file_path)
        logging.debug("Press enter")
        pyautogui.hotkey("enter")

        time.sleep(1)
