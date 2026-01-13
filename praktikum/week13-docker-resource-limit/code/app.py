import time

data = []
iterasi = 0

print("Program uji resource container dimulai...")
print("Tekan Ctrl+C untuk menghentikan\n")

try:
    while True:
        # Beban CPU (perhitungan berulang)
        total = 0
        for i in range(700_000):
            total += i * i

        # Beban memori (alokasi bertahap)
        data.append("A" * 3_000_000)  # ~3 MB

        iterasi += 1
        print(f"Iterasi {iterasi} | Total hitung: {total} | Estimasi memori: {len(data)*3} MB")

        time.sleep(1)

except MemoryError:
    print("ERROR: Memori tidak cukup, container terkena limit.")
except KeyboardInterrupt:
    print("\nProgram dihentikan manual.")
