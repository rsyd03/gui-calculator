import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#init
window = tk.Tk()
window.configure(bg="black")
window.geometry("360x640")

#variable
ANGKA_PERTAMA = tk.IntVar()
ANGKA_KEDUA = tk.IntVar()

#fungsi clc
def tombol_click_tambah():
    '''Fungsi ini akan dipanggil oleh tombol tambah'''
    angka_pertama = ANGKA_PERTAMA.get()
    angka_kedua = ANGKA_KEDUA.get()
    angka_ketiga = angka_pertama + angka_kedua

    pesan = f"Hasil penjumlahan {angka_pertama} dan {angka_kedua} adalah = {angka_ketiga}"
    showinfo(title="tambah", message=pesan)

def tombol_click_kurang():
    '''Fungsi ini akan dipanggil oleh tombol tambah'''
    angka_pertama = ANGKA_PERTAMA.get()
    angka_kedua = ANGKA_KEDUA.get()
    angka_ketiga = angka_pertama - angka_kedua

    pesan = f"Hasil pengurangan {angka_pertama} dan {angka_kedua} adalah = {angka_ketiga}"
    showinfo(title="tambah", message=pesan)

def tombol_click_kali():
    '''Fungsi ini akan dipanggil oleh tombol tambah'''
    angka_pertama = ANGKA_PERTAMA.get()
    angka_kedua = ANGKA_KEDUA.get()
    angka_ketiga = angka_pertama * angka_kedua

    pesan = f"Hasil pengalian {angka_pertama} dan {angka_kedua} adalah = {angka_ketiga}"
    showinfo(title="tambah", message=pesan)

def tombol_click_bagi():
    '''Fungsi ini akan dipanggil oleh tombol tambah'''
    angka_pertama = ANGKA_PERTAMA.get()
    angka_kedua = ANGKA_KEDUA.get()
    angka_ketiga = angka_pertama / angka_kedua

    pesan = f"Hasil pembagian {angka_pertama} dan {angka_kedua} adalah = {angka_ketiga}"
    showinfo(title="tambah", message=pesan)


#input garis / frame 
input_frame = ttk.Frame(window)
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen - komponen
# 1. Label pertama
angka_pertama = ttk.Label(input_frame,text="Angka pertama :")
angka_pertama.pack(padx = 10, fill="y", expand=True)

# Entry angka pertama
angka_pertama_entry = ttk.Entry(input_frame,textvariable=ANGKA_PERTAMA)
angka_pertama_entry.pack(padx=10,fill="x",expand=True)

# 2. Label kedua
angka_pertama = ttk.Label(input_frame,text="Angka kedua :")
angka_pertama.pack(padx = 10, fill="y", expand=True)

# Entry angka kedua
angka_kedua_entry = ttk.Entry(input_frame,textvariable=ANGKA_KEDUA)
angka_kedua_entry.pack(padx=10,fill="x",expand=True)

# 5. Tombol tambah
tombol_tambah = ttk.Button(input_frame,text="+",command = tombol_click_tambah)
tombol_tambah.pack(padx=10,pady=10,fill='x',expand=True)

# 6. Tombol kurang
tombol_kurang = ttk.Button(input_frame, text = "-",command = tombol_click_kurang)
tombol_kurang.pack(padx=10,pady=10,fill='x',expand=True)

# 7. Tombol kali
tombol_kali = ttk.Button(input_frame,text="x",command = tombol_click_kali)
tombol_kali.pack(padx=10,pady=10,fill='x',expand=True)

# 8. Tombol bagi
tombol_bagi = ttk.Button(input_frame,text="/",command = tombol_click_bagi)
tombol_bagi.pack(padx=10,pady=10,fill='x',expand=True)

#looping window
window.mainloop()