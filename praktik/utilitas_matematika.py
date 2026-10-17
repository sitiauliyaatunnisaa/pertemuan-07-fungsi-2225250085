
def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif.")

    total = 0

    for i in range(1, n + 1):
        total += i

    return total


def faktorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif.")

    hasil = 1

    for i in range(2, n + 1):
        hasil *= i

    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("0. Keluar")


def baca_bilangan_bulat(pesan):
    teks = input(pesan).strip()

    try:
        nilai = int(teks)
    except ValueError:
        raise ValueError("Masukkan bilangan bulat yang valid.")

    if nilai < 0:
        raise ValueError("Bilangan tidak boleh negatif.")

    return nilai


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi (0-4): ").strip()

        try:
            if pilihan == "1":
                p = float(input("Masukkan panjang: "))
                l = float(input("Masukkan lebar: "))

                if p < 0 or l < 0:
                    raise ValueError("Ukuran tidak boleh negatif.")

                hasil = luas_persegi_panjang(p, l)
                print(f"Luas persegi panjang = {hasil:g}")

            elif pilihan == "2":
                a = float(input("Masukkan alas: "))
                t = float(input("Masukkan tinggi: "))

                if a < 0 or t < 0:
                    raise ValueError("Ukuran tidak boleh negatif.")

                hasil = luas_segitiga(a, t)
                print(f"Luas segitiga = {hasil:g}")

            elif pilihan == "3":
                n = baca_bilangan_bulat("Masukkan n: ")
                print(f"Jumlah 1 sampai {n} = {jumlah_n(n)}")

            elif pilihan == "4":
                n = baca_bilangan_bulat("Masukkan n: ")
                print(f"{n}! = {faktorial(n)}")

            elif pilihan == "0":
                print("Program selesai.")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih 0 sampai 4.")

        except ValueError as e:
            print("Input tidak valid:", e)


if __name__ == "__main__":
    main()
