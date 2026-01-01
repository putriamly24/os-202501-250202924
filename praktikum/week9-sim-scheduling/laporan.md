
# Laporan Praktikum Minggu [ 9 ]
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : Putri Amaliya Rahmadani  
- **NIM**   :  250202924
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.
4. Menjelaskan hasil simulasi secara tertulis.
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
1. Penjadwalan CPU merupakan mekanisme yang dijalankan oleh sistem operasi untuk menentukan proses mana dari *ready queue* yang memperoleh alokasi waktu pemrosesan pada CPU, dengan tujuan menjaga CPU tetap aktif dan mendukung lingkungan sistem yang bersifat multiprogamming.
2. Penjadwalan CPU berfungsi untuk mengatur pemanfaatan sumber daya prosesor secara efisien, dengan sasaran uatama memaksimalkan penggunaan CPU, meningkatkan jumlah proses yang dapat diselesaikan dalam satuan waktu tertentu, serta meminimalkan waktu tunggu dan waktu penyelesaian proses.
3. Algoritma penjadwalan CPU diklasifikasikan ke dalam dua kategori, yaitu non-preemptive, di mana proses dieksekusi hingga selesai atau menunggu I/O, dan preemptive, di mana sistem operasi dapat menghentikan sementara proses yang sedang berjalan untuk memberikan kesempatan eksekusi kepada proses lain.
4. Dalam sistem operasi, proses umumnya mengalami siklus bergantian antara eksekusi CPU (CPU burst) dan operasi masukan/keluaran (I/O burst), sehingga penjadwalan CPU berperan penting dalam menentukan proses berikutnya yang dieksekusi ketika proses aktif memasuki keadaan menunggu atau telah selesai.
5. Kinerja algoritma penjadwalan CPU dievaluasi menggunakan beberapa parameter, antara lain tingkat pemanfaatan CPU, throughput, turnaround time, waiting time, dan response time, yang digunakan untuk menilai efektivitas serta efisiensi suatu algoritma penjadwalan.  
---

## Langkah Praktikum
1. Sesuaikan struktur folder dengan template repo:
```
praktikum/week9-sim-scheduling/
├─ code/
│  ├─ scheduling_simulation.py
│  └─ dataset.csv
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
```
2. Siapkan dataset seperti berikut:
| Proses |	Arrival Time |	Burst Time |
| P1 | 0 | 6 |
| P2 | 1 | 8 |
| P3 | 2 | 7 |	
| P4 | 3 | 3 |
3. Implementasikan Algoritma

Program harus:
- Menghitung waiting time dan turnaround time.
- Mendukung minimal 1 algoritma (FCFS atau SJF non-preemptive).
- Menampilkan hasil dalam tabel.

4. Eksekusi & Validasi
- Jalankan program menggunakan dataset uji.
- Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.
- Simpan hasil eksekusi (screenshot).
  
5. Analisis
- Jelaskan alur program.
- Bandingkan hasil simulasi dengan perhitungan manual.
- Jelaskan kelebihan dan keterbatasan simulasi.

6. Commit & Push

```bash
git add .
git commit -m "Minggu 9 - Simulasi Scheduling CPU"
git push origin main
```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```
proses  = ["P1", "P2", "P3", "P4"]
arrival = [0, 1, 2, 3]
burst   = [6, 8, 7, 3]

time = 0
wt = []
tat = []

# Hitung FCFS
for i in range(len(proses)):
    if time < arrival[i]:
        time = arrival[i]

    wt.append(time - arrival[i])
    tat.append(wt[i] + burst[i])
    time += burst[i]

# Tampilkan tabel
print("Proses | Arrival | Burst | Waiting | Turnaround")
print("-" * 45)

for i in range(len(proses)):
    print(f"{proses[i]:>5} | {arrival[i]:>7} | {burst[i]:>5} | {wt[i]:>7} | {tat[i]:>10}")
```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/dataset.py)

---

