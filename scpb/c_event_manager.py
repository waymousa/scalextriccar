import uuid
from c_driver import CDriver  
from c_participant import CParticipant
from c_controller_factory import CControllerFactory
from c_car_factory import CCarFactory
import logging
import secrets
import asyncio
from asyncio import Queue

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

class CEventManager:

    def __init__(self, controller_type: str ="ScalextricSixCarPowerBase") -> None:
        log.debug("Initializing Event Manager")
        self.race_id = 0
        self.race_state = 0
        self.lap_times = []
        self.participants = []
        self.total_laps = 0
        self.max_participants = 0
        self.race_commands = []
        self.lap_time_queue = Queue()
        self.race_controller = CControllerFactory.create_controller(self, controller_type)

    def create_race(self, total_laps: int=10, max_participants: int =6) -> None:
        log.info("Creating race")
        self.set_race_id()
        self.set_total_laps(total_laps)
        self.set_max_participants(max_participants)
  
    def get_race_id(self) -> uuid.UUID:
        log.debug("Getting race id")
        return self.race_id

    def set_race_id(self) -> None:
        log.debug("Setting race id")
        self.race_id = uuid.uuid4()
    
    def get_total_laps(self) -> int:
        log.debug("Getting total laps")
        return self.total_laps
    
    def set_total_laps(self, total_laps: int) -> None:
        log.debug("Setting total laps")
        if total_laps <= 0:
            raise ValueError("Total laps must be greater than zero")
        self.total_laps = total_laps

    def get_max_participants(self) -> int:
        log.debug("Getting max participants")        
        return self.max_participants

    def set_max_participants(self, max_participants: int) -> None:
        log.debug("Setting maximum participants")
        if max_participants <= 0:
            raise ValueError("Maximum participants must be greater than zero")
        self.max_participants = max_participants    

    def start_race(self) -> None:
        log.debug("Starting race")
        self.race_state = 1
        print("Race started")
    
    def end_race(self) -> None:
        log.debug("Ending race")
        self.race_state = 0
        print("Race ended")

    def get_race_state(self) -> int:
        log.debug("Getting race state")
        return self.race_state
    
    def red_flag_race(self) -> None:
        log.debug("Red flag race")
        self.race_state = 2
        print("Race paused due to red flag")
    
    def yellow_flag_race(self) -> None:
        log.debug("Yellow flag race")
        self.race_state = 3
        print("Race slowed due to yellow flag")

    def start_practice(self) -> None:
        log.debug("Starting practice")
        self.race_state = 4
        print("Practice started")

    def register_participant(self, driver_name: str, car_id: int) -> None:
        '''
        Registers a participant with the given driver name and car ID.
        Raises a ValueError if the maximum number of participants has been reached,
        or if a participant with the same driver name or car ID already exists.
        '''
        log.debug("Registering participant")
        log.info("Registering participant")
        log.debug(driver_name)
        log.debug(car_id)
        if len(self.participants) >= self.max_participants:
            raise ValueError("Maximum participants reached")
        if self.get_participant_driver(driver_name) or self.get_participant_car(car_id):
            raise ValueError("Driver or car already registered")
        participant = CParticipant()
        driver = CDriver(driver_name)
        log.debug(driver.get_driver_name())
        car = CCarFactory.create_car(car_id, car_type="ScalextricDigital")
        log.debug(car.get_car_id())
        participant.set_driver(driver)
        participant.set_car(car)
        self.participants.append(participant)
 
    def get_participant_driver(self, driver_name: str):
        '''
        Returns the participant object for the given driver name.
        If no participant is found with the given driver name, returns None.
        '''
        log.debug("Getting participant driver")
        for participant in self.participants:
            if participant.get_driver().get_driver_name() == driver_name:
                return participant
        return None
    
    def get_participant_car(self, car_id: int):
        '''
        Returns the participant object for the given car ID.
        If no participant is found with the given car ID, returns None.
        '''
        log.debug("Getting participant car")
        for participant in self.participants:
            if participant.get_car().get_car_id() == car_id:
                return participant
        return None
    
    def get_participants(self):
        '''
        Returns a list of dictionaries containing driver names and car IDs of all participants.
        Each tuple is in the format (driver_name, car_id).
        '''
        log.debug("Getting participants")
        parts = [{"Name:" : participant.get_driver().get_driver_name(), 
                  "CarID:" : participant.get_car().get_car_id()} 
                  for participant in self.participants]
        return parts
    
    def get_full_state_snapshot(self):
        '''
        Returns a list of dictionaries containing the full state of the race manager
        '''
        log.debug("Getting full state snapshot")
        snapshot = []
        parts = [{"Name:" : participant.get_driver().get_driver_name(), 
                  "CarID:" : participant.get_car().get_car_id(),
                  "Brake:" : participant.get_car().get_car_brake(),
                  "Speed:" : participant.get_car().get_car_speed(),
                  "LaneChange:" : participant.get_car().get_car_lane_change()} 
                  for participant in self.participants]
        snapshot.append({"RaceID": self.race_id,
                        "RaceState": self.race_state,
                        "SnapshotUID": secrets.token_hex(4),
                        "Participants": parts})
        return snapshot
    
    def receive_lap_time(self, car_id: int, lap_time):
        log.debug("Receiving lap time")
        participant = self.get_participant_car(car_id)
        if participant:
            car_id = participant.get_car().get_car_id()
            driver_name = participant.get_driver().get_driver_name()
            print(f"Lap time {lap_time} recorded for {car_id}")
            self.lap_times.append((driver_name, car_id, lap_time))
        else:
            print(f"Driver {driver_name} not found")

    def receive_race_command(self, command: int) -> None:
        """
        Recieves a race comand and updates the race state accordingly.
        Args:
            command (int): The command to be processed.
        """
        log.debug("Receiving race command")
        if command < 0 or command > 4:
            raise ValueError("Invalid race command")
        self.race_state = command

    def receive_driver_command(self, command = {}):
        log.debug("Receiving driver command")
        if not isinstance(command, dict):
            raise ValueError("Invalid driver command")
        if "CarID" in command:
            car_id = command["CarID"]
            participant = self.get_participant_car(car_id)
            if participant:
                car = participant.get_car()
                if "Brake" in command:
                    car.set_car_brake(command["Brake"])
                if "Speed" in command:
                    car.set_car_speed(command["Speed"])
                if "LaneChange" in command:
                    car.set_car_lane_change(command["LaneChange"])
                log.debug(f"Driver command received for CarID {car_id}: {command}")
            else:
                log.error(f"No participant found with CarID {car_id}")
 
    def issue_controller_command(self, command):
        log.debug("Issuing controller command")
        print(f"Controller command issued: {command}")
    
    def receive_controller_response(self, response):
        log.debug("Receiving controller response")
        print(f"Controller response received: {response}")

    async def run(self):
        log.info("Starting EventManager main loop")
        while True:
            laptime = await self.lap_time_queue.get()


