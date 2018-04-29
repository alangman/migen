# This file is Copyright (c) 2016 Ivan Uvarov <flashcactus@ya.ru>
# License: BSD
#
# Note: This file maps only the buttons, switches, LEDs and GPIO headers;
# the actual devboard has much more than that.

from migen.build.generic_platform import *
from migen.build.altera import AlteraPlatform
from migen.build.altera.programmer import USBsvf


_io = [
    ("clk12M", 0, Pins("H6"), IOStandard("3.3-V LVTTL")),

    ("user_led", 0, Pins("A8"), IOStandard("3.3-V LVTTL")),
    ("user_led", 1, Pins("A9"), IOStandard("3.3-V LVTTL")),
    ("user_led", 2, Pins("A11"), IOStandard("3.3-V LVTTL")),
    ("user_led", 3, Pins("A10"), IOStandard("3.3-V LVTTL")),
    ("user_led", 4, Pins("B10"), IOStandard("3.3-V LVTTL")),
    ("user_led", 5, Pins("C9"), IOStandard("3.3-V LVTTL")),
    ("user_led", 6, Pins("C10"), IOStandard("3.3-V LVTTL")),
    ("user_led", 7, Pins("D8"), IOStandard("3.3-V LVTTL")),

    ("user_btn", 7, Pins("E6"), IOStandard("3.3-V LVTTL")),


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
        AlteraPlatform.__init__(self, "10M08SAU169C8G", _io)

    def create_programmer(self):
        return USBsvf()
