
import customtkinter 
import pandas as pd 
import numpy as np 
from datetime import timedelta

def run_time(TimestampSeries):
    list_dates=list(TimestampSeries)
    first_date=list_dates[0]
    last_date=list_dates[-1]
    delta=last_date-first_date
    time_difference=round(delta/timedelta(hours=1))
    return time_difference


class cb_dash(customtkinter.CTkFrame):
    def __init__(self,master, dataframe, TimestampSeries, **kwargs):
        super().__init__(master, **kwargs)

        title=customtkinter.CTkLabel(master= self,
                                        text="Centerbody Metrics")
        title.place(relx=0.5, rely=0.05, anchor='center')

        label=customtkinter.CTkLabel(master= self,
                                        text="Robot Runtime (Hours): ")
        label.place(relx=0.3, rely=0.1, anchor='center')
        runtime=customtkinter.CTkLabel(master= self,
                                        text=run_time(TimestampSeries))
        runtime.place(relx=0.65, rely=0.1, anchor='center')

        label=customtkinter.CTkLabel(master= self, 
                                        text="Max AOS Temp(C): ")
        label.place(relx=0.3, rely=0.15, anchor='center' )
        aos_temp=customtkinter.CTkLabel(master= self, 
                                        text= np.max(dataframe['/inputs/toque_outputs/aos_cold_degC']))
        aos_temp.place(relx=0.65, rely=0.15, anchor='center')

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Brain Temp(C): ")
        label.place(relx=0.3, rely=0.2, anchor='center')
        brain_temp=customtkinter.CTkLabel(master= self,
                                    text= np.max(dataframe['/inputs/brain_outputs/temp_degC']))
        brain_temp.place(relx=0.65, rely=.20, anchor='center')

        label=customtkinter.CTkLabel(master= self,
                                    text="Max SFP1 Temp(C): ")
        label.place(relx=0.3, rely=.25, anchor='center')
        sfp1_temp=customtkinter.CTkLabel(master= self,
                                    text=np.max(dataframe['/inputs/brain_outputs/sfp1/temp_degC']))
        sfp1_temp.place(relx=0.65, rely=0.25, anchor='center')

        label=customtkinter.CTkLabel(master= self,
                                    text="Max SFP2 Temp(C): ")
        label.place(relx=0.3, rely=0.3, anchor='center')
        sfp2_temp=customtkinter.CTkLabel(master= self,
                                    text=np.max(dataframe['/inputs/brain_outputs/sfp2/temp_degC']))
        sfp2_temp.place(relx=0.65, rely=0.3, anchor='center')

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Vicor Temp(C): ")
        label.place(relx=0.3, rely=0.35, anchor='center')
        vicor_temp=customtkinter.CTkLabel(master= self,
                                    text=np.max(dataframe['/inputs/hvdcdc_outputs/vicor_temp_degC']))
        vicor_temp.place(relx=0.65, rely=0.35, anchor='center' )

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Brain Humidity: ")
        label.place(relx=0.3, rely=0.4, anchor='center')
        brain_humidity=customtkinter.CTkLabel(master= self,
                                    text=np.max(dataframe['/inputs/brain_outputs/rel_humidity_percent']))
        brain_humidity.place(relx=0.65, rely=0.4, anchor='center')

        label=customtkinter.CTkLabel(master= self,
                                    text="Max HVDCDC Humidity: ")
        label.place(relx=0.3, rely=0.45, anchor='center')
        hvdcdc_humidity=customtkinter.CTkLabel(master= self,
                                    text=np.max(dataframe['/inputs/hvdcdc_outputs/relative_humidity_percent']))
        hvdcdc_humidity.place(relx=0.65, rely=0.45, anchor='center')

        label=customtkinter.CTkLabel(master= self,
                                    text="Max Brain Dewpoint(C): ")
        label.place(relx=0.3, rely=0.5, anchor='center')
        brain_dewpoint=customtkinter.CTkLabel(master= self,
                                    text=np.max(dataframe['/inputs/brain_outputs/dewpoint_degC']))
        brain_dewpoint.place(relx=0.65, rely=0.5, anchor='center')

        label=customtkinter.CTkLabel(master= self,
                                    text="Max HVDCDC Dewpoint(C): ")
        label.place(relx=0.3, rely=0.55, anchor='center')
        hvdcdc_dewpoint=customtkinter.CTkLabel(master= self,
                                    text=np.max(dataframe['/inputs/hvdcdc_outputs/dewpoint_degC']))
        hvdcdc_dewpoint.place(relx=0.65, rely=0.55, anchor='center')