#!/usr/bin/env python3
import gifte_core_logic, gifte_core_io, tkinter, tkinter.filedialog
from tkinter import ttk

class Gifte_Tkinter:

    # Class Constants
    FRAME_PADDING = '0.5i'
    EMAIL_LABEL_TEXT = "Enter Sending Email:"
    PASSWORD_LABEL_TEXT = "Enter Email Password:"
    PASSWORD_SHOW = '*'
    CONFIG_LABEL_TEXT = "Enter Config Location:"
    CONFIG_BUTTON_TEXT = "Find File"
    CONFIG_EXTENSION=".txt"
    CONFIG_INITIAL="geconf"
    CONFIG_TITLE = "Config File Selector"
    CONFIG_TYPES = [("Config File", "*" + CONFIG_EXTENSION)]
    SENDMAIL_TEXT = "Send Mail"
    
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._root_window.title("Kurennon's Gift Exchanger")
        self._main_frame = ttk.Frame(self._root_window, padding = Gifte_Tkinter.FRAME_PADDING)
        self._email_label = ttk.Label(self._main_frame, text = Gifte_Tkinter.EMAIL_LABEL_TEXT)
        self._email_label.grid(column = 0, row = 0)
        self._email_input = ttk.Entry(self._main_frame)
        self._email_input.grid(column = 1, row = 0)
        self._password_label = ttk.Label(self._main_frame, text = Gifte_Tkinter.PASSWORD_LABEL_TEXT)
        self._password_label.grid(column = 0, row = 1)
        self._password_input = ttk.Entry(self._main_frame, show = Gifte_Tkinter.PASSWORD_SHOW)
        self._password_input.grid(column = 1, row = 1)
        self._config_label = ttk.Label(self._main_frame, text = Gifte_Tkinter.CONFIG_LABEL_TEXT)
        self._config_label.grid(column = 0, row = 2)
        self._config_input = ttk.Entry(self._main_frame)
        self._config_input.insert(0, Gifte_Tkinter.CONFIG_INITIAL
            + Gifte_Tkinter.CONFIG_EXTENSION)
        self._config_input.grid(column = 1, row = 2)
        self._config_file_button = ttk.Button(self._main_frame, text = Gifte_Tkinter.CONFIG_BUTTON_TEXT,
            command = self._find_config_file)
        self._config_file_button.grid(column = 3, row = 2)
        self._send_mail_button = ttk.Button(self._main_frame, text = Gifte_Tkinter.SENDMAIL_TEXT,
            command = self._sendmail)
        self._send_mail_button.grid(row = 3)
        self._main_frame.grid()
    
    def _find_config_file(self):
        filename = tkinter.filedialog.askopenfilename(defaultextension=Gifte_Tkinter.CONFIG_EXTENSION,
                            initialfile = Gifte_Tkinter.CONFIG_INITIAL, title=Gifte_Tkinter.CONFIG_TITLE,
                            filetypes=Gifte_Tkinter.CONFIG_TYPES)
        self._config_input.delete(0, len(self._config_input.get()))
        self._config_input.insert(0, filename)
        
    def _sendmail(self):
        title, people = gifte_core_io.load_preferences(self._config_input.get())
        credentials = [ self._email_input.get(), self._password_input.get() ]
        gifte_core_io.send_emails(gifte_core_logic.gift_designation(people), title, credentials)
        
    def run(self):
        self._root_window.mainloop()
    
if __name__ == "__main__":
    app = Gifte_Tkinter()
    app.run()
