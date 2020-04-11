from tapsdk import TapSDK, TapInputMode
from tapsdk.models import AirGestures
from time import sleep
from enum import IntEnum


class SensorIndex(IntEnum):
    indexof_IMU_GYRO = 0
    indexof_IMU_ACCELEROMETER = 1
    indexof_DEV_THUMB = 0
    indexof_DEV_INDEX = 1
    indexof_DEV_MIDDLE = 2
    indexof_DEV_RING = 3
    indexof_DEV_PINKY = 4


class SensorType(IntEnum):
    _ = 0
    IMU = 1
    Device = 2


tap_instance = []
tap_identifiers = []


def on_connect(identifier, name, fw):
    print(identifier + " Tap: " + str(name), " FW Version: ", fw)
    if identifier not in tap_identifiers:
        tap_identifiers.append(identifier)
    print("Connected taps:")
    for identifier in tap_identifiers:
        print(identifier)


def on_disconnect(identifier):
    print("Tap has disconnected")
    if identifier in tap_identifiers:
        tap_identifiers.remove(identifier)
    for identifier in tap_identifiers:
        print(identifier)


def on_mouse_event(identifier, dx, dy, isMouse):
    if isMouse:
        print(str(dx), str(dy))
    else:
        pass
        # print("Air: ", str(dx), str(dy))


def on_tap_event(identifier, tapcode):
    print(identifier, str(tapcode))
    if int(tapcode) == 17:
        sequence = [500, 200, 500, 500, 500, 200]
        tap_instance.send_vibration_sequence(sequence, identifier)


def on_air_gesture_event(identifier, air_gesture):
    print(" Air gesture: " + AirGestures(air_gesture).name)
    return
    if air_gesture == AirGestures.UP_ONE_FINGER.value:
        tap_instance.set_input_mode(TapInputMode("raw"), identifier)
    if air_gesture == AirGestures.DOWN_ONE_FINGER.value:
        tap_instance.set_input_mode(TapInputMode("text"), identifier)
    if air_gesture == AirGestures.LEFT_ONE_FINGER.value:
        tap_instance.set_input_mode(TapInputMode("controller"), identifier)


def on_air_gesture_state_event(identifier: str, air_gesture_state: bool):
    if air_gesture_state:
        print("Entered air mouse mode")
    else:
        print("Left air mouse mode")


i = 0


def on_raw_sensor_data(identifier, raw_sensor_data):
    # print(raw_sensor_data)
    global i
    i += 1
    # if i % 10 == 0 and raw_sensor_data.type == SensorType.IMU:
    if raw_sensor_data.type == SensorType.IMU:
        print(raw_sensor_data.GetPoint(SensorIndex.indexof_IMU_ACCELEROMETER))
    # if (
    #     raw_sensor_data.GetPoint(1).z > 2000
    #     and raw_sensor_data.GetPoint(2).z > 2000
    #     and raw_sensor_data.GetPoint(3).z > 2000
    #     and raw_sensor_data.GetPoint(4).z > 2000
    # ):
    #     tap_instance.set_input_mode(TapInputMode("controller"), identifier)


def main():
    global tap_instance
    tap_instance = TapSDK()
    tap_instance.run()
    tap_instance.register_connection_events(on_connect)
    tap_instance.register_disconnection_events(on_disconnect)
    tap_instance.register_mouse_events(on_mouse_event)
    tap_instance.register_tap_events(on_tap_event)
    tap_instance.register_raw_data_events(on_raw_sensor_data)
    tap_instance.register_air_gesture_events(on_air_gesture_event)
    tap_instance.register_air_gesture_state_events(on_air_gesture_state_event)
    tap_instance.set_input_mode(TapInputMode("controller"))
    # tap_instance.set_input_mode(TapInputMode("raw", sensitivity=[2,1,4]))
    # tap_instance.set_input_mode(TapInputMode("text"))
    # tap_instance.set_default_input_mode(TapInputMode("raw", sensitivity=[2,1,4]))
    # sleep(3.0)

    while True:
        pass


if __name__ == "__main__":
    main()
