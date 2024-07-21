# cd /mnt/c/Users/emily/Documents/projects/algo-vis-code/algorithm-visualiser

import tkinter as tk

window = tk.Tk()
window.title("Algorithm Visualiser")

# Fullscreen mode
window.state("zoomed")

label = tk.Label(text="Algorithm Visualiser")
label.pack()

window.mainloop()