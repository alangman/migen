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


    ("gpio_0", 0,
        Pins(""),
        IOStandard("3.3-V LVTTL")
    ),
    ("gpio_1", 0,
        Pins(""),
        IOStandard("3.3-V LVTTL")
    ),
]


class Platform(AlteraPlatform):
    default_clk_name = "clk12M"
    default_clk_period = 83.333

    def __init__(self):
        AlteraPlatform.__init__(self, "10CL025YU256C8G", _io)

    def create_programmer(self):
        return USBArrowBlaster()
