import tkinter as tk
from tkinter import ttk, messagebox
import math

def regula_falsi(f_str, a, b, tol, max_iter):
    # Fungsi lokal untuk mengevaluasi ekspresi matematika dari input pengguna
    def f(x):
        return eval(f_str)

    data = []
    fa = f(a)
    fb = f(b)

    # Validasi agar f(a) dan f(b) memiliki tanda berbeda
    if fa * fb > 0:
        messagebox.showerror("Error", "f(a) dan f(b) memiliki tanda yang sama! Tidak ada akar di antara a dan b.")
        return []

    # Iterasi Regula Falsi
    for i in range(1, max_iter + 1):
        xr = (b * fa - a * fb) / (fa - fb)  # rumus utama Regula Falsi
        fxr = f(xr)
        product_fb = fxr * fb
        abs_fxr = abs(fxr)

        # Simpan data tiap iterasi ke dalam list
        data.append((i, a, b, fa, fb, xr, fxr, product_fb, abs_fxr))

        # Hentikan jika sudah memenuhi toleransi
        if abs_fxr < tol:
            break

        # Update batas interval
        if fxr * fb < 0:
            b = xr
            fb = fxr
        else:
            a = xr
            fa = fxr

    return data

def hitung():
    try:
        f_str = entry_f.get()
        a = float(entry_a.get())
        b = float(entry_b.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_iter.get())

        # Hapus tabel sebelumnya
        for item in tree.get_children():
            tree.delete(item)

        # Jalankan metode Regula Falsi
        hasil = regula_falsi(f_str, a, b, tol, max_iter)

        # Masukkan hasil ke tabel
        for i, row in enumerate(hasil):
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            tree.insert("", "end", values=[f"{v:.9f}" if isinstance(v, float) else v for v in row], tags=(tag,))

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def hapus_tabel():
    # Hapus semua baris pada tabel hasil
    for item in tree.get_children():
        tree.delete(item)

    # Kosongkan semua input field
    entry_f.delete(0, tk.END)
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_tol.delete(0, tk.END)
    entry_iter.delete(0, tk.END)

    # Tampilkan notifikasi sederhana
    messagebox.showinfo("Hapus Data", "Tabel dan input berhasil dikosongkan.")

root = tk.Tk()
root.title("🧮 Kalkulator Metode Regula Falsi")
root.geometry("1200x700")
root.config(bg="#E9EEF5")

# Judul utama aplikasi
judul = tk.Label(
    root,
    text="Kalkulator Metode Regula Falsi",
    font=("Segoe UI", 18, "bold"),
    bg="#3E5879",
    fg="white",
    pady=10
)
judul.pack(fill="x")

frame_input = tk.LabelFrame(
    root,
    text="Input Parameter",
    font=("Segoe UI", 11, "bold"),
    bg="#F8FAFD",
    fg="#3E5879",
    padx=15,
    pady=10,
    labelanchor="n"
)
frame_input.pack(pady=15, padx=20, fill="x")

# Field input
tk.Label(frame_input, text="Masukkan f(x):", bg="#F8FAFD", fg="#2E4057", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
entry_f = tk.Entry(frame_input, width=40, font=("Consolas", 10))
entry_f.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_input, text="Nilai tebakan a:", bg="#F8FAFD", fg="#2E4057", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=5)
entry_a = tk.Entry(frame_input, width=15, font=("Consolas", 10))
entry_a.grid(row=1, column=1, sticky="w", padx=10)

tk.Label(frame_input, text="Nilai tebakan b:", bg="#F8FAFD", fg="#2E4057", font=("Segoe UI", 10)).grid(row=2, column=0, sticky="w", pady=5)
entry_b = tk.Entry(frame_input, width=15, font=("Consolas", 10))
entry_b.grid(row=2, column=1, sticky="w", padx=10)

tk.Label(frame_input, text="Toleransi error:", bg="#F8FAFD", fg="#2E4057", font=("Segoe UI", 10)).grid(row=3, column=0, sticky="w", pady=5)
entry_tol = tk.Entry(frame_input, width=15, font=("Consolas", 10))
entry_tol.grid(row=3, column=1, sticky="w", padx=10)

tk.Label(frame_input, text="Jumlah iterasi:", bg="#F8FAFD", fg="#2E4057", font=("Segoe UI", 10)).grid(row=4, column=0, sticky="w", pady=5)
entry_iter = tk.Entry(frame_input, width=15, font=("Consolas", 10))
entry_iter.grid(row=4, column=1, sticky="w", padx=10)

# Tombol aksi
frame_btn = tk.Frame(root, bg="#E9EEF5")
frame_btn.pack(pady=10)
btn_hitung = tk.Button(frame_btn, text="▶ Hitung", command=hitung, bg="#4ABCE2", fg="white",
font=("Segoe UI", 10, "bold"), relief="flat", width=15)
btn_hitung.pack(side="left", padx=10)

btn_hapus = tk.Button(frame_btn, text="🗑 Hapus Tabel", command=hapus_tabel, bg="#E74C3C", fg="white",
font=("Segoe UI", 10, "bold"), relief="flat", width=15)
btn_hapus.pack(side="left", padx=10)

frame_tabel = tk.LabelFrame(root, text="Hasil Iterasi", font=("Segoe UI", 11, "bold"),
bg="#F8FAFD", fg="#3E5879", padx=10, pady=10, labelanchor="n")
frame_tabel.pack(padx=20, pady=10, fill="both", expand=True)

columns = ("Iterasi", "a", "b", "f(a)", "f(b)", "xr", "f(xr)", "f(xr)*f(b)", "|f(xr)|")
tree = ttk.Treeview(frame_tabel, columns=columns, show="headings", height=15)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")

# Pewarnaan baris tabel
tree.tag_configure('evenrow', background="#F1F6FC")
tree.tag_configure('oddrow', background="#FFFFFF")

# Scrollbar vertikal
scrollbar = ttk.Scrollbar(frame_tabel, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# Jalankan GUI
root.mainloop()


