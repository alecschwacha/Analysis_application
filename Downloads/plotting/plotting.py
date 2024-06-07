import pandas as pd 
import matplotlib.pyplot as plt 


def AOS_current(dataframe, TimestampSeries):
    plt.figure(figsize=(9,4))
    plt.plot(TimestampSeries, dataframe['/inputs/toque_outputs/aos_current_mA'], label='AOS current mA')
    plt.xlabel("Time")
    plt.ylabel("Current mA")
    plt.title("AOS current mA")
    plt.xticks(rotation=25)
    plt.legend()
    plt.show()


def switch_presence(dataframe, TimestampSeries): 
    plt.figure(figsize=(20,4))
    plt.plot(TimestampSeries,dataframe['/inputs/brain_outputs/switch_port1_presence'], label='port 1 presence')
    plt.plot(TimestampSeries,dataframe['/inputs/brain_outputs/switch_port3_presence'], label='port 3 presence')
    plt.plot(TimestampSeries,dataframe['/inputs/brain_outputs/switch_port6_presence'], label='port 6 presence')
    plt.plot(TimestampSeries,dataframe['/inputs/brain_outputs/switch_port7_presence'], label='port 7 presence')
    plt.xlabel("Time")
    plt.title("Port Presence")
    plt.legend()
    plt.show()        
    

def switch_speed(dataframe, TimestampSeries):
    plt.figure(figsize=(20,4))
    plt.plot(TimestampSeries,dataframe['/inputs/brain_outputs/switch_port1_speed'], label='port 1 speed')
    plt.plot(TimestampSeries,dataframe['/inputs/brain_outputs/switch_port3_speed'], label='port 3 speed')
    plt.plot(TimestampSeries,dataframe['/inputs/brain_outputs/switch_port6_speed'], label='port 6 speed')
    plt.plot(TimestampSeries,dataframe['/inputs/brain_outputs/switch_port7_speed'], label='port 7 speed')
    plt.xlabel("Time")
    plt.title("Port speeds")
    plt.legend()
    plt.show()        


def voltage_bus(dataframe, TimestampSeries): 
    plt.figure(figsize=(24,12))
    plot1 = plt.subplot2grid((2, 2), (0, 0)) 
    plot2 = plt.subplot2grid((2, 2), (0, 1)) 
    plot3 = plt.subplot2grid((2, 2), (1, 0))
    plot4 = plt.subplot2grid((2, 2), (1, 1))

    plot1.set_xlabel('Time')
    plot1.set_ylabel('Volts')
    plot1.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_left/vbus_voltage_v'])
    plot1.set_title('Voltage Front Left')

    plot2.set_xlabel('Time')
    plot2.set_ylabel('Volts')
    plot2.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_right/vbus_voltage_v'])
    plot2.set_title('Voltage Front Right')

    plot3.set_xlabel('Time') 
    plot3.set_ylabel('Volts')
    plot3.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_left/vbus_voltage_v'])
    plot3.set_title('Voltage Rear Left')


    plot4.set_xlabel('Time')
    plot4.set_ylabel('Volts')
    plot4.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_right/vbus_voltage_v'])
    plot4.set_title('Voltage Rear Right')
    plt.show()   


def motor_error(dataframe, TimestampSeries):
    plt.figure(figsize=(24,12))
    plot1 = plt.subplot2grid((2, 2), (0, 0)) 
    plot2 = plt.subplot2grid((2, 2), (0, 1)) 
    plot3 = plt.subplot2grid((2, 2), (1, 0))
    plot4 = plt.subplot2grid((2, 2), (1, 1))

    plot1.set_xlabel('Time')
    plot1.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_left/motor_error'])
    plot1.set_title('Motor Error Front Left')
    plot1.set_yticklabels(plot1.get_yticklabels(), rotation=60)

    plot2.set_xlabel('Time')
    plot2.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_right/motor_error'])
    plot2.set_title('Motor Error Front Right')
    plot2.set_yticklabels(plot2.get_yticklabels(), rotation=60)

    plot3.set_xlabel('Time')
    plot3.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_left/motor_error'])
    plot3.set_title('Motor Error Rear Left')
    plot3.set_yticklabels(plot3.get_yticklabels(), rotation=60)

    plot4.set_xlabel('Time')
    plot4.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_right/motor_error'])
    plot4.set_title('Motor Error Rear Right')
    plot4.set_yticklabels(plot4.get_yticklabels(), rotation=60)

    plt.show()    


def disconnects(dataframe, TimestampSeries):
    plt.figure(figsize=(22,4))
    plt.plot(TimestampSeries,dataframe['/inputs/brain_outputs/brain_state'])
    plt.xlabel("Time")
    plt.title('Robot Disconnects in relation to time')
    # plt.yticks(rotation=35)
    plt.show()

