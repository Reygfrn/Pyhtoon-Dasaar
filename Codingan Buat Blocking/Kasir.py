import tkinter as tk
from tkinter import messagebox

def hitung_total():
    try:
        harga = float(entry_harga.get())
        kuantitas = int(entry_kuantitas.get())
        total = harga * kuantitas
        label_total.config(text=f"Total: Rp.{total:,.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Harap masukkan angka yang valid!")

window = tk.Tk()
window.title("Hitung Total")
window.geometry("300x200")

label_harga = tk.Label(window, text="Harga:")
label_harga.pack()
entry_harga = tk.Entry(window)
entry_harga.pack()

label_kuantitas = tk.Label(window, text="Kuantitas:")
label_kuantitas.pack()
entry_kuantitas = tk.Entry(window)
entry_kuantitas.pack()

button_hitung = tk.Button(window, text="Hitung Total", command=hitung_total)
button_hitung.pack()

label_total = tk.Label(window, text="Total: Rp.0.00")
label_total.pack()

window.mainloop()