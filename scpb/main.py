from c_event_manager import CEventManager
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    log.debug("Starting main")
    event_manager = CEventManager()
    event_manager.create_race(total_laps=10, max_participants=6)
    log.info(f"Race ID: {event_manager.get_race_id()}")

    event_manager.register_participant("John", 1)
    event_manager.register_participant("Jane", 2)
    event_manager.register_participant("Joe", 3)
    event_manager.register_participant("Jim", 4)
    event_manager.register_participant("Janice", 5)
    event_manager.register_participant("Janine", 6)
    log.info(f"Race state: {event_manager.get_full_state_snapshot()}")
    event_manager.receive_race_command(command=4)
    log.info(f"Race state: {event_manager.get_full_state_snapshot()}")
    event_manager.receive_driver_command({"CarID": 1,
                                          "Speed": 50,
                                          "Brake": 0, 
                                          "LaneChange": 1})
    event_manager.receive_driver_command({"CarID": 2,
                                          "Speed": 60,
                                          "Brake": 0, 
                                          "LaneChange": 1})
    event_manager.receive_driver_command({"CarID": 3,
                                          "Speed": 70,
                                          "Brake": 0, 
                                          "LaneChange": 1})
    event_manager.receive_driver_command({"CarID": 4,
                                          "Speed": 80,
                                          "Brake": 0, 
                                          "LaneChange": 1})
    event_manager.receive_driver_command({"CarID": 5,
                                          "Speed": 90,
                                          "Brake": 0, 
                                          "LaneChange": 1})
    event_manager.receive_driver_command({"CarID": 6,
                                          "Speed": 100,
                                          "Brake": 0, 
                                          "LaneChange": 1})
    log.info(f"Race state: {event_manager.get_full_state_snapshot()}")

if __name__ == "__main__":
    main()
    