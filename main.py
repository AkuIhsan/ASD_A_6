#############################################################################
# TOPIK : TUMPUKAN DOKUMEN
# NO KELOMPOK : 
# ANGGOTA : 
# - IHSAN HAMIZAN (J0403251051)
# - MUHAMMAD RAIHAN RAMADHAN (J0403251038)
# - HANIF MISBAH (J0403251)
#
#############################################################################

from os import system, name, remove
from datetime import datetime
from Stack import Stack
from Queuee import Queue
from rich.console import Console
from rich import inspect
from rich.table import Table
from rich import print
from pathlib import Path
from rich.rule import Rule
import json

# Inisiasi objek console dari library rich agar menampilkan teks dengan style yang indah.
console = Console()

# Inisiasi variabel lanjut untuk mengetahui status pengguna, apakah masih ingin lanjut menggunakan program atau tidak.
lanjut = True

# Inisiasi variabel untuk lokasi dari antrian.json dan tumpukan.json
PathAntrian = "./Data/antrian.json"
PathTumpukan = "./Data/tumpukan.json"

# Inisiasi variabel untuk mengetahui apakah antrian.json dan tumpukan.json exist (ada)
PathAntrianExist = Path(PathAntrian)
PathTumpukanExist = Path(PathTumpukan)

# Inisiasi variabel untuk membuat objek dari class Stack dan Queue
tumpukan = Stack()
antrian = Queue()



def Tampilan_Menu() :
    """ Fungsi untuk menampilkan menu pada tampilan awal program """

    console.print("Halo Selamat Datang di [bold red]TuDo[/bold red] 📃", style="dim ")
    print("ToDo adalah aplikasi berbasi CLI (Command Line Interface) yang bertujuan membantu pengguna khususnya di bidang manajemen dalam mengatur tumpukan dokumen")
    console.print("1. Membuat tumpukan")
    console.print("2. Melihat isi tumpukan")
    console.print("3. Menghapus tumpukan")
    console.print("4. Mengedit ukuran tumpukan")
    console.print("5. Ambil dokumen dari Tumpukan")
    console.print("6. Buat dan taruh dokumen baru ke tumpukan")
    console.print("7. Mencari dokumen di tumpukan")
    console.print("9. Keluar")

def Cek_Keberadaan_File(path) :
    """ fungsi untuk mengecek eksistensi suatu file apakah dia exist atau tidak? """

    if path.exists() : return True
    return False

def baca_data_tumpukan() :
    """ Fungsi Untuk Membaca data dari JSON untuk data tumpukan"""
    if not Cek_Keberadaan_File(PathTumpukanExist) :
        return
    with open(PathTumpukan, 'r') as file:
        tumpukan.reset()
        data = json.load(file)
        for i in range(len(data)) :
            if i == 0 :
                tumpukan.SetSize(data[i]['ukuran'])
                continue

            tumpukan.push(data[i])


def simpan_perubahan_tumpukan() :
    tumpukan_list = list(tumpukan.data)
    tumpukanGabungan = [{'ukuran' : tumpukan.size} ] + tumpukan_list
    json_str = json.dumps(tumpukanGabungan, indent=4)
    with open(PathTumpukan, "w") as f:
        f.write(json_str)


###################################################################################################
#                                   Operasi untuk tumpukan                                        #
###################################################################################################
def buat_tumpukan() :
    """ Fungsi untuk membuat tumpukan pada program """
    if Cek_Keberadaan_File(PathTumpukanExist) : 
        return "Tumpukan Sudah Ada "

    ukuran = str(console.input("Masukkan ukuran tumpukan :  "))
    if not ukuran.isnumeric() :
        return "Anda memasukkan input selain angka"

    tumpukan.SetSize(int(ukuran))

    with open(PathTumpukan, "w") as f:
        json.dump([{"ukuran" : tumpukan.size}], f)

    return "Tumpukan Berhasil Dibuat!"