def softfault_error(dataframe, TimestampSeries): 
    plt.figure(figsize=(24,12))
    plot1 = plt.subplot2grid((2, 2), (0, 0)) 
    plot2 = plt.subplot2grid((2, 2), (0, 1)) 
    plot3 = plt.subplot2grid((2, 2), (1, 0))
    plot4 = plt.subplot2grid((2, 2), (1, 1))

    plot1.set_xlabel('Time')
    plot1.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_left/encoder_error'])
    plot1.set_title('Motor Encoder Error Front Left')
    plot1.set_yticklabels(plot1.get_yticklabels(), rotation=60)

    plot2.set_xlabel('Time')
    plot2.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_right/encoder_error'])
    plot2.set_title('Motor Encoder Error Front Right')
    plot2.set_yticklabels(plot2.get_yticklabels(), rotation=60)
   
    plot3.set_xlabel('Time')
    plot3.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_left/encoder_error'])
    plot3.set_title('Motor Encoder Error Rear Left')
    plot3.set_yticklabels(plot3.get_yticklabels(), rotation=60)

    plot4.set_xlabel('Time')
    plot4.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_right/encoder_error'])
    plot4.set_title('Motor Encoder Error Rear Right')
    plot4.set_yticklabels(plot4.get_yticklabels(), rotation=60)

    plt.show()    

def current_measure(dataframe, TimestampSeries): 
    plt.figure(figsize=(24,12))
    plot1 = plt.subplot2grid((2, 2), (0, 0)) 
    plot2 = plt.subplot2grid((2, 2), (0, 1)) 
    plot3 = plt.subplot2grid((2, 2), (1, 0))
    plot4 = plt.subplot2grid((2, 2), (1, 1))

    plot1.set_xlabel('Time')
    plot1.set_ylabel('IQ(amps)')
    plot1.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_left/current_measurement_iq'], label="Front Left Current Measurement")
    plot1.set_title('Current Front Left DM')
    plot1.legend()

    plot2.set_xlabel('Time')
    plot2.set_ylabel('IQ(amps)')
    plot2.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_right/current_measurement_iq'], label="Front Right Current Measurement")
    plot2.set_title('Current Front Right DM')
    plot2.legend()

    plot3.set_xlabel('Time')
    plot3.set_ylabel('IQ(amps)')
    plot3.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_left/current_measurement_iq'], label='Rear Left Current Measurement')
    plot3.set_title('Current Rear Left DM')
    plot3.legend()

    plot4.set_xlabel('Time')
    plot4.set_ylabel('IQ(amps)')
    plot4.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_right/current_measurement_iq'], label='Rear Right Current Measurement')
    plot4.set_title('Current Rear Right DM')
    plot4.legend()
    plt.show()    

def encoder(dataframe, TimestampSeries): 
    plt.figure(figsize=(9,4))
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/encoder_primary_count'], label="Primary Encoder Count")
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/encoder_secondary_count'], label="Secondary Encoder Count")
    plt.title("Primary and Secondary Count Comparison")
    plt.legend()
    plt.show()

def acutator(dataframe, TimestampSeries): 
    plt.figure(figsize=(9,4))
    plt.plot(TimestampSeries, dataframe['/inputs/drive_outputs/sensor_rail_right_current_mA'], label="Right Linear Actuator Current mA")
    plt.plot(TimestampSeries, dataframe['/inputs/drive_outputs/sensor_rail_left_current_mA'], label="Left Linear Actuator Current mA")
    plt.title("Linear Actuator Current mA vs Time")
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Current mA")
    plt.show()
    
