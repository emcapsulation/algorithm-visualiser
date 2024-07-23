import tkinter as tk

from MainMenuScreen import MainMenuScreen

from constants import *

pages = {
    "MainMenuScreen": MainMenuScreen
}

class App(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)

		self.window_config()	

		self._frame = None
		self.switch_frame("MainMenuScreen")


	def switch_frame(self, page_name):
		cls = pages[page_name]
		new_frame = cls(master = self)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = new_frame
		self._frame.pack()


	def window_config(self):
		self.title("Algorithm Visualiser")
		self.configure(background=BG_COLOUR)
		self.state("zoomed")


if __name__ == "__main__":
    app = App()
    app.mainloop()
