def main():
    # Buka file bernama 'indata.txt' dalam mode baca
    with open('indata.txt', 'r') as file:
        # Baca semua baris dari file dan konversi setiap baris menjadi integer
        numbers = [int(line.strip()) for line in file]

    # Hitung jumlah dari semua bilangan
    total = sum(numbers)

    # Cetak jumlah dengan pemisah koma dan dua digit di belakang koma
    print("{:.2f}".format(total))

if __name__ == "__main__":
    main()
