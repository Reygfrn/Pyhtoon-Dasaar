import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menyimpan data
def simpan_data():
    nama = entry_nama.get()
    tanggal_lahir = entry_tanggal_lahir.get()
    asal_sekolah = entry_asal_sekolah.get()
    nisn = entry_nisn.get()
    nama_ayah = entry_nama_ayah.get()
    nama_ibu = entry_nama_ibu.get()
    nomor_telepon = entry_telepon.get()
    alamat = text_alamat.get("1.0", tk.END).strip()

    if not nama or not tanggal_lahir or not asal_sekolah or not nisn:
        messagebox.showerror("Error", "Data tidak boleh kosong!")
        return

    messagebox.showinfo("Berhasil", f"Data siswa atas nama {nama} berhasil disimpan!")

    # Reset form setelah menyimpan
    hapus_data()

# Fungsi untuk menghapus data
def hapus_data():
    entry_nama.delete(0, tk.END)
    entry_tanggal_lahir.delete(0, tk.END)
    entry_asal_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_nama_ayah.delete(0, tk.END)
    entry_nama_ibu.delete(0, tk.END)
    entry_telepon.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

# Membuat jendela utama
window = tk.Tk()
window.title("Data Siswa Baru")
window.geometry("600x600")
window.configure(bg="#D1F1FF")

# Label judul
label_judul = tk.Label(window, text="DATA SISWA BARU", font=("Arial", 16, "bold"), bg="#D1F1FF", fg="black")
label_judul.pack(pady=10)

# Frame untuk form input
frame_form = tk.Frame(window, bg="#D1F1FF")
frame_form.pack(pady=10)

# Input Nama Lengkap
label_nama = tk.Label(frame_form, text="Nama Lengkap", bg="#D1F1FF")
label_nama.grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_nama = tk.Entry(frame_form, width=40)
entry_nama.grid(row=0, column=1, padx=10, pady=5)

# Input Tanggal Lahir
label_tanggal_lahir = tk.Label(frame_form, text="Tanggal Lahir", bg="#D1F1FF")
label_tanggal_lahir.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_tanggal_lahir = tk.Entry(frame_form, width=40)
entry_tanggal_lahir.grid(row=1, column=1, padx=10, pady=5)

# Input Asal Sekolah
label_asal_sekolah = tk.Label(frame_form, text="Asal Sekolah", bg="#D1F1FF")
label_asal_sekolah.grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_asal_sekolah = tk.Entry(frame_form, width=40)
entry_asal_sekolah.grid(row=2, column=1, padx=10, pady=5)

# Input NISN
label_nisn = tk.Label(frame_form, text="NISN", bg="#D1F1FF")
label_nisn.grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_nisn = tk.Entry(frame_form, width=40)
entry_nisn.grid(row=3, column=1, padx=10, pady=5)

# Input Nama Ayah
label_nama_ayah = tk.Label(frame_form, text="Nama Ayah", bg="#D1F1FF")
label_nama_ayah.grid(row=4, column=0, sticky="w", padx=10, pady=5)
entry_nama_ayah = tk.Entry(frame_form, width=40)
entry_nama_ayah.grid(row=4, column=1, padx=10, pady=5)

# Input Nama Ibu
label_nama_ibu = tk.Label(frame_form, text="Nama Ibu", bg="#D1F1FF")
label_nama_ibu.grid(row=5, column=0, sticky="w", padx=10, pady=5)
entry_nama_ibu = tk.Entry(frame_form, width=40)
entry_nama_ibu.grid(row=5, column=1, padx=10, pady=5)

# Input Nomor Telepon
label_telepon = tk.Label(frame_form, text="Nomor Telepon / HP", bg="#D1F1FF")
label_telepon.grid(row=6, column=0, sticky="w", padx=10, pady=5)
entry_telepon = tk.Entry(frame_form, width=40)
entry_telepon.grid(row=6, column=1, padx=10, pady=5)

# Input Alamat
label_alamat = tk.Label(frame_form, text="Alamat", bg="#D1F1FF")
label_alamat.grid(row=7, column=0, sticky="nw", padx=10, pady=5)
text_alamat = tk.Text(frame_form, width=30, height=5)
text_alamat.grid(row=7, column=1, padx=10, pady=5)

# Frame untuk tombol
frame_button = tk.Frame(window, bg="#D1F1FF")
frame_button.pack(pady=10)

# Tombol Simpan
button_simpan = tk.Button(frame_button, text="Simpan", command=simpan_data, bg="#FF914D", fg="white", width=10)
button_simpan.grid(row=0, column=0, padx=10, pady=10)

# Tombol Hapus
button_hapus = tk.Button(frame_button, text="Hapus", command=hapus_data, bg="#FF914D", fg="white", width=10)
button_hapus.grid(row=0, column=1, padx=10, pady=10)

# Menjalankan aplikasi
window.mainloop()