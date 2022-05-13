from PyQt5.QtWidgets import *
from view import Ui_MainWindow
from classes import *


class Controller(QMainWindow, Ui_MainWindow):
    """
    Class representing the controller object.
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Constructor which sets the default attributes for Controller.
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        """
        Buttons regarding the Television's attributes are disabled initially.
        """
        self.button_power.setEnabled(False)
        self.button_c_up.setEnabled(False)
        self.button_c_down.setEnabled(False)
        self.button_v_up.setEnabled(False)
        self.button_v_down.setEnabled(False)

        self.button_values.clicked.connect(lambda: self.enter_values())

        self.button_power.clicked.connect(lambda: self.power_status())

        self.button_c_up.clicked.connect(lambda: self.ch_up())
        self.button_c_down.clicked.connect(lambda: self.ch_down())
        self.button_v_up.clicked.connect(lambda: self.vol_up())
        self.button_v_down.clicked.connect(lambda: self.vol_down())

        self.tv = Television()  # Creating a Television object

    def off_state(self) -> None:
        """
        Method that sets the Television's off state. The 'Enter' button
        is enabled and all buttons regarding the Television's
        attributes are disabled. Called whenever the Television is powered off.
        """
        self.button_values.setEnabled(True)

        self.button_power.setEnabled(False)
        self.button_c_up.setEnabled(False)
        self.button_c_down.setEnabled(False)
        self.button_v_up.setEnabled(False)
        self.button_v_down.setEnabled(False)

    def on_state(self) -> None:
        """
        Method that sets the Television's on state. All buttons regarding the Television's
        attributes are enabled. Called whenever the Television is powered on.
        """
        self.button_power.setEnabled(True)
        self.button_c_up.setEnabled(True)
        self.button_c_down.setEnabled(True)
        self.button_v_up.setEnabled(True)
        self.button_v_down.setEnabled(True)

    def disable_spin_boxes(self) -> None:
        """
        Method that disables all spin boxes in order to prevent
        the user from changing the Television's channel and volume
        attributes while the Television is still on. Called whenever
        the Television is turned on.
        """
        self.spinBox_max_c.setEnabled(False)
        self.spinBox_min_c.setEnabled(False)

        self.spinBox_max_v.setEnabled(False)
        self.spinBox_min_v.setEnabled(False)

    def enable_spin_boxes(self) -> None:
        """
        Method that enabled all spin boxes in order to allow
        the user to reconfigure the Television's channel and volume
        attributes. Called whenever the Television is turned off.
        """
        self.spinBox_min_c.setEnabled(True)
        self.spinBox_max_c.setEnabled(True)

        self.spinBox_max_v.setEnabled(True)
        self.spinBox_min_v.setEnabled(True)

    def enter_values(self) -> None:
        """
        Method that confirms the user selected configurations for the
        Television's channel and volume attributes. Can only be called
        while the Television is turned off. Will only enable the Television's
        'On/Off' button if the user selected configurations for the
        Television's channel and volume attributes are valid.
        """
        if self.button_power.text() == "Off" \
                and self.spinBox_min_c.value() <= self.spinBox_max_c.value() \
                and self.spinBox_min_v.value() <= self.spinBox_max_v.value():
            self.button_values.setText('Valid \n Press Power \n On/Off')
            self.button_power.setEnabled(True)
            self.display_current_channel.display(self.spinBox_min_c.value())
            self.display_current_volume.display(self.spinBox_min_v.value())

            self.tv.__init__(c_min=self.spinBox_min_c.value(), c_max=self.spinBox_max_c.value(),
                             v_min=self.spinBox_min_v.value(), v_max=self.spinBox_max_v.value())

        elif self.button_power.text() == "On":
            self.button_values.setText("Turn Power Off")
        else:
            self.button_values.setText('Invalid \n Try Again')

    def power_status(self) -> None:
        """
        Method which changes the power state of the Television between
        'On' and 'Off'. Called whenever the Television's power button
        is enabled and is pressed by the user.
        """
        if self.button_values.text() == "Valid \n Press Power \n On/Off":
            self.button_values.setText('Enter')
            self.button_values.setEnabled(False)
            if self.button_power.text() == "Off":
                self.button_power.setText('On')

                Controller.disable_spin_boxes(self)
                Controller.on_state(self)

                self.tv.power()

            else:
                self.button_power.setText('Off')
                Controller.enable_spin_boxes(self)
                Controller.off_state(self)

                self.tv.power()

        elif self.button_values.text() == "Turn Power Off":
            self.button_values.setText('Enter')
            self.button_power.setText('Off')
            Controller.enable_spin_boxes(self)
            Controller.off_state(self)

            self.tv.power()

        else:
            if self.button_power.text() == "Off":
                self.button_power.setText('On')
                Controller.disable_spin_boxes(self)
                Controller.on_state(self)

                self.tv.power()

            else:
                self.button_power.setText('Off')
                Controller.enable_spin_boxes(self)
                Controller.off_state(self)

                self.tv.power()

    def ch_up(self) -> None:
        """
        Method that uses the Television's 'channel_up()' method to
        increase the displayed channel value according to the method.
        Called when the channel up button is pressed by the user.
        """
        if self.button_power.text() == "On":
            self.tv.channel_up()
            self.display_current_channel.display(self.tv.get_channel())

    def ch_down(self) -> None:
        """
        Method that uses the Television's 'channel_down()' method to
        decrease the displayed channel value according to the method.
        Called when the channel down button is pressed by the user.
        """
        if self.button_power.text() == "On":
            self.tv.channel_down()
            self.display_current_channel.display(self.tv.get_channel())

    def vol_up(self) -> None:
        """
        Method that uses the Television's 'volume_up()' method to
        increase the displayed volume value according to the method.
        Called when the volume up button is pressed by the user.
        """
        if self.button_power.text() == "On":
            self.tv.volume_up()
            self.display_current_volume.display(self.tv.get_volume())

    def vol_down(self) -> None:
        """
        Method that uses the Television's 'volume_down()' method to
        decrease the displayed volume value according to the method.
        Called when the volume down button is pressed by the user.
        :return:
        """
        if self.button_power.text() == "On":
            self.tv.volume_down()
            self.display_current_volume.display(self.tv.get_volume())
