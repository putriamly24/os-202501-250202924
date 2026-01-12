
# Laporan Praktikum Minggu 12
Topik: Virtualisasi Menggunakan Virtual Machine
---

## Identitas
- **Nama**  : 
  1. Sukmani Intan Jumala (250202983)
  2. Novia Safitri (250202923)
  3. Putri Amaliya Rahmadani (250202924)
- **Kelas** : 1 IKRA
---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).
2. Membuat dan menjalankan sistem operasi guest di dalam VM.
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
- Virtualisasi adalah teknologi yang memungkinkan satu komputer fisik menjalankan beberapa sistem operasi secara bersamaan dengan memanfaatkan pembagian sumber daya perangkat keras.
- Host OS dan Guest OS adalah dua jenis sistem operasi dalam virtualisasi, di mana host OS berfungsi mengelola perangkat keras secara langsung, sedangkan guest OS berjalan di dalam mesin virtual dan menggunakan resource dari host OS.
- Hypervisor merupakan perangkat lunak yang berperan mengatur dan mengelola mesin virtual serta membagi sumber daya seperti CPU dan RAM agar setiap sistem dapat berjalan dengan aman dan stabil.
- Isolasi Sistem adalah konsep dalam virtualisasi yang membuat setiap mesin virtual berjalan secara terpisah, sehingga gangguan atau masalah pada satu sistem tidak langsung memengaruhi sistem lainnya maupun sistem utama.

---

## Langkah Praktikum
1. **Struktur folder (sesuaikan dengan template repo):**
```
praktikum/week12-virtual-machine/
├─ code/
│  └─ catatan_konfigurasi.txt (opsional)
├─ screenshots/
│  ├─ instalasi_vm.png
│  ├─ konfigurasi_resource.png
│  └─ os_guest_running.png
└─ laporan.md
```
2. **Instalasi Virtual Machine**

- Instal VirtualBox atau VMware pada komputer host.
- Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

3. **Instalasi Sistem Operasi**

- Jalankan proses instalasi OS guest sampai selesai.
- Pastikan OS guest dapat login dan berjalan normal.

4. **Konfigurasi Resource**

- Ubah konfigurasi CPU dan RAM.
- Amati perbedaan performa sebelum dan sesudah perubahan resource.

5. **Analisis Proteksi OS**

- Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.
- Kaitkan dengan konsep sandboxing dan hardening OS.

6. **Dokumentasi**

- Ambil screenshot setiap tahap penting.
- Simpan di folder `screenshots/`.

7. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
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

## Quiz
1. Apa perbedaan antara host OS dan guest OS?
   **Jawaban:**

   Host OS adalah sistem operasi utama yang terpasang langsung pada komputer dan memiliki kontrol penuh terhadap perangkat      keras. Sedangkan guest OS adalah sistem operasi yang dijalankan di dalam mesin virtual menggunakan software virtualisasi     dan hanya menggunakan resource yang dialokasikan oleh host OS. Perbedaan utamanya, host OS mengelola hardware secara         langsung, sementara guest OS berjalan secara terisolasi di atas host OS tanpa mengganggu sistem utama.  

3. Apa peran hypervisor dalam virtualisasi?

   **Jawaban:**

   Hypervisor berperan sebagai pengelola utama dalam teknologi virtualisasi yang bertugas membuat, menjalankan, dan mengatur    mesin virtual (Virtual Machine). Hypervisor membagi serta mengalokasikan sumber daya perangkat keras seperti CPU, RAM,       dan storage kepada setiap VM agar dapat berjalan secara bersamaan tanpa saling mengganggu, sehingga sistem host tetap        stabil dan aman.

5. Mengapa virtualisasi meningkatkan keamanan sistem?

   **Jawaban:**

    Virtualisasi dapat meningkatkan keamanan sistem karena setiap sistem operasi dijalankan dalam lingkungan yang terpisah.      terjadi error, crash, atau serangan malware pada sistem operasi guest, dampaknya tidak langsung memengaruhi sistem utama     (host). Dengan adanya isolasi ini, pengguna dapat melakukan pengujian atau menjalankan aplikasi berisiko dengan lebih        aman  tanpa mengganggu kestabilan dan keamanan sistem secara keseluruhan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
