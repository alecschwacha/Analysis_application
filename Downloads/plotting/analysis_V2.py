import customtkinter 
import pandas as pd 
import numpy as np 
from pathlib import Path
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import webbrowser
from tkinter import filedialog
import google_transfer
import plotting
import cb_dash
import dms_dash
import popup


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("975x900")
        self.title("Analysis Application")
        self.resizable(True, True)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(2, weight=1)

        #Button for selecting CSV
        self.csv=customtkinter.CTkButton(self, text="Select CSV", command=lambda: self.CSV()) 
        self.csv.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        #Button for looking at multiple CSVs
        self.button=customtkinter.CTkButton(self, text="Combine CSV", command=lambda: self.combine())
        self.button.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        #Button for Selecting log **still needs to be setup 
        self.button=customtkinter.CTkButton(self, text="Selecting Log File", command=lambda: self.log())
        self.button.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')
        
        #button for selecting Director(MAybe) **still needs to be setup
        self.button=customtkinter.CTkButton(self, text="Select Folder", command=lambda: self.directory())
        self.button.grid(row=1, column=3, padx=10, pady=10, sticky='nsew')

        #button for opening terraium 
        self.button=customtkinter.CTkButton(self, text="Terraium", command=lambda: self.terriaum_link())
        self.button.grid(row=1, column=4, padx=10, pady=10, sticky='nsew')

        #button for opening Google buckets
        self.button=customtkinter.CTkButton(self, text="Google Buckets", command=lambda: self.google_buckets())
        self.button.grid(row=1, column=5, padx=10, pady=10, sticky='nsew')       

        self.count = 0

    def combine(self): 
        self.count=self.count+1
        if self.count <=1:  
            #Selecting and creating title 
            self.file_path=filedialog.askopenfilenames(filetypes=(("CSV files", "*.csv"), ("All Files", "*.*")))
            self.files=list(self.file_path)
            self.name=self.file_path[-1].split("/")[-1]
            self.name1=self.name.split("_")[0]
            self.title(f"{self.name1}")
            
            global d
            d=popup.loading_multi(self.files)
                        
            global time
            initial_time=pd.to_datetime(d['/timestamp'], unit='s')
            time=(initial_time-timedelta(hours=4)) 

            #Custom Frame
            self.dash=dashboard(master=self, corner_radius=20)
            self.dash.grid(rows=2, columnspan=6, padx=20, pady=20, sticky="nsew")

            #Custom Tabs 
            self.tabview=tab_view(master=self, width=900, height=300, corner_radius=20)
            self.tabview.grid(rows=3, columnspan=6, padx=20, pady=20, sticky="sew")

            #uploading file to the Google Cloud        
            def cloud():
                google_transfer.health_database(d, self.name1)
                google_transfer.upload(f'{self.name1}_health.csv', self.name1)

            self.button=customtkinter.CTkButton(master=self, text="Upload", command=cloud)
            self.button.grid(row=7, column=0, pady=10)

        else: 

            self.file_path=filedialog.askopenfilenames(filetypes=(("CSV files", "*.csv"), ("All Files", "*.*")))
            self.files=list(self.file_path)
            self.name=self.file_path[-1].split("/")[-1]
            self.name1=self.name.split("_")[0]
            self.title(f"{self.name1}")

            d=popup.loading_multi(self.files)
            if type(d) is str:
                pass
            else:
                try:
                    self.tabview.destroy()
                    self.dash.destroy()
                    self.button.destroy()
                except AttributeError:
                    pass
            
            try: 
                initial_time=pd.to_datetime(d['/timestamp'], unit='s')
                time=(initial_time-timedelta(hours=4)) 
                
            except KeyError or NameError:
                popup.wrong_csv()
            
            #Custom Frame
            self.dash=dashboard(master=self, corner_radius=20)
            self.dash.grid(rows=2, columnspan=6, padx=20, pady=20, sticky="nsew")

            #Custom Tabs 
            self.tabview=tab_view(master=self, width=900, height=300, corner_radius=20)
            self.tabview.grid(rows=3, columnspan=6, padx=20, pady=20, sticky="sew")

            #uploading file to the Google Cloud        
            def cloud():
                google_transfer.health_database(d, self.name1)
                google_transfer.upload(f'{self.name1}_health.csv', self.name1)

            self.button=customtkinter.CTkButton(master=self, text="Upload", command=cloud)
            self.button.grid(row=7, column=0, pady=10)

    def CSV(self):
        self.count=self.count+1
        if self.count<=1:
            self.file_path=filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"), ("All Files", "*.*")))
            self.name=self.file_path.split("/")[-1]
            self.name1=self.name.split("_")[0]
            self.title(f"{self.name1}")

            global d 
            d=popup.loading(self.file_path)
            
            try: 
                global time
                initial_time=pd.to_datetime(d['/timestamp'], unit='s')
                time=(initial_time-timedelta(hours=4)) 

            except KeyError or NameError:
                popup.wrong_csv()

            #Custom Frame
            self.dash=dashboard(master=self, corner_radius=20)
            self.dash.grid(rows=2, columnspan=6, padx=20, pady=20, sticky="nsew")

            #Custom Tabs 
            self.tabview=tab_view(master=self, width=900, height=300, corner_radius=20)
            self.tabview.grid(rows=3, columnspan=6, padx=20, pady=20, sticky="sew")

            #uploading file to the Google Cloud        
            def cloud():
                # google_transfer.report_card(d)
                google_transfer.health_database(d, self.name1)
                google_transfer.upload(f'{self.name1}_health.csv', self.name1)

            self.button=customtkinter.CTkButton(self, text="Upload", command=cloud)
            self.button.grid(row =7, column=0, pady=10)

        else:
            self.file_path=filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"), ("All Files", "*.*")))
            self.name=self.file_path.split("/")[-1]
            self.name1=self.name.split("_")[0]
            self.title(f"{self.name1}")

            d=popup.loading(self.file_path)

            if type(d) is str:
                pass
            else:
                try:
                    self.dash.destroy()
                    self.tabview.destroy()
                    self.button.destroy()
                except AttributeError:
                    pass
            
            try: 
                initial_time=pd.to_datetime(d['/timestamp'], unit='s')
                time=(initial_time-timedelta(hours=4)) 

            except KeyError or NameError:
                popup.wrong_csv()               

            #Custom Frame
            self.dash=dashboard(master=self, corner_radius=20)
            self.dash.grid(rows=2, columnspan=6, padx=20, pady=20, sticky="nsew")

            #Custom Tabs 
            self.tabview=tab_view(master=self, width=900, height=300, corner_radius=20)
            self.tabview.grid(rows=3, columnspan=6, padx=20, pady=20, sticky="sew")

            #uploading file to the Google Cloud        
            def cloud():
                google_transfer.health_database(d, self.name1)
                google_transfer.upload(f'{self.name1}_health.csv', self.name1)

            self.button=customtkinter.CTkButton(self, text="Upload", command=cloud)
            self.button.grid(row =7, column=0, pady=10)
        
    def directory(self):
        self.count=self.count+1
        if self.count<=1:
            self.dir=filedialog.askdirectory()
            files=list(Path(self.dir).glob('*.csv'))
            print(files[-1])
            
            global d
            d=popup.loading_multi(files)
        
            global time
            initial_time=pd.to_datetime(d['/timestamp'], unit='s')
            time=(initial_time-timedelta(hours=4)) 

            #Custom Frame
            self.dash=dashboard(master=self, corner_radius=20)
            self.dash.grid(rows=2, columnspan=6, padx=20, pady=20, sticky="nsew")

            #Custom Tabs 
            self.tabview=tab_view(master=self, width=900, height=300, corner_radius=20)
            self.tabview.grid(rows=3, columnspan=6, padx=20, pady=20, sticky="sew")

            #uploading file to the Google Cloud        
            def cloud():
                google_transfer.report_card(d)
                google_transfer.upload('attempt.csv')

            self.button=customtkinter.CTkButton(self, text="Upload", command=cloud)
            self.button.grid(row =7, column=0, pady=10)

        else:
            self.dir=filedialog.askdirectory()
            files=list(Path(self.dir).glob('*.csv'))
            
            self.dash.destroy()
            self.tabview.destroy()
            self.button.destroy()

            d=popup.loading_multi(files)
        
            initial_time=pd.to_datetime(d['/timestamp'], unit='s')
            time=(initial_time-timedelta(hours=4)) 

            #Custom Frame
            self.dash=dashboard(master=self, corner_radius=20)
            self.dash.grid(rows=2, columnspan=6, padx=20, pady=20, sticky="nsew")

            #Custom Tabs 
            self.tabview=tab_view(master=self, width=900, height=300, corner_radius=20)
            self.tabview.grid(rows=3, columnspan=6, padx=20, pady=20, sticky="sew")

            #uploading file to the Google Cloud        
            def cloud():
                google_transfer.report_card(d)
                google_transfer.upload('attempt.csv')

            self.button=customtkinter.CTkButton(self, text="Upload", command=cloud)
            self.button.grid(row =7, column=0, pady=10)

    def log(self):
        self.log_path=filedialog.askopenfilename(filetypes=(("Log Files", "*.log"), ("All Files", "*.*")))
        self.title(self.log_path)
        
    def terriaum_link(self):
        webbrowser.open('https://terrarium.internal.geckorobotics.com/table')

    def google_buckets(self):
        webbrowser.open('https://console.cloud.google.com/storage/browser?organizationId=402743163244&project=gecko-ops&pageState=(%22StorageBucketsTable%22:(%22f%22:%22%255B%257B_22k_22_3A_22Name%2520contains_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22G4_5C_22_22_2C_22i_22_3A_22name_22%257D%255D%22,%22s%22:%5B(%22i%22:%22name%22,%22s%22:%220%22)%5D,%22r%22:30))&prefix=&forceOnBucketsSortingFiltering=true')
        

