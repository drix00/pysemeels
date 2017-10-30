#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: pysemeels.hdf5_sem_parameters

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

HDF5 label for SEM parameters
"""

###############################################################################
# Copyright 2017 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.
HDF5_GROUP_SEM_PARAMETERS = "sem parameters"
HDF5_ATTRIBUTE_INSTRUCT_NAME = "instruct_name".lower().replace('_', ' ')
HDF5_ATTRIBUTE_SEM_VERSION = "sem_version".lower().replace('_', ' ')
HDF5_ATTRIBUTE_SDM_VERSION = "SDM_Version".lower().replace('_', ' ')
HDF5_ATTRIBUTE_SERIAL_NUMBER = "Serial_Number".lower().replace('_', ' ')
HDF5_ATTRIBUTE_DATA_NUMBER = "Data_Number".lower().replace('_', ' ')
HDF5_ATTRIBUTE_SAMPLE_NAME = "Sample_Name".lower().replace('_', ' ')
HDF5_ATTRIBUTE_FORMAT = "Format".lower().replace('_', ' ')
HDF5_ATTRIBUTE_IMAGE_NAME = "Image_Name".lower().replace('_', ' ')
HDF5_ATTRIBUTE_DIRECTORY = "Directory".lower().replace('_', ' ')
HDF5_ATTRIBUTE_DATE = "Date".lower().replace('_', ' ')
HDF5_ATTRIBUTE_TIME = "Time".lower().replace('_', ' ')
HDF5_ATTRIBUTE_MEDIA = "Media".lower().replace('_', ' ')
HDF5_ATTRIBUTE_DATA_SIZE = "Data_Size".lower().replace('_', ' ')
HDF5_ATTRIBUTE_PIXEL_SIZE = "Pixel_Size".lower().replace('_', ' ')
HDF5_ATTRIBUTE_SIGNAL_NAME = "Signal_Name".lower().replace('_', ' ')
HDF5_ATTRIBUTE_DISPLAY_SIGNAL_NAME = "Display_Signal_Name".lower().replace('_', ' ')
HDF5_ATTRIBUTE_LABSE_MODE = "LABSE_Mode".lower().replace('_', ' ')
HDF5_ATTRIBUTE_SE_DET_SETTING = "SE_Det_Setting".lower().replace('_', ' ')
HDF5_ATTRIBUTE_ACCELERATING_VOLTAGE_V = "accelerating voltage (V)"
HDF5_ATTRIBUTE_DECELERATION_VOLTAGE_V = "deceleration voltage (V)"
HDF5_ATTRIBUTE_DECELERATION_MODE = "Deceleration_Mode".lower().replace('_', ' ')
HDF5_ATTRIBUTE_MAGNIFICATION = "Magnification".lower().replace('_', ' ')
HDF5_ATTRIBUTE_WORKING_DISTANCE_um = "working distance (um)"
HDF5_ATTRIBUTE_EMISSION_CURRENT_nA = "emission current (nA)"
HDF5_ATTRIBUTE_LENS_MODE = "Lens_Mode".lower().replace('_', ' ')
HDF5_ATTRIBUTE_PHOTO_SIZE = "Photo_Size".lower().replace('_', ' ')
HDF5_ATTRIBUTE_MAGNIFICATION_DISPLAY = "Magnification_Display".lower().replace('_', ' ')
HDF5_ATTRIBUTE_VACUUM = "Vacuum".lower().replace('_', ' ')
HDF5_ATTRIBUTE_MICRON_MARKER = "Micron_Marker".lower().replace('_', ' ')
HDF5_ATTRIBUTE_SUB_MAGNIFICATION = "Sub_Magnification".lower().replace('_', ' ')
HDF5_ATTRIBUTE_SUB_SIGNAL_NAME = "Sub_Signal_Name".lower().replace('_', ' ')
HDF5_ATTRIBUTE_SPECIMEN_BIAS_V = "specimen bias (V)"
HDF5_ATTRIBUTE_CONDENCER1 = "Condencer1".lower().replace('_', ' ')
HDF5_ATTRIBUTE_SCAN_SPEED = "Scan_Speed".lower().replace('_', ' ')
HDF5_ATTRIBUTE_CAPTURE_SPEED_INTEGRATION = "Capture_Speed_Integration".lower().replace('_', ' ')
HDF5_ATTRIBUTE_CALIBRATION_SCAN_SPEED = "Calibration_Scan_Speed".lower().replace('_', ' ')
HDF5_ATTRIBUTE_IMG_ENHANCE = "Img_Enhance".lower().replace('_', ' ')
HDF5_ATTRIBUTE_COLOR_MODE = "Color_Mode".lower().replace('_', ' ')
HDF5_ATTRIBUTE_COLOR_PALETTE = "Color_Palette".lower().replace('_', ' ')
HDF5_ATTRIBUTE_SCREEN_MODE = "Screen_Mode".lower().replace('_', ' ')
HDF5_ATTRIBUTE_COMMENT = "Comment".lower().replace('_', ' ')
HDF5_ATTRIBUTE_KEYWORD1 = "KeyWord1".lower().replace('_', ' ')
HDF5_ATTRIBUTE_KEYWORD2 = "KeyWord2".lower().replace('_', ' ')
HDF5_ATTRIBUTE_CONDITION = "Condition".lower().replace('_', ' ')
HDF5_ATTRIBUTE_DATA_DISPLAY_COMBINE = "Data_Display_Combine".lower().replace('_', ' ')
HDF5_ATTRIBUTE_STAGE_TYPE = "Stage_Type".lower().replace('_', ' ')
HDF5_ATTRIBUTE_STAGE_POSITION_X = "Stage_Position_X".lower().replace('_', ' ')
HDF5_ATTRIBUTE_STAGE_POSITION_Y = "Stage_Position_Y".lower().replace('_', ' ')
HDF5_ATTRIBUTE_STAGE_POSITION_R = "Stage_Position_R".lower().replace('_', ' ')
HDF5_ATTRIBUTE_STAGE_POSITION_Z = "Stage_Position_Z".lower().replace('_', ' ')
HDF5_ATTRIBUTE_STAGE_POSITION_T = "Stage_Position_T".lower().replace('_', ' ')
HDF5_ATTRIBUTE_FOCUS_DEPTH = "Focus_Depth".lower().replace('_', ' ')
HDF5_ATTRIBUTE_DYNAMIC_FOCUS = "Dynamic_Focus".lower().replace('_', ' ')
HDF5_ATTRIBUTE_TILT_COMPENSATION = "Tilt_Compensation".lower().replace('_', ' ')
HDF5_ATTRIBUTE_RASTER_ROTATION = "Raster_Rotation".lower().replace('_', ' ')
HDF5_ATTRIBUTE_CONDENSER_APERTURE_SIZE_ID = "CONDENSER_APERTURE_SIZE_ID".lower().replace('_', ' ')
HDF5_ATTRIBUTE_OBJECTIVE_APERTURE_SIZE_ID = "OBJECTIVE_APERTURE_SIZE_ID".lower().replace('_', ' ')
HDF5_ATTRIBUTE_BRIGHT_FIELD_APERTURE_SIZE_ID = "BRIGHT_FIELD_APERTURE_SIZE_ID".lower().replace('_', ' ')

