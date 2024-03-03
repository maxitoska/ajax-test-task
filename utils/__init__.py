import os
from datetime import datetime


class Loger:
    def __init__(self, program_name, test_status):
        self.program_name = program_name
        self.test_status = test_status
        date = str(datetime.now()).split('.')[0].replace(":", ".").replace("-", ".").split(" ")
        self.init_date = date[0]
        self.init_time = date[1]

    def print(self, text):
        print(text)
        path = "logs"
        filename = f"{self.program_name}_{self.init_date}_{self.init_time}_{self.test_status}.log"
        with open(os.path.join(os.path.dirname(__file__), '..', path, filename), 'a') as log_file:
            log_file.write(text)


def get_udid() -> str:
    listOfDevice = []
    result = os.popen('adb devices').read()
    result = result.replace('List of devices attached', '')
    result = result.replace('device', ',')
    result = result.replace(' ', '').strip()
    result = result.replace('            ', '')
    result = result.replace('\n', '')
    result = result.replace('\t', '')
    deviceList = result.split(",")

    for device in deviceList:
        if device != "":
            listOfDevice.append(device)

    return deviceList[0]
