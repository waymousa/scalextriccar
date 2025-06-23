from i_controller import IController
from c_event_manager import CEventManager
import logging
import asyncio
from asyncio import Queue

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class CScalextricSixCarPowerBase(IController):

    def __init__(self, event_manager: CEventManager) -> None:
        log.info("Initializing CScalextricSixCarPowerBase")
        self.current_request_byte_array = bytearray()
        self.next_request_byte_array = bytearray()
        self.response_byte_array = bytearray()
        self.command_queue = Queue()
        self.event_manager = event_manager
        log.debug('Starting controller task...')
        self.task = asyncio.create_task(self.run())
  
    def send_serial_byte_array(self) -> None:
        """
        Sends the current request byte array to the controller.
        Implements serial communication logic.
        """
        serial_count : int = 0
        while serial_count < 3:
            log.debug("Sending serial byte array to controller: %s", self.current_request_byte_array)
            # implement serial logic here
            log.debug("Received response byte array from controller: %s", self.response_byte_array)
            serial_count +=1
            if self.validate_response():
                log.debug("Controller response was valid")
                self.current_request_byte_array = self.next_request_byte_array
                # add code to check to see if the laptime setting is valid and then trigger the 
                # method to send the laptime to the event_manager queue
                break
            else:
                log.error("Response from controller was invalid, retrying...")

    def validate_response(self) -> bool:
        """
        Validates the response byte array received from the controller.
        Returns True if the response is valid, False otherwise.
        """
        log.debug("Validating response")
        # implement response checksum validation here
        # implement response lap time check here
        laptime: int = 0
        if laptime == 1:
            log.info("Lap time received, adding to event_manager queue")
            self.event_manager.lap_time_queue.put(self.response_byte_array)
        return True

    def set_byte_array(self, snapshot: bytearray) -> None:
        """
        Sets the next request byte array based on the given snapshot.
        """
        log.debug("Setting byte array")
        self.next_request_byte_array = snapshot
    
    def convert_byte_array_response_to_lap_time(self, response: bytearray) -> None:
        """
        Converts the response byte array to a lap time.
        This is a placeholder for actual conversion logic.
        """
        log.debug("Converting byte array response to lap time")
        # implement conversion logic here
        # send the converted laptim to the event_manager.
        self.event_manager.lap_time_queue.put(response)

    async def run(self):
        """
        Main loop for the controller.
        Continuously checks for new requests and sends them to the controller.
        """
        log.info("Starting CScalextricSixCarPowerBase main loop")
        while True:
            snapshot = await self.command_queue.get()
            log.debug("Received new request from queue")
            self.set_byte_array(snapshot)
            self.send_serial_byte_array()
            await asyncio.sleep_ms(13)
            self.queue.task_done()
