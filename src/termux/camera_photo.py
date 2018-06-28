#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

import sys
from box import Box
from termux import Termux_object

try:
    from sh import termux_camera_photo
except ImportError:
    print('Unable to find termux_audio_info')
    print('Please install or update termux-api')
    print(' $ pkg install termux-api')
    sys.exit(2)


def camera_photo(output_file, camera_id=0):
    """
    Take a photo and save it to a file in JPEG format.

    :param output_file: Path of file to save photo
    :type output_file: str

    :param camera_id: ID of the camera to use (see termux-camera-info), default: 0
    :type camera_id: int
    """
    
    termux_camera_photo('-c', camera_id, output_file)
