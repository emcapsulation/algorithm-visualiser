import tkinter as tk

BG_COLOUR = "#2b2b28"
NEON_GREEN = "#11ed4b"


def go_to_algorithm_screen(algo_choice):
	print(algo_choice)


def main():
	# Main window setup
	window = tk.Tk()
	window.title("Algorithm Visualiser")
	window.configure(background=BG_COLOUR)
	window.state("zoomed")


	# Main heading
	heading = tk.Label(text="Algorithm Visualiser")
	heading.configure(
		background=BG_COLOUR,
		font=("Consolas", 26),
		fg="white")
	heading.place(relx=0.5, rely=0.1, anchor="center")


	# Drop down with algorithm selection
	ALGORITHM_CHOICES = [
		"Sorting",
		"Path finding",
		"Tree traversal"
	]

	algo_dropdown = tk.StringVar(window)
	algo_dropdown.set(ALGORITHM_CHOICES[0])

	dropdown = tk.OptionMenu(window, algo_dropdown, *ALGORITHM_CHOICES)
	dropdown.place(relx=0.5, rely=0.5, anchor="center")
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
	vis_button = tk.Button(window, text="Visualise", command=lambda: go_to_algorithm_screen(algo_dropdown.get()))
	vis_button.configure(
		background=NEON_GREEN,
		font=("Consolas", 20),	
		cursor="hand2")
	vis_button.place(relx=0.5, rely=0.9, anchor="center")

	window.mainloop()

main()