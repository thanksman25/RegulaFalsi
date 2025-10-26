# ============================================================
# feat(core): menambahkan fungsi utama metode Regula Falsi
# ------------------------------------------------------------
# Logika utama untuk menghitung akar persamaan non-linear
# menggunakan metode Regula Falsi secara iteratif.
# ============================================================

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