## Analisis
- Alur Progam
  Progam diawali dengan pendefinisian data proses yang meliputi identitas proses, waktu kedatangan (*arrival time*), dan waktu eksekusi (*burst time*).Selanjutnya, program menginisialisasi variabel waktu CPU (`time`) yang berfungsi sebagai penanda waktu berjalan, serta dua buah list untuk menyimpan nilai waiting time dan turnaround time. Proses penjadwalan dilakukan menggunakan algoritma First Come First Served (FCFS), di mana proses dieksekusi berdasarkan urutan kedatangan. Pada setiap iterasi, program terlebih dahulu memastikan apakah CPU harus menunggu hingga proses tiba. Setelah itu, waiting time dihitung dari selisih antara waktu CPU saat proses akan dieksekusi dengan waktu kedatangannya. Nilai turnaround time diperoleh dari penjumlahan waiting time dan burst time. Setelah proses selesai dieksekusi, waktu CPU diperbarui dengan menambahkan burst time proses tersebut.Setelah seluruh proses dieksekusi, program menampilkan hasil perhitungan dalam bentuk tabel yang berisi informasi proses, *arrival time*, *burst time*, *waiting time*, dan *turnaround time*.
>- Tabel Hasil Perhitungan FCFS
  
| Proses | Arrival Time | Burst Time | Waiting Time | Turnaround Time |
| ------ | ------------ | ---------- | ------------ | --------------- |
| P1     | 0            | 6          | 0            | 6               |
| P2     | 1            | 8          | 5            | 13              |
| P3     | 2            | 7          | 12           | 19              |
| P4     | 3            | 3          | 18           | 21              |

- Perbandingan Hasil Simulasi dengan Perhitungan Manual: 
Berdasarkan hasil simulasi yang diperoleh, nilai waiting time dan turnaround time untuk setiap proses menunjukkan kesesuaian dengan hasil perhitungan manual yang telah dilakukan sebelumnya. Urutan eksekusi proses juga tidak mengalami perbedaan karena algoritma FCFS mengeksekusi proses sesuai urutan waktu kedatangan. Dengan demikian, dapat disimpulkan bahwa simulasi yang dibuat telah berjalan dengan benar dan hasilnya valid.
- Kelebihan : 
Simulasi ini mempermudah proses perhitungan waiting time dan turnaround time secara sistematis dan konsisten. Selain itu, penggunaan program dapat mengurangi kesalahan yang mungkin terjadi pada perhitungan manual. Penyajian hasil dalam bentuk tabel juga memudahkan proses analisis dan evaluasi hasil penjadwalan.
- Kekurangan :
  Simulasi ini masih terbatas pada penggunaan satu algoritma penjadwalan, yaitu FCFS. Program belum mempertimbangkan adanya context switching maupun penjadwalan bersifat preemptive. Selain itu, simulasi belum dilengkapi dengan visualisasi seperti Gantt Chart yang dapat memberikan gambaran waktu eksekusi proses secara lebih jelas.
  

---

## Kesimpulan
- Algoritma First Come First Served (FCFS) mengeksekusi proses berdasarkan urutan kedatangan sehingga mudah dipahami dan diimplementasikan, namun dapat menyebabkan waktu tunggu yang cukup lama bagi proses yang datang belakangan.
- Hasil simulasi penjadwalan CPU menggunakan program menunjukkan nilai waiting time dan turnaround time yang sesuai dengan perhitungan manual, sehingga simulasi dapat dinyatakan berjalan dengan benar dan valid.
- Melalui praktikum ini, penggunaan simulasi membantu mahasiswa memahami konsep penjadwalan CPU secara lebih sistematis serta mempermudah analisis dibandingkan perhitungan manual.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?
   Jawaban : Simulasi diperlukan untuk menguji algoritma scheduling karena sistem nyata bersifat kompleks, banyak proses bersaing, dan simmulasi mampu menunjukkan performa seperti waktu tunggu, waktu selesai, serta respons secara lebih realistis.
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
   Jawaban : Perhitungan manual cocok untuk sedikit proses namun lambat dan rawan salah, sedangkan simulasi lebih cepat, akurat, dapat menangani ribuan proses, serta mudah diulang dengan berbagai skenario.
3. Algoritma mana yang lebih mudah diimplementassikan? Jelaskan.
   Jawaban : Karena hanya mengikuti urutan kedatangan proses, sementara algoritma lain seperti Round Robin atau Priority Scheduling membutuhkan aturan tambahan yang lebih rumit. 
   

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? memahami alur perhitungan waiting time dan turnaround time dalam algoritma penjadwalan CPU.
- Bagaimana cara Anda mengatasinya?memahami konsep dasarnya dan berdiskusi dengan teman.  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
