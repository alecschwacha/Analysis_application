import customtkinter 
import pandas as pd 
import numpy as np 

def error_front_left(dataframe):
    if 'ODRIVE_STATE_FAULT' in dataframe['/inputs/drive_outputs/odrive_state_front_left'].tolist():
        return "ERROR"
    else:
        return "NONE"

def error_front_right(dataframe):
    if 'ODRIVE_STATE_FAULT' in dataframe['/inputs/drive_outputs/odrive_state_front_right'].tolist():
        return "ERROR"
    else:
        return "NONE"

def error_rear_left(dataframe):
    if 'ODRIVE_STATE_FAULT' in dataframe['/inputs/drive_outputs/odrive_state_rear_left'].tolist():
        return "ERROR"
    else:
        return "NONE"

def error_rear_right(dataframe):
    if 'ODRIVE_STATE_FAULT' in dataframe['/inputs/drive_outputs/odrive_state_rear_right'].tolist():
        return "ERROR"
    else:
        return "NONE"

class fl_dash(customtkinter.CTkFrame):
    def __init__(self, master, dataframe, TimestampSeries, **kwargs):
        super().__init__(master, **kwargs)

        title=customtkinter.CTkLabel(master= self, text="Front Left DM Metrics")
        title.place(x=25, y=10)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max DM Temp(C): ")
        label.place(x=10, y=40)
        fl_dmtemp=customtkinter.CTkLabel(master=self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_front_left/motor_temp_degC']))
        fl_dmtemp.place(x=140, y=40)
    
        label=customtkinter.CTkLabel(master= self,
                                    text="Max Inverter Temp(C): ")
        label.place(x=10, y=60)
        fl_dmtemp=customtkinter.CTkLabel(master=self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_front_left/inverter_temp_degC']))
        fl_dmtemp.place(x=140, y=60)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Brake Temp(C): ")
        label.place(x=10, y=80)
        fl_dmtemp=customtkinter.CTkLabel(master= self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_front_left/brake_temp_degC']))
        fl_dmtemp.place(x=140, y=80)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Humidity: ")
        label.place(x=10, y=100)
        fl_dmtemp=customtkinter.CTkLabel(master= self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_front_left/rh_percent']))
        fl_dmtemp.place(x=140, y=100)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Dewpoint(C): ")
        label.place(x=10, y=120)
        fl_dmtemp=customtkinter.CTkLabel(master= self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_front_left/dewpoint_degC']))
        fl_dmtemp.place(x=140, y=120)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max/Min Current(A): ")
        label.place(x=10, y=140)
        fl_current=customtkinter.CTkLabel(master= self,
                                        text=f"{round(np.max(dataframe['/inputs/drive_outputs/axis_front_left/current_measurement_iq']))}, {round(np.min(dataframe['/inputs/drive_outputs/axis_front_left/current_measurement_iq']))}")
        fl_current.place(x=140, y=140)

        label=customtkinter.CTkLabel(master= self,
                                    text="DM Error: ")
        label.place(x=10, y=160)
        fl_dmtemp=customtkinter.CTkLabel(master= self,
                                    text=error_front_left(dataframe))
        fl_dmtemp.place(x=140, y=160)

class fr_dash(customtkinter.CTkFrame):
    def __init__(self, master, dataframe, TimestampSeries, **kwargs):
        super().__init__(master, **kwargs)

        title=customtkinter.CTkLabel(master= self, text="Front Right DM Metrics")
        title.place(x=25, y=10)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max DM Temp(C): ")
        label.place(x=10, y=40)
        fr_dmtemp=customtkinter.CTkLabel(master=self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_front_right/motor_temp_degC']))
        fr_dmtemp.place(x=140, y=40)
    
        label=customtkinter.CTkLabel(master= self,
                                    text="Max Inverter Temp(C): ")
        label.place(x=10, y=60)
        fr_dmtemp=customtkinter.CTkLabel(master=self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_front_right/inverter_temp_degC']))
        fr_dmtemp.place(x=140, y=60)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Brake Temp(C): ")
        label.place(x=10, y=80)
        fr_dmtemp=customtkinter.CTkLabel(master= self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_front_right/brake_temp_degC']))
        fr_dmtemp.place(x=140, y=80)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Humidity: ")
        label.place(x=10, y=100)
        fr_dmtemp=customtkinter.CTkLabel(master= self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_front_right/rh_percent']))
        fr_dmtemp.place(x=140, y=100)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Dewpoint(C): ")
        label.place(x=10, y=120)
        fr_dmtemp=customtkinter.CTkLabel(master= self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_front_right/dewpoint_degC']))
        fr_dmtemp.place(x=140, y=120)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max/Min Current(A): ")
        label.place(x=10, y=140)
        fr_current=customtkinter.CTkLabel(master= self,
                                        text=f"{round(np.max(dataframe['/inputs/drive_outputs/axis_front_right/current_measurement_iq']))}, {round(np.min(dataframe['/inputs/drive_outputs/axis_front_right/current_measurement_iq']))}")
        fr_current.place(x=140, y=140)

        label=customtkinter.CTkLabel(master= self,
                                    text="DM Error: ")
        label.place(x=10, y=160)
        fr_dmtemp=customtkinter.CTkLabel(master= self,
                                    text=error_front_right(dataframe))
        fr_dmtemp.place(x=140, y=160)

class rl_dash(customtkinter.CTkFrame):
    def __init__(self, master, dataframe, TimestampSeries, **kwargs):
        super().__init__(master, **kwargs)

        title=customtkinter.CTkLabel(master= self, text="Rear Left DM Metrics")
        title.place(x=25, y=10)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max DM Temp(C): ")
        label.place(x=10, y=40)
        rl_dmtemp=customtkinter.CTkLabel(master=self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_rear_left/motor_temp_degC']))
        rl_dmtemp.place(x=140, y=40)
    
        label=customtkinter.CTkLabel(master= self,
                                    text="Max Inverter Temp(C): ")
        label.place(x=10, y=60)
        rl_dmtemp=customtkinter.CTkLabel(master=self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_rear_left/inverter_temp_degC']))
        rl_dmtemp.place(x=140, y=60)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Brake Temp(C): ")
        label.place(x=10, y=80)
        rl_dmtemp=customtkinter.CTkLabel(master= self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_rear_left/brake_temp_degC']))
        rl_dmtemp.place(x=140, y=80)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Humidity: ")
        label.place(x=10, y=100)
        rl_dmtemp=customtkinter.CTkLabel(master= self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_rear_left/rh_percent']))
        rl_dmtemp.place(x=140, y=100)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Dewpoint(C): ")
        label.place(x=10, y=120)
        rl_dmtemp=customtkinter.CTkLabel(master= self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_rear_left/dewpoint_degC']))
        rl_dmtemp.place(x=140, y=120)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max/Min Current(A): ")
        label.place(x=10, y=140)
        rl_current=customtkinter.CTkLabel(master= self,
                                        text=f"{round(np.max(dataframe['/inputs/drive_outputs/axis_rear_left/current_measurement_iq']))}, {round(np.min(dataframe['/inputs/drive_outputs/axis_rear_left/current_measurement_iq']))}")
        rl_current.place(x=140, y=140)

        label=customtkinter.CTkLabel(master= self,
                                    text="DM Error: ")
        label.place(x=10, y=160)
        rl_dmtemp=customtkinter.CTkLabel(master= self,
                                    text=error_rear_left(dataframe))
        rl_dmtemp.place(x=140, y=160)

class rr_dash(customtkinter.CTkFrame):
    def __init__(self, master, dataframe, TimestampSeries, **kwargs):
        super().__init__(master, **kwargs)

        title=customtkinter.CTkLabel(master= self, text="Rear Right DM Metrics")
        title.place(x=25, y=10)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max DM Temp(C): ")
        label.place(x=10, y=40)
        rr_dmtemp=customtkinter.CTkLabel(master=self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_rear_right/motor_temp_degC']))
        rr_dmtemp.place(x=140, y=40)
    
        label=customtkinter.CTkLabel(master= self,
                                    text="Max Inverter Temp(C): ")
        label.place(x=10, y=60)
        rr_dmtemp=customtkinter.CTkLabel(master=self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_rear_right/inverter_temp_degC']))
        rr_dmtemp.place(x=140, y=60)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Brake Temp(C): ")
        label.place(x=10, y=80)
        rr_dmtemp=customtkinter.CTkLabel(master= self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_rear_right/brake_temp_degC']))
        rr_dmtemp.place(x=140, y=80)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Humidity: ")
        label.place(x=10, y=100)
        rr_dmtemp=customtkinter.CTkLabel(master= self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_rear_right/rh_percent']))
        rr_dmtemp.place(x=140, y=100)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Dewpoint(C): ")
        label.place(x=10, y=120)
        rr_dmtemp=customtkinter.CTkLabel(master= self,
                                        text=np.max(dataframe['/inputs/drive_outputs/axis_rear_right/dewpoint_degC']))
        rr_dmtemp.place(x=140, y=120)

        label=customtkinter.CTkLabel(master= self,
                                    text="Max/Min Current(A): ")
        label.place(x=10, y=140)
        rr_current=customtkinter.CTkLabel(master= self,
                                        text=f"{round(np.max(dataframe['/inputs/drive_outputs/axis_rear_right/current_measurement_iq']))}, {round(np.min(dataframe['/inputs/drive_outputs/axis_rear_right/current_measurement_iq']))}")
        rr_current.place(x=140, y=140)

        label=customtkinter.CTkLabel(master= self,
                                    text="DM Error: ")
        label.place(x=10, y=160)
        rr_dmtemp=customtkinter.CTkLabel(master= self,
                                    text=error_rear_right(dataframe))
        rr_dmtemp.place(x=140, y=160)