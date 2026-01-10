
# Laporan Praktikum Minggu 12
Topik: Virtualisasi Menggunakan Virtual Machine
---

## Identitas
- **Nama**  : Putri Amaliya Rahmadani  
- **NIM**   : 250202924
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
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

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
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