def lihat_tumpukan() :
    """ Fungsi untuk melihat isi tumpukan """
    
    if not Cek_Keberadaan_File(PathTumpukanExist) :
        return "Tumpukan Belum Ada"
    
    # Inisiasi objek tabel dari library rich untuk membuat tampilan tabel
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("No")
    table.add_column("Waktu Masuk", style="dim", width=12)
    table.add_column("Judul")
    table.add_column("Author")

    # Inisiasi variabel untuk nomor
    nomor = 1


    
    for data in tumpukan.data :
        table.add_row(str(nomor), data['waktu'], data['judul'], data['author'])
        nomor += 1

    console.print(f"Ukuran Tumpukan : {tumpukan.size}")
    console.print(table)


def hapus_tumpukan() :
    remove(PathTumpukan)
    return "Tumpukan Berhasil Dihapus"


def edit_tumpukan() :
    ukuran = str(console.input("Masukkan ukuran : "))
    
    if ukuran.isnumeric() :
        konfirmasi = console.input("Apakah anda ingin melakukan perubahan ? (ya/tidak) ")
        if konfirmasi == "ya" :
            tumpukan.SetSize(int(ukuran))
            console.print(Rule(f"[bold red]Perubahan berhasil dibuat[bold red]"))
                
        elif konfirmasi == "tidak" :
            console.print(Rule(f"[bold red]Anda membatalkan perubahan [bold red]"))

        else :
            console.print(Rule(f"[bold red]Anda tidak memilih dengan pilihan yang ada[bold red]"))

    else :
        console.print(Rule(f"[bold red]Anda tidak memasukkan angka[bold red]"))



###################################################################################################
#                                   Operasi untuk dokumen                                         #
###################################################################################################

def ambil_dokumen() :
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Waktu Masuk", style="dim", width=12)
    table.add_column("Judul")
    table.add_column("Author")

    dokumen = tumpukan.pop()
    if not dokumen :
        return
    table.add_row(dokumen['waktu'],dokumen['judul'],dokumen['author'])
    console.print(table)


def cari_dokumen() :
    if not Cek_Keberadaan_File(PathTumpukanExist) :
        console.print(Rule("[bold red]Tumpukan belum ada[/bold red]"))
        return

    if len(tumpukan.data) == 0 :
        console.print(Rule("[bold red]Tumpukan masih kosong[/bold red]"))
        return

    console.print(Rule("[bold cyan]Cari Dokumen[/bold cyan]"))
    console.print("[bold]Cari berdasarkan :[/bold]")
    console.print("  [cyan]1.[/cyan] Judul")
    console.print("  [cyan]2.[/cyan] Penulis / Author")
    console.print("  [cyan]3.[/cyan] Index / Urutan")
    console.print("  [cyan]4.[/cyan] Waktu Input")

    param = console.input("\nPilih parameter pencarian (1-4) : ").strip()

    if param not in ["1", "2", "3", "4"] :
        console.print(Rule("[bold red]Pilihan tidak valid[/bold red]"))
        return

    if param == "4" :
        keyword = console.input("Masukkan keyword pencarian (YYYY-MM-DD) : ").strip().lower()
    else:
        keyword = console.input("Masukkan keyword pencarian : ").strip().lower()

    if not keyword :
        console.print(Rule("[bold red]Keyword tidak boleh kosong[/bold red]"))
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("No",       style="bold",    width=4)
    table.add_column("Judul",    style="cyan")
    table.add_column("Author",   style="green")
    table.add_column("Index / Urutan", style="yellow", width=14)
    table.add_column("Waktu Input", style="dim")

    hasil_ditemukan = 0
    nomor_tampil = 1

    for index, dokumen in enumerate(tumpukan.data) :
        judul  = dokumen.get('judul',  '')
        author = dokumen.get('author', '')
        waktu  = dokumen.get('waktu',  '')
        urutan = str(index + 1)

        cocok = False

        if param == "1" :
            cocok = keyword in judul.lower()

        elif param == "2" :
            cocok = keyword in author.lower()

        elif param == "3" :
            cocok = keyword == urutan

        elif param == "4" :
            cocok = keyword in waktu.lower()

        if cocok :
            table.add_row(
                str(nomor_tampil),
                judul,
                author,
                urutan,
                waktu
            )
            hasil_ditemukan += 1
            nomor_tampil += 1

    console.print(Rule("[bold cyan]Hasil Pencarian[/bold cyan]"))
    if hasil_ditemukan == 0 :
        if param == "1" :
            console.print(Rule(f"[bold red] Dokumen dengan Judul '{keyword}' Tidak Ada [/bold red]"))
        elif param == "2" :
            console.print(Rule(f"[bold red] Dokumen dengan Penulis '{keyword}' Tidak Ada [/bold red]"))
        elif param == "3" :
            console.print(Rule(f"[bold red] Dokumen dengan Index '{keyword}' Tidak Ada [/bold red]"))
        elif param == "4" :
            console.print(Rule(f"[bold red]Tidak ada Dokumen yang diinput pada'{keyword}'[/bold red]"))
    else :
        console.print(f"Ditemukan [bold green]{hasil_ditemukan}[/bold green] dokumen dengan keyword '[bold]{keyword}[/bold]'")
        console.print(table)