class tab_view(customtkinter.CTkTabview):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        
        #creating tabs
        self.add("Centerbody")
        self.add("Drive Module")
        self.add("Create Plot")

        #cb tab layout 
        self.button=customtkinter.CTkButton(master=self.tab("Centerbody"),
                                            text="CB Humidity and Dew Point",
                                            command=lambda: plotting.CBhumidity(d, time))
        self.button.grid(row=0, column=0, padx=20, pady=20)

        self.button=customtkinter.CTkButton(master=self.tab("Centerbody"),
                                            text="CB Temperature Deg C",
                                            command=lambda: plotting.cbtemp(d, time))        
        self.button.grid(row=0, column=1, padx=20, pady=20)

        self.button=customtkinter.CTkButton(master=self.tab("Centerbody"),
                                            text="CB Current",
                                            command=lambda: plotting.CBcurrent(d, time))
        self.button.grid(row=0, column=2, padx=20, pady=20)
        
        self.button=customtkinter.CTkButton(master=self.tab("Centerbody"),
                                            text="Robot Disconnects",
                                            command=lambda: plotting.disconnects(d, time))
        self.button.grid(row=1, column=0, padx=20, pady=20)

        self.button=customtkinter.CTkButton(master=self.tab("Centerbody"),
                                            text="Switch Ports Speeds",
                                            command= lambda: plotting.switch_speed(d,time))
        self.button.grid(row=1, column=1, padx=20, pady=20)

        self.button=customtkinter.CTkButton(master=self.tab("Centerbody"),
                                            text="Switch Ports Presence",
                                            command= lambda: plotting.switch_presence(d,time))
        self.button.grid(row=1, column=2, padx=20, pady=20)

        self.button=customtkinter.CTkButton(master=self.tab("Centerbody"),
                                            text="AOS Current",
                                            command= lambda: plotting.AOS_current(d,time))
        self.button.grid(row=0, column=3, padx=20, pady=20)


        #DM Tab layout 
        self.button=customtkinter.CTkButton(master=self.tab("Drive Module"),
                                            text="DM Humidity and Dew Point", 
                                            command=lambda: plotting.dmhumidity(d, time))
        self.button.grid(row=0, column=0, padx=20, pady=20)

        self.button=customtkinter.CTkButton(master=self.tab("Drive Module"), 
                                            text="DM Motor Temp Deg C",
                                            command=lambda: plotting.dm_motor_temp(d, time))
        self.button.grid(row=0, column=1, padx=20, pady=20)

        self.button=customtkinter.CTkButton(master=self.tab("Drive Module"), 
                                            text="DM Inverter Temp Deg C",
                                            command=lambda: plotting.dm_inverter_temp(d, time))
        self.button.grid(row=0, column=2, padx=20, pady=20)
        
        self.button=customtkinter.CTkButton(master=self.tab("Drive Module"),
                                             text="DM Brake Temp Deg C", 
                                             command=lambda: plotting.dm_brake_temp(d, time))
        self.button.grid(row=0, column=3, padx=20, pady=20)
        
        self.button=customtkinter.CTkButton(master=self.tab("Drive Module"),
                                            text="IQ Current",
                                            command=lambda: plotting.iqcurrent(d, time))
        self.button.grid(row=1, column=0, padx=20, pady=20)

        self.button=customtkinter.CTkButton(master=self.tab("Drive Module"),
                                            text="Linear Actuator Current",
                                            command=lambda: plotting.acutator(d, time))
        self.button.grid(row=1, column=1, padx=20, pady=20)

        self.button=customtkinter.CTkButton(master=self.tab("Drive Module"),
                                            text="Encoder Count Comparison",
                                            command=lambda: plotting.encoder(d, time ))
        self.button.grid(row=1, column=2, padx=20, pady=20)

        self.button=customtkinter.CTkButton(master=self.tab("Drive Module"),
                                            text="DM Current Measurement",
                                            command=lambda: plotting.current_measure(d,time))
        self.button.grid(row=1, column=3, padx=20, pady=20)

        self.button=customtkinter.CTkButton(master=self.tab("Drive Module"),
                                            text="DM Encoder",
                                            command=lambda: plotting.softfault_error(d, time))
        self.button.grid(row=2, column=0, padx=20, pady=20)
        
        self.button=customtkinter.CTkButton(master=self.tab("Drive Module"),
                                            text="DM Motor Error",
                                            command=lambda: plotting.motor_error(d,time))
        self.button.grid(row=2, column=1, padx=20, pady=20)

        self.button=customtkinter.CTkButton(master=self.tab("Drive Module"),
                                            text="DM Vbus",
                                            command=lambda:plotting.voltage_bus(d, time))
        self.button.grid(row=2, column=2, padx=20, pady=20)
        
        #Creating your own graph
        self.CBradio=customtkinter.CTkRadioButton(master=self.tab("Create Plot"),
                                            text="CB",
                                            command=lambda: self.cbbutton())
        self.CBradio.grid(row=0, column=0, padx=10, pady=10)

        self.dmradio=customtkinter.CTkRadioButton(master=self.tab("Create Plot"), 
                                            text="DM", 
                                            command=lambda: self.dmbutton())
        self.dmradio.grid(row=1, column=0, padx=10, pady=10)
        
    def cbbutton(self): 
        #produce drop down
        dataframe_headers=d.columns.to_list()
        cb_header_list=list()
        brain_output=list(filter(lambda k: '/inputs/brain_outputs' in k, dataframe_headers))
        hvdcdc_outputs=list(filter(lambda k: '/inputs/hvdcdc_outputs' in k, dataframe_headers))
        toque_outputs=list(filter(lambda k: '/inputs/toque_outputs'in k, dataframe_headers))
        cb_header_list.extend(brain_output)
        cb_header_list.extend(hvdcdc_outputs)
        cb_header_list.extend(toque_outputs)
        
        def combo(choice): 
            plt.figure(figsize=(9,4))
            plt.plot(time, d[choice], label=choice)
            plt.xlabel("Time")
            plt.legend()
            plt.show()

        option_box=customtkinter.CTkComboBox(master=self.tab("Create Plot"), values=cb_header_list , command=combo, width=500)
        option_box.grid(row=0, column=1, padx=10, pady=10)
    
    def dmbutton(self): 
        #produce drop down
        dataframe_headers=d.columns.to_list()
        dm_header_list=list()
        drive_output=list(filter(lambda k: '/inputs/drive_outputs' in k, dataframe_headers))
        drive_input=list(filter(lambda k: '/inputs/drive_inputs' in k, dataframe_headers))
        dm_header_list.extend(drive_output)
        dm_header_list.extend(drive_input)
        def combo(choice): 
            plt.figure(figsize=(9,4))
            plt.plot(time, d[choice], label=choice)
            plt.xlabel("Time")
            plt.legend()
            plt.show()

        option_box=customtkinter.CTkComboBox(master=self.tab("Create Plot"), values=dm_header_list , command=combo, width=500)
        option_box.grid(row=1, column=1, padx=10, pady=10)