def iqcurrent(dataframe, TimestampSeries):
    plt.figure(figsize=(24,12))
    plot1 = plt.subplot2grid((2, 2), (0, 0)) 
    plot2 = plt.subplot2grid((2, 2), (0, 1)) 
    plot3 = plt.subplot2grid((2, 2), (1, 0))
    plot4 = plt.subplot2grid((2, 2), (1, 1))

    plot1.set_xlabel('Time')
    plot1.set_ylabel('IQ(amps)')
    plot1.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_left/current_setpoint_iq'], alpha=1, label="/drive_outputs/axis_front_left/current_setpoint_iq")
    plot1.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_left/current_measurement_iq'],"-o", alpha=0.1, label="/drive_outputs/axis_front_left/current_measurement_iq")
    plot1.tick_params(axis='y')
    ax2=plot1.twinx()
    ax2.set_ylabel('velocity commanded percent')
    ax2.plot(TimestampSeries, dataframe['/inputs/drive_inputs/velocity_left_cmd_percent'],"-g", alpha=.3, label="/drive_inputs/velocity_left_cmd_percent")
    ax2.tick_params(axis='y')
    plot1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plot1.set_title('Iq Current Front Left')

    plot2.set_xlabel('Time')
    plot2.set_ylabel('IQ(amps)')
    plot2.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_right/current_setpoint_iq'], alpha=1, label="axis_front_right/current_setpoint_iq")
    plot2.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_right/current_measurement_iq'],"-o", alpha=0.1, label="axis_front_left/current_measurement_iq")
    plot2.tick_params(axis='y')
    ax2=plot2.twinx()
    ax2.set_ylabel('velocity commanded percent')
    ax2.plot(TimestampSeries, dataframe['/inputs/drive_inputs/velocity_right_cmd_percent'],"-g", alpha=.3, label="velocity left percentage")
    ax2.tick_params(axis='y')
    plot2.legend(loc='upper right')
    ax2.legend(loc='upper left')
    plot2.set_title('Iq Current Front Right')

    plot3.set_xlabel('Time')
    plot3.set_ylabel('IQ(amps)')
    plot3.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_left/current_setpoint_iq'], alpha=1, label='rear left current setpoint')
    plot3.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_left/current_measurement_iq'], "-o", alpha=.1, label='rear left current measurement')
    plot3.tick_params(axis='y')
    ax2=plot3.twinx()
    ax2.set_ylabel('velcity commanded percent')
    ax2.plot(TimestampSeries, dataframe['/inputs/drive_inputs/velocity_left_cmd_percent'],"-g", alpha=.3, label="velocity left percentage")
    ax2.tick_params(axis='y')
    plot3.legend(loc='upper right')
    ax2.legend(loc='upper left')
    plot3.set_title('Iq Current Rear Left')


    plot4.set_xlabel('Time')
    plot4.set_ylabel('IQ(amps)')
    plot4.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_right/current_setpoint_iq'], alpha=1, label='rear right current setpoint')
    plot4.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_right/current_measurement_iq'], "-o", alpha=.1, label='rear right current measurement')
    plot4.tick_params(axis='y')
    ax2=plot4.twinx()
    ax2.set_ylabel('velcity commanded percent')
    ax2.plot(TimestampSeries, dataframe['/inputs/drive_inputs/velocity_right_cmd_percent'],"-g", alpha=.3, label="velocity right percentage")
    ax2.tick_params(axis='y')
    plot4.legend(loc='upper right')
    ax2.legend(loc='upper left')
    plot4.set_title('Iq Current Rear Right')
    plt.show()    

def dm_motor_temp(dataframe, TimestampSeries):
    plt.figure(figsize=(9,4))
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_right/motor_temp_degC'], label="/drive_outputs/axis_front_right_motor_temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_left/motor_temp_degC'], label="/drive_outputs/axis_front_left/motor_temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_right/motor_temp_degC'], label="/drive_outputs/axis_rear_right/motor_temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_left/motor_temp_degC'], label="/drive_outputs/axis_rear_left/motor_temp_degC")
    plt.legend(loc="best")
    plt.title('Motor Temps(Degree C)')
    plt.xlabel('Time')
    plt.ylabel('Temperature C')
    plt.ylim(0,100)
    plt.show()

def dm_inverter_temp(dataframe, TimestampSeries):
    plt.figure(figsize=(9,4))
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_left/inverter_temp_degC'], label="/drive_outputs/axis_rear_left/inverter_temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_right/inverter_temp_degC'], label="/drive_outputs/axis_rear_right/inverter_temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_left/inverter_temp_degC'], label="/drive_outputs/axis_front_left/inverter_temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_right/inverter_temp_degC'], label="/drive_outputs/axis_front_right/inverter_temp_degC")
    plt.legend(loc="best")
    plt.title('Motor Inverter Temp (Degree C)')
    plt.xlabel('Time')
    plt.ylabel('Temperature C')
    plt.ylim(0,100)
    plt.show()

def dm_brake_temp(dataframe, TimestampSeries):  
    plt.figure(figsize=(9,4))
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_left/brake_temp_degC'], label="/drive_outputs/axis_rear_left/brake_temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_rear_right/brake_temp_degC'], label="/drive_outputs/axis_rear_right/brake_temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_right/brake_temp_degC'], label="/drive_outputs/axis_front_right/brake_temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/drive_outputs/axis_front_left/brake_temp_degC'], label="/drive_outputs/axis_front_left/brake_temp_degC")
    plt.legend(loc="best")
    plt.title('Motor Brake Temp (Degree C)')
    plt.xlabel('Time')
    plt.ylabel('Temperature C')
    plt.ylim(0,100)
    plt.show()

