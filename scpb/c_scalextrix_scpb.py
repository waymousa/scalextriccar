from i_controller import IController
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class CScalextricSixCarPowerBase(IController):

    def __init__(self):
        log.info("Initializing CScalextricSixCarPowerBase")

    def send_message(self, message: str) -> str:
        log.info("Sending message: %s", message)
        response = f"Response to: {message}"
        return response