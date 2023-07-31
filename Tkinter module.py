import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Graphic Model with Tkinter")

# Create a canvas widget to draw on
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw a rectangle on the canvas
rect = canvas.create_rectangle(50, 50, 200, 150, fill="blue")

# Draw an oval on the canvas
oval = canvas.create_oval(250, 50, 350, 150, fill="red")

# Draw a line on the canvas
line = canvas.create_line(50, 200, 350, 200, fill="green", width=3)

# Start the main event loop
root.mainloop()