def dmhumidity(dataframe, TimestampSeries): 
    plt.figure(figsize=(10,9))
    plot1=plt.subplot2grid((2,2), (0,0), colspan=2)
    plot2=plt.subplot2grid((2,2), (1,0), colspan=2)

    plot1.plot(TimestampSeries, dataframe['/inputs/drive_outputs/axis_front_left/rh_percent'], label="drive_outputs axis_front_left/rh_percent")
    plot1.plot(TimestampSeries, dataframe['/inputs/drive_outputs/axis_front_right/rh_percent'], label="drive_outputs axis_front_right/rh_percent")
    plot1.plot(TimestampSeries, dataframe['/inputs/drive_outputs/axis_rear_left/rh_percent'], label="drive_outputs axis_rear_left_/rh_percent")
    plot1.plot(TimestampSeries, dataframe['/inputs/drive_outputs/axis_rear_right/rh_percent'], label="drive_outputs axis_rear_right/rh_percent")
    plot1.set_title('Robot Relative Humidity')
    plot1.legend()
    

    plot2.set_xlabel("Time")
    plot2.set_ylabel("Dewpoint")
    plot2.plot(TimestampSeries, dataframe['/inputs/drive_outputs/axis_front_left/dewpoint_degC'], label="drive_outputs axis_front_left/dewpoint_degC")
    plot2.plot(TimestampSeries, dataframe['/inputs/drive_outputs/axis_front_right/dewpoint_degC'], label="drive_outputs axis_front_right/dewpoint_degC")
    plot2.plot(TimestampSeries, dataframe['/inputs/drive_outputs/axis_rear_left/dewpoint_degC'], label="drive_outputs axis_rear_left_/dewpoint_degC")
    plot2.plot(TimestampSeries, dataframe['/inputs/drive_outputs/axis_rear_right/dewpoint_degC'], label="drive_outputs axis_rear_right/dewpoint_degC")
    plot2.set_title('Robot Dewpoint')
    plot2.legend()
    plt.show()

def cbtemp(dataframe, TimestampSeries):
    plt.figure(figsize=(9,4))
    plt.plot(TimestampSeries,dataframe['/inputs/toque_outputs/aos_cold_degC'], label="/toque_outputs/aos_cold_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/hvdcdc_outputs/vicor_temp_degC'], label="/hvdcdc_outputs/vicor_temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/hvdcdc_outputs/ambient_temp_degC'],label="/hvdcdc_outputs/ambient_temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/brain_outputs/temp_degC'], label="/brain_outputs/temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/brain_outputs/sfp1/temp_degC'], label="/brain_outputs/sfp1/temp_degC")
    plt.plot(TimestampSeries,dataframe['/inputs/brain_outputs/sfp2/temp_degC'], label="/brain_outputs/sfp2/temp_degC")
    plt.legend()
    plt.title('CB Internal Thermals C')
    plt.show()
    
def CBhumidity(dataframe, TimestampSeries):
    plt.figure(figsize=(10,9))
    plot1=plt.subplot2grid((2,2), (0,0), colspan=2)
    plot2=plt.subplot2grid((2,2), (1,0), colspan=2)

    plot1.set_xlabel("Time")
    plot1.set_ylabel("Relative Humidity")
    plot1.plot(TimestampSeries, dataframe['/inputs/brain_outputs/rel_humidity_percent'], label="brain_outputs rel_humidity_percent")
    plot1.plot(TimestampSeries, dataframe['/inputs/hvdcdc_outputs/relative_humidity_percent'], label="hvdcdc_outputs relative_humdity_percent")
    plot1.set_title('CenterBody Relative Humidity')
    plot1.legend()
    
    plot2.set_xlabel("Time")
    plot2.set_ylabel("Dewpoint")
    plot2.plot(TimestampSeries, dataframe['/inputs/brain_outputs/dewpoint_degC'], label="brain_outputs dewpoint_degC")
    plot2.plot(TimestampSeries, dataframe['/inputs/hvdcdc_outputs/dewpoint_degC'], label="hvdcdc_outputs dewpoint_degC")
    plot2.set_title('Centerbody Dewpoint')
    plot2.legend()
    plt.show()

def CBcurrent(dataframe, TimestampSeries):
    plt.figure(figsize=(9,4))
    plt.plot(TimestampSeries, dataframe['/inputs/hvdcdc_outputs/drive_current_mA'], label="Drive Current mA")
    plt.plot(TimestampSeries, dataframe['/inputs/hvdcdc_outputs/brain_current_mA'], label="Brain Current mA")
    plt.xlabel("Time")   
    plt.ylabel("mA")
    plt.legend()
    plt.show()

