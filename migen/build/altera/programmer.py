import subprocess

from migen.build.generic_programmer import GenericProgrammer


class USBBlaster(GenericProgrammer):
    needs_bitreverse = False

    def __init__(self, cable_name="Arrow-USB-Blaster", device_id=1):
        self.cable_name = cable_name
        self.device_id = device_id

    def load_bitstream(self, bitstream_file, cable_suffix=""):
        print("{}{}".format(self.cable_name, cable_suffix))
        print("p;{}@{}".format(bitstream_file, self.device_id))
        subprocess.call(["quartus_pgm", "-m", "jtag", "-c",
                         "{}{}".format(self.cable_name, cable_suffix), "-o",
                         "p;{}@{}".format(bitstream_file, self.device_id)])

class USBArrowBlaster(GenericProgrammer):
    needs_bitreverse = False

    def __init__(self):
        pass

    def load_bitstream(self, bitstream_file):
        print("Loading bitsteam {} ".format(bitstream_file))
        cmd = "xsvftool-ft232h -C A -s {}".format(bitstream_file)
        subprocess.call(["xsvftool-ft232h", "-C","A","-s","{}".format(bitstream_file)])
        print("[done]")

