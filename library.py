import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--nama", required=True, help="Masukkan nama anda")
parser.add_argument(
    "-t",
    "--tanggallahir",
    required=True,
    help="Masukkan tanggal lahir anda (DD-MM-YYYY)",
)
args = parser.parse_args()

from datetime import date

today = date.today()
lahir = date(
    *[int(x) for x in args.tanggallahir.split("-")[::-1]]
)  # set date format to DD-MM-YYYY
usia = today.year - lahir.year - ((today.month, today.day) < (lahir.month, lahir.day))

if usia < 30:
    print(
        f"Terima kasih telah menggunakan program ini pada tahun {today.year}, Kak {args.nama}!"
    )
else:
    print(
        f"Terima kasih telah menggunakan program ini pada tahun {today.year}, Bapak {args.nama}!"
    )
