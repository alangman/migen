from migen.build.generic_platform import *
from migen.build.lattice import LatticePlatform
from migen.build.lattice.programmer import IceStormProgrammer

_io = [
    ("user_led", 0, Pins("12"), IOStandard("LVCMOS33")),

    ("status_led", 0,
        Subsignal("blue", Pins("39"), IOStandard("LVCMOS33")),
        Subsignal("green", Pins("40"), IOStandard("LVCMOS33")),
        Subsignal("red", Pins("41"), IOStandard("LVCMOS33"))
    ),

    ("spiflash", 0,
        Subsignal("cs_n", Pins("16"), IOStandard("LVCMOS33")),
        Subsignal("clk",  Pins("15"), IOStandard("LVCMOS33")),
        Subsignal("mosi", Pins("14"), IOStandard("LVCMOS33")),
        Subsignal("miso", Pins("17"), IOStandard("LVCMOS33"))
    ),

    ("serial",0,
        Subsignal("cts",Pins("23")),
        Subsignal("rts",Pins("25")),
        Subsignal("tx",Pins("26")),
        Subsignal("rx",Pins("27")),
        IOStandard("LVCMOS33")
    )
]

_connectors = [
    #Pin 3-16, Pin 8 -> IOT_46B_G0(35), Pin  10 -> IOT_45A_G1(37)
    ("JP5", "23 25 26 27 32 35 31 37 34 43 36 42 38 28"),  
    #Pin 1-16 Pin 9 -> IOB_3B_G6(44)
    ("JP6", "12 21 13 19 18 11 10 9 6 44 4 3 48 45 47 44 46 2"),  
    #TP4 -> IOB_25B_G3 (20)
    ("TP","20 10")
]


class Platform(LatticePlatform):
    default_clk_name = "clk48MHz"
    default_clk_period = 21
    def __init__(self):
        LatticePlatform.__init__(self, "ice40-up5k-sg48", _io, _connectors,
                                 toolchain="icestorm")

    def create_programmer(self):
        return IceStormProgrammer()