def buat_taruh_dokumen() :
    if Cek_Keberadaan_File(PathAntrianExist) :
        return
     
    author = str(console.input("Masukkan nama author : "))
    judul = str(console.input("Masukkan judul dokumen : "))
    waktu = str(datetime.now())

    data = {
        'author' : author,
        'judul' : judul,
        'waktu' : waktu
    } 

    if not tumpukan.push(data) :
        console.print(Rule(f"[bold red] Data gagal dimasukkan karena sudah melebihi ukuran tumpukan[bold red]"))
    else :
        console.print(Rule(f"[bold red] Data berhasil dimasukkan [bold red]"))

###################################################################################################
#                                   Operasi untuk Antrian                                         #
###################################################################################################

def buat_antrian() :
    pass

def lihat_antrian() :
    pass

def urutkan_antrian() :
    pass

def hapus_antrian() :
    pass



###################################################################################################
#                                   Fungsi Utama Program                                          #
###################################################################################################
def main() :
    global lanjut

    while lanjut :
        baca_data_tumpukan()
        Tampilan_Menu()
        pilihan = input("Pilih Menu : ")
        if pilihan == "1" :
            system("cls" if name == "nt" else "clear")
            console.print(Rule(f"[bold cyan]{buat_tumpukan()}[/bold cyan]"))

        elif pilihan == "2" :
            system("cls" if name == "nt" else "clear")
            lihat_tumpukan()

        elif pilihan == "3" :
            system("cls" if name == "nt" else "clear")
            if Cek_Keberadaan_File(PathTumpukanExist) :
                konfirmasi = console.input("[bold red]Konfirmasi Penghapusan[/bold red] (ya/tidak)")

                if konfirmasi.lower() == "ya" :
                    console.print(Rule(f"[bold red]{hapus_tumpukan()}[/bold red]"))

                elif konfirmasi.lower() == "tidak" :
                    console.print(Rule(f"[bold red]Tumpukan gagal dihapus karena tidak disetujui[bold red]"))


                else :
                    console.print(Rule(f"[bold red]Anda tidak memilih dengan pilihan yang ada[bold red]"))
            else :
                console.print(Rule(f"[bold red]Tidak ada tumpukan[bold red]"))
        
        elif pilihan == "4" :
            system("cls" if name == "nt" else "clear")
            edit_tumpukan()
            simpan_perubahan_tumpukan()

        elif pilihan == "5" :
            system("cls" if name == "nt" else "clear")
            ambil_dokumen()
            simpan_perubahan_tumpukan()

        elif pilihan == "6" :
            system("cls" if name == "nt" else "clear")
            buat_taruh_dokumen()
            simpan_perubahan_tumpukan()

        elif pilihan == "7" :
            system("cls" if name == "nt" else "clear")
            cari_dokumen()

        elif pilihan == "9" :
            system("cls" if name == "nt" else "clear")
            console.print("Terima kasih sudah menggunakan TuDo 😊", style="bold cyan")
            lanjut = False

        else :
            system("cls" if name == "nt" else "clear")
            console.print(Rule(f"[bold red]Anda tidak memilih dengan pilihan yang ada[bold red]"))
            continue
            


main()




