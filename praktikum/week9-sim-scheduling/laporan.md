
# Laporan Praktikum Minggu 9
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
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---
## Tugas 
1. Buat progam simulasi FCFS atau SJF.
2. Jalankan progam dengan dataset uji.
3. Sajikan output dalam tabel atau grafik.
4. Tuliskan laporan praktikum pada `laporan.md`.
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
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
