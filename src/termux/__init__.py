# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound


class Termux_object:

    def __init__(self):
        self.output = ''
        self.result = Box.from_json(str(self.output))

    def __getitem__(self, key):
        return self.result[key]

    def __str__(self):
        return str(self.result)

    def __reprr__(self):
        return repr(self.result)


from .audio_info import audio_info
from .battery_status import battery_status
from .brightness import brightness
from .camera_info import camera_info
from .camera_photo import camera_photo
