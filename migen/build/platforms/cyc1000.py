# This file is Copyright (c) 2016 Ivan Uvarov <flashcactus@ya.ru>
# License: BSD
#
# Note: This file maps only the buttons, switches, LEDs and GPIO headers;
# the actual devboard has much more than that.

from migen.build.generic_platform import *
from migen.build.altera import AlteraPlatform
from migen.build.altera.programmer import USBBlaster,USBArrowBlaster


_io = [
    ("clk12M", 0, Pins("M2"), IOStandard("3.3-V LVTTL")),

    ("user_led", 0, Pins("M6"), IOStandard("3.3-V LVTTL")),
    ("user_led", 1, Pins("T4"), IOStandard("3.3-V LVTTL")),
    ("user_led", 2, Pins("T3"), IOStandard("3.3-V LVTTL")),
    ("user_led", 3, Pins("R3"), IOStandard("3.3-V LVTTL")),
    ("user_led", 4, Pins("T2"), IOStandard("3.3-V LVTTL")),
    ("user_led", 5, Pins("R4"), IOStandard("3.3-V LVTTL")),
    ("user_led", 6, Pins("N5"), IOStandard("3.3-V LVTTL")),
    ("user_led", 7, Pins("N3"), IOStandard("3.3-V LVTTL")),

    ("user_btn", 7, Pins("N6"), IOStandard("3.3-V LVTTL")),


    ("epcs", 0,
        Subsignal("data0", Pins("H2")),
        Subsignal("asd0", Pins("C1")),
        Subsignal("dclk", Pins("H1")),
        Subsignal("ncs", Pins("D2")),
        IOStandard("3.3-V LVTTL")
    ),

    ("sdram", 0,
        Subsignal("a", Pins("A3 B5 B4 B3 C3 D3 E6 E7 D6 D8 A5")),
        Subsignal("ba", Pins("A4 B6")),
        Subsignal("clk", Pins("B14")),
        Subsignal("cke", Pins("F8")),
        Subsignal("ras_n", Pins("B7")),
        Subsignal("cas_n", Pins("C8")),
        Subsignal("we_n", Pins("A7")),
        Subsignal("cs_n", Pins("A6")),
        Subsignal("dq", Pins("B10 A10 B11 A11 A12 D9 B12 C9 D11 E11 A15 E9 D14 F9 C14 A14")),
        Subsignal("dqm", Pins("B13 D12")),
        IOStandard("3.3-V LVTTL")
    ),

    ("lis3dh",0,
        Subsignal("int1", Pins("B1")),
        Subsignal("int2", Pins("C2")),
        Subsignal("sdi",  Pins("G2")),
        Subsignal("sdo",  Pins("G1")),
        Subsignal("spc",  Pins("F3")),
        Subsignal("cs",   Pins("D1")),
        IOStandard("3.3-V LVTTL")
    ),

    ("ft2232_bdbus", 0, Pins("R7"),IOStandard("3.3-V LVTTL")),
    ("ft2232_bdbus", 1, Pins("T7"),IOStandard("3.3-V LVTTL")),
    ("ft2232_bdbus", 2, Pins("R6"),IOStandard("3.3-V LVTTL")),
    ("ft2232_bdbus", 3, Pins("T6"),IOStandard("3.3-V LVTTL")),
    ("ft2232_bdbus", 4, Pins("R5"),IOStandard("3.3-V LVTTL")),
    ("ft2232_bdbus", 5, Pins("T5"),IOStandard("3.3-V LVTTL"))
]

_connectors = [
    ("J1",{
        "AREF":"P11",    #Pin 1
        "AIN0":"R12",
        "AIN1":"T13",
        "AIN2":"R13",
        "AIN3":"T14",
        "AIN4":"P14",
        "AIN5":"R14",
        "AIN6":"T15",
        "D0"  :"N16",
        "D1"  :"L15",
        "D2"  :"L16",
        "D3"  :"K15",
        "D4"  :"K16",
        "D5"  :"J14"    #Pin 14
        }    
    ),
    ("J2",{
        "5V"    :"PWR",    #Pin 1
        "VIN"   :"PWR",
        "3.3V"  :"PWR",
        "GND"   :"PWR",
        "RESET" :"IO",
        "D14"   :"R1",
        "D13"   :"P1",
        "D12"   :"L2",
        "D11"   :"K2",
        "D10"   :"J2",
        "D9"    :"J1",
        "D8"    :"P2",
        "D7"    :"N1",
        "D6"    :"N2"    #Pin 14
        }
    ),
    ("PMOD",{
        "PIO_01":"F13",    #Pin 1
        "PIO_02":"F15",
        "PIO_03":"F16",
        "PIO_04":"D16",
        "GND_05":"PWR",
        "3.3V_06":"PWR",
        "PIO_05":"D15",
        "PIO_06":"C15",
        "PIO_07":"B16",
        "PIO_08":"C16",
        "GND_11":"PWR",
        "3.3V_12":"PWR"    #Pin 12
        }
    )
]


class Platform(AlteraPlatform):
    default_clk_name = "clk12M"
    default_clk_period = 83.333

    def __init__(self):
        AlteraPlatform.__init__(self, "10CL025YU256C8G", _io,_connectors)

    def create_programmer(self):
        return USBArrowBlaster()
