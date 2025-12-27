import time

import pyvisa
import BKP_9141

def powerCycleAll(instrument_in):
    #Turn channel 0 off
    instrument_in.query('INST 0')
    instrument_in.query('OUTP 0')

    #Turn channel 1 off
    instrument_in.query('INST 1')
    instrument_in.query('OUTP 0')


    time.sleep(5)

    #Turn channel 0 off
    instrument_in.query('INST 0')
    instrument_in.query('OUTP 1')



    #Turn channel 1 off
    #instrument_in.query('INST 1')
    #instrument_in.query('OUTP 1')


rm = pyvisa.ResourceManager()
rm.list_resources()

my_instrument = rm.open_resource('USB0::0x3121::0x0002::579I23132::INSTR')

#Put all channels in single mode
#my_instrument.query('OUTP:PAIR OFF')
powerCycleAll(my_instrument)