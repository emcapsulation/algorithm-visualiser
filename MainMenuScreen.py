import tkinter as tk

from constants import *

class MainMenuScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, background=BG_COLOUR)

        self.decorate_screen(master)
        

    def decorate_screen(self, master):
        # Main heading
        heading = tk.Label(self, text="Algorithm Visualiser")
        heading.configure(
          background=BG_COLOUR,
          font=("Consolas", 26),
          fg="white")
        heading.pack(fill=tk.BOTH, pady=50)


        # Drop down with algorithm selection
        ALGORITHM_CHOICES = [
          "Sorting",
          "Path finding",
          "Tree traversal"
        ]

        algo_dropdown = tk.StringVar(self)
        algo_dropdown.set(ALGORITHM_CHOICES[0])

        dropdown = tk.OptionMenu(self, algo_dropdown, *ALGORITHM_CHOICES)
        dropdown.pack(fill=tk.BOTH, pady=100)
        dropdown.configure(
          background=BG_COLOUR,
          fg="white",
          font=("Consolas", 20),
          width=40)

        dropdown["menu"].configure(
          background=BG_COLOUR,
          fg="white",
          font=("Consolas", 20))


        # Button to proceed
        vis_button = tk.Button(self, text="Visualise", command=lambda: master.switch_frame(algo_dropdown.get()))
        vis_button.configure(
          background=NEON_GREEN,
          font=("Consolas", 20),  
          cursor="hand2")
        vis_button.pack(fill=tk.BOTH, pady=25)


if __name__ == "__main__":
    app = MainMenuScreen()
    app.mainloop()