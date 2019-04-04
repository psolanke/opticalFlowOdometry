from dronekit import connect
import time

class Utils(object):

    def __init__(self,connection_string):
        self.vehicle = connect(connection_string, baud=115200)
        time.sleep(10)

    def get_state(self):
        state_dict = {}
        state_dict['latitude'] = self.vehicle.location.global_relative_frame.lat
        state_dict['longitude'] = self.vehicle.location.global_relative_frame.lon
        state_dict['heading'] = self.vehicle.heading
        state_dict['altitude'] = self.vehicle.location.global_relative_frame.alt
        state_dict['yaw'] = self.vehicle.attitude.yaw
        state_dict['pitch'] = self.vehicle.attitude.pitch
        state_dict['roll'] = self.vehicle.attitude.roll
        return state_dict


