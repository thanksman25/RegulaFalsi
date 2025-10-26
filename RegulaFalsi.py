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

