import tkinter as tk
from tkinter import messagebox

data_pelanggan = []

def hitung_biaya():
    try:
        no_pol = entry_no_pol.get()
        waktu_masuk = int(entry_masuk.get())
        waktu_keluar = int(entry_keluar.get())

        if waktu_keluar < waktu_masuk:
            messagebox.showerror("Input Error", "Waktu keluar tidak boleh lebih kecil dari waktu masuk!")
            return

        biaya_per_jam = 2000
        durasi = waktu_keluar - waktu_masuk
        biaya = durasi * biaya_per_jam

        data_pelanggan.append({
            "no_pol": no_pol,
            "masuk": waktu_masuk,
            "keluar": waktu_keluar,
            "biaya": biaya
        })

        update_tabel()

        label_biaya.config(text=f"Biaya: Rp. {biaya:,.0f}")

    except ValueError:
        messagebox.showerror("Input Error", "Harap masukkan data yang valid!")

def cari_no_pol():
    no_pol = entry_cari.get()
    hasil = [p for p in data_pelanggan if p["no_pol"] == no_pol]

    if hasil:
        messagebox.showinfo("Hasil Pencarian", f"Nomor Polisi {no_pol} ditemukan!")
    else:
        messagebox.showinfo("Hasil Pencarian", f"Nomor Polisi {no_pol} tidak ditemukan.")

def update_tabel():
    for item in tabel_terakhir.get_children():
        tabel_terakhir.delete(item)

    for item in tabel_banyak_bayar.get_children():
        tabel_banyak_bayar.delete(item)

    for pelanggan in sorted(data_pelanggan, key=lambda x: x["keluar"], reverse=True):
        tabel_terakhir.insert("", tk.END, values=(pelanggan["no_pol"], pelanggan["masuk"], pelanggan["keluar"], f"Rp. {pelanggan['biaya']:,.0f}"))

    for pelanggan in sorted(data_pelanggan, key=lambda x: x["biaya"], reverse=True):
        tabel_banyak_bayar.insert("", tk.END, values=(pelanggan["no_pol"], pelanggan["masuk"], pelanggan["keluar"], f"Rp. {pelanggan['biaya']:,.0f}"))

window = tk.Tk()
window.title("Aplikasi Parkir Kelompok 6")
window.geometry("800x600")

label_title = tk.Label(window, text="Aplikasi Parkir Kelompok 6", font=("Arial", 16, "bold"))
label_title.pack()

frame_input = tk.Frame(window)
frame_input.pack(pady=10)

label_cari = tk.Label(frame_input, text="Cari NoPol:")
label_cari.grid(row=0, column=0, padx=5, pady=5)
entry_cari = tk.Entry(frame_input)
entry_cari.grid(row=0, column=1, padx=5, pady=5)
button_cari = tk.Button(frame_input, text="Cari", command=cari_no_pol)
button_cari.grid(row=0, column=2, padx=5, pady=5)

label_no_pol = tk.Label(frame_input, text="No Plat Polisi:")
label_no_pol.grid(row=1, column=0, padx=5, pady=5)
entry_no_pol = tk.Entry(frame_input)
entry_no_pol.grid(row=1, column=1, padx=5, pady=5)

label_masuk = tk.Label(frame_input, text="Waktu Masuk:")
label_masuk.grid(row=2, column=0, padx=5, pady=5)
entry_masuk = tk.Entry(frame_input)
entry_masuk.grid(row=2, column=1, padx=5, pady=5)

label_keluar = tk.Label(frame_input, text="Waktu Keluar:")
label_keluar.grid(row=3, column=0, padx=5, pady=5)
entry_keluar = tk.Entry(frame_input)
entry_keluar.grid(row=3, column=1, padx=5, pady=5)

label_biaya = tk.Label(frame_input, text="Biaya: Rp. 0", font=("Arial", 12, "bold"), fg="red")
label_biaya.grid(row=4, column=1, padx=5, pady=5)

button_hitung = tk.Button(frame_input, text="Hitung", command=hitung_biaya)
button_hitung.grid(row=4, column=2, padx=5, pady=5)

frame_tabel = tk.Frame(window)
frame_tabel.pack(pady=10)

label_tabel_terakhir = tk.Label(frame_tabel, text="List Pelanggan Urut Terakhir Keluar")
label_tabel_terakhir.grid(row=0, column=0, padx=10, pady=5)
tabel_terakhir = tk.ttk.Treeview(frame_tabel, columns=("no_pol", "masuk", "keluar", "biaya"), show="headings", height=10)
tabel_terakhir.grid(row=1, column=0, padx=10, pady=5)
tabel_terakhir.heading("no_pol", text="No Plat Polisi")
tabel_terakhir.heading("masuk", text="Masuk")
tabel_terakhir.heading("keluar", text="Keluar")
tabel_terakhir.heading("biaya", text="Biaya")

label_tabel_banyak_bayar = tk.Label(frame_tabel, text="List Pelanggan Banyak Bayar")
label_tabel_banyak_bayar.grid(row=0, column=1, padx=10, pady=5)
tabel_banyak_bayar = tk.ttk.Treeview(frame_tabel, columns=("no_pol", "masuk", "keluar", "biaya"), show="headings", height=10)
tabel_banyak_bayar.grid(row=1, column=1, padx=10, pady=5)
tabel_banyak_bayar.heading("no_pol", text="No Plat Polisi")
tabel_banyak_bayar.heading("masuk", text="Masuk")
tabel_banyak_bayar.heading("keluar", text="Keluar")
tabel_banyak_bayar.heading("biaya", text="Biaya")

window.mainloop()   