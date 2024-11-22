import tkinter as tk
root = tk.Tk()
label1 = tk.Label(root, text="label 1")
label2 = tk.Label(root, text=" label 2")
label3 = tk.Label(root, text=" label 3")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2)
root.mainloop()