# FCFS Scheduling Sederhana

# Data proses: Nama proses, Arrival Time, Burst Time
proses = [
    {"Nama": "P1", "Datang": 0, "Burst": 5},
    {"Nama": "P2", "Datang": 1, "Burst": 7},
    {"Nama": "P3", "Datang": 2, "Burst": 6},
    {"Nama": "P4", "Datang": 3, "Burst": 4},
]

waktu_sekarang = 0
total_waiting = 0
total_turnaround = 0

# Hitung Waiting Time dan Turnaround Time
for p in proses:
    if waktu_sekarang < p["Datang"]:
        waktu_sekarang = p["Datang"]
    p["Waiting"] = waktu_sekarang - p["Datang"]
    p["Turnaround"] = p["Waiting"] + p["Burst"]
    waktu_sekarang += p["Burst"]
    total_waiting += p["Waiting"]
    total_turnaround += p["Turnaround"]

# Tampilkan tabel hasil
print("-"*50)
print("Process    Arrival  Burst    Waiting    Turnaround")
print("-"*50)
for p in proses:
    print(f"{p['Nama']:<10} {p['Datang']:<7} {p['Burst']:<8} {p['Waiting']:<9} {p['Turnaround']}")
print("-"*50)

n = len(proses)
print(f"Rata-rata Waiting Time    : {total_waiting/n}")
print(f"Rata-rata Turnaround Time : {total_turnaround/n}")