class dashboard(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #Creating labels/dashboard components 
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        
        #Center Body metrics frame
        self.cb_frame=cb_dash.cb_dash(dataframe= d,
                                TimestampSeries=time,
                                master=self, 
                                border_color="white",
                                border_width=2)
        self.cb_frame.grid(rows=2, column=1, pady=5, sticky="nwes")

        #Front Left DM Metrics frame
        self.front_left_frame=dms_dash.fl_dash(dataframe=d,
                                           TimestampSeries=time,
                                           master=self,
                                           border_color="white", 
                                           border_width=2)
        self.front_left_frame.grid(row=0, column=0, padx=5, pady=5)

        #Front right DM Metrics Frame
        self.front_right=dms_dash.fr_dash(dataframe=d,
                                           TimestampSeries=time,
                                           master=self,
                                           border_color="white", 
                                           border_width=2)
        self.front_right.grid(row=0, column=2, padx=5, pady=5)
        
        #Rear Left DM metrics frame 

        self.rear_left_frame=dms_dash.rl_dash(dataframe=d,
                                           TimestampSeries=time,
                                           master=self,
                                           border_color="white", 
                                           border_width=2)
        self.rear_left_frame.grid(row=1, column=0, padx=5, pady=5)
        
        #Rear Right DM metrics frame 
        self.rear_right=dms_dash.rr_dash(dataframe=d,
                                           TimestampSeries=time,
                                           master=self,
                                           border_color="white", 
                                           border_width=2)
        self.rear_right.grid(row=1, column=2, padx=5, pady=5)
        
app=App()
app.mainloop()