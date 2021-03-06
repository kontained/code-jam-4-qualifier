"""
A GUI application for a rocketship launch control panel.
This application is built on tkinter. See the official
documentation and linked resources here:
    https://docs.python.org/3/library/tkinter.html

Requirements:
    Python 3.
"""
import tkinter as tk
from launch_helper import LaunchHelper


class RocketShipControlPanel(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.countdown = LaunchHelper()
        self.pilot = None
        self.pilot_label = None
        self.password = None
        self.password_label = None
        self.launch_button = None

    def create_form(self):
        """
        Create the input fields, labels,
        and buttons when called.
        """

        self.pilot_label = tk.Label(
            self,
            text="Pilot: ",
        )
        self.pilot = tk.Entry(
            self,
            width=30,
        )
        self.pilot_label.pack(side=tk.TOP)
        self.pilot.pack(side=tk.TOP)

        self.password_label = tk.Label(
            self,
            text="Password: ",
        )
        self.password = tk.Entry(
            self,
            width=30,
            show='*'
        )
        self.password_label.pack(side=tk.TOP)
        self.password.pack(side=tk.TOP)

        self.launch_button = tk.Button(
            self,
            text="Launch",
            command=self.do_countdown,
        )
        self.launch_button.pack(side=tk.BOTTOM)

    def do_countdown(self):
        """
        When the user clicks the login button, this callback
        is invoked. Make it do a countdown. The first time
        it is clicked, the button text should change to "3".
        The next time to "2", then to "1", and then to "LIFTOFF!".

        If the username or the password are blank, this
        callback should not do anything.
        """
        if not self.pilot.get() or not self.password.get():
            return

        self.countdown.increment_countdown()
        self.launch_button['text'] = self.countdown.get_countdown_text()


root = tk.Tk()
app = RocketShipControlPanel(master=root)
app.create_form()
app.mainloop()
