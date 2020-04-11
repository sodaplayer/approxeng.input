from approxeng.input import Controller, Button, BinaryAxis, CentredAxis

__all__ = ['SwitchProController']

#  Generic HID
#  class WirelessSwitchProController(Controller):

    #  def __init__(self, dead_zone=0.05, hot_zone=0.05):
        #  """
        #  Create a new Nintendo Switch Pro Controller instance

        #  :param float dead_zone:
            #  Used to set the dead zone for each :class:`approxeng.input.CentredAxis`
            #  in the controller.
        #  :param float hot_zone:
            #  Used to set the hot zone for each :class:`approxeng.input.CentredAxis`
            #  in the controller.
        #  """
        #  super(WirelessSwitchProController, self).__init__(
            #  controls=[
                #  Button("X", 307, sname="circle"),
                #  Button("Y", 306, sname="triangle"),
                #  Button("B", 304, sname="square"),
                #  Button("A", 305, sname="cross"),
                #  Button("Right Stick", 315, sname='rs'),
                #  Button("Left Stick", 314, sname='ls'),
                #  Button("Plus", 313, sname='start'),
                #  Button("Minus", 312, sname='select'),
                #  Button("Home", 316, sname='home'),
                #  Button("Capture", 317, sname='capture'),
                #  Button("L", 308, sname='l1'),
                #  Button("R", 309, sname='r1'),
                #  Button("LZ", 310, sname='l2'),
                #  Button("RZ", 311, sname='r2'),
                #  BinaryAxis("D-pad Horizontal", 16, b1name='dleft', b2name='dright'),
                #  BinaryAxis("D-pad Vertical", 17, b1name='dup', b2name='ddown'),
                #  CentredAxis("Left Horizontal", 0, 65535, 0, sname="lx"),
                #  CentredAxis("Left Vertical", 0, 65535, 1, sname="ly"),
                #  CentredAxis("Right Horizontal", 0, 65535, 3, sname="rx"),
                #  CentredAxis("Right Vertical", 0, 65535, 4, sname="ry")
            #  ],
            #  dead_zone=dead_zone,
            #  hot_zone=hot_zone)

    #  @staticmethod
    #  def registration_ids():
        #  """
        #  :return: list of (vendor_id, product_id) for this controller
        #  """
        #  return [(0x57e, 0x2009)]

    #  def __repr__(self):
        #  return 'Nintendo Switch Pro Controller'

class WiredSwitchProController(Controller):

    def __init__(self, dead_zone=0.05, hot_zone=0.05):
        """
        Create a new Nintendo Switch Pro Controller instance

        :param float dead_zone:
            Used to set the dead zone for each :class:`approxeng.input.CentredAxis`
            in the controller.
        :param float hot_zone:
            Used to set the hot zone for each :class:`approxeng.input.CentredAxis`
            in the controller.
        """
        super(WiredSwitchProController, self).__init__(
            controls=[
                Button("X", 307, sname="circle"),
                Button("Y", 308, sname="triangle"),
                Button("B", 305, sname="square"),
                Button("A", 304, sname="cross"),
                Button("Right Stick", 318, sname='rs'),
                Button("Left Stick", 317, sname='ls'),
                Button("Plus", 315, sname='start'),
                Button("Minus", 314, sname='select'),
                Button("Home", 316, sname='home'),
                Button("Capture", 309, sname='capture'),
                Button("L", 310, sname='l1'),
                Button("R", 311, sname='r1'),
                Button("LZ", 312, sname='l2'),
                Button("RZ", 313, sname='r2'),
                BinaryAxis("D-pad Horizontal", 16, b1name='dleft', b2name='dright'),
                BinaryAxis("D-pad Vertical", 17, b1name='dup', b2name='ddown'),
                CentredAxis("Left Horizontal", -32767, 32767, 0, sname="lx"),
                CentredAxis("Left Vertical", -32767, 32767, 1, sname="ly", invert=True),
                CentredAxis("Right Horizontal", -32767, 32767, 3, sname="rx"),
                CentredAxis("Right Vertical", -32767, 32767, 4, sname="ry", invert=True)
            ],
            node_mappings={'Nintendo Switch Pro Controller IMU': 'motion'},
            dead_zone=dead_zone,
            hot_zone=hot_zone)

    @staticmethod
    def registration_ids():
        """
        :return: list of (vendor_id, product_id) for this controller
        """
        return [(0x57e, 0x2009)]

    def __repr__(self):
        return 'Nintendo Switch Pro Controller'
