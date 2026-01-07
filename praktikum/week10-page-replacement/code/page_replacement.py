pages = [7,0,1,2,0,3,0,4,2,3,0,3,2]
frame_size = 3

def fifo(pages):
    frame, idx, fault = [], 0, 0
    print("\nSIMULASI FIFO (First In First Out)")
    print("| No | Page | Status | Isi Frame |")
    print("-"*47)

    for i,p in enumerate(pages):
        if p in frame:
            status = "HIT"
        else:
            status = "MISS"
            fault += 1
            if len(frame) < frame_size:
                frame.append(p)
            else:
                frame[idx] = p
                idx = (idx+1) % frame_size
        print(f"| {i+1:<2} | {p:<4} | {status:<6} | {frame} |")

    print("-"*47)
    print("Total Page Fault FIFO :", fault)
    return fault


def lru(pages):
    frame, recent, fault = [], [], 0
    print("\nSIMULASI LRU (Least Recently Used)")
    print("| No | Page | Status | Isi Frame |")
    print("-"*47)

    for i,p in enumerate(pages):
        if p in frame:
            status = "HIT"
            recent.remove(p)
        else:
            status = "MISS"
            fault += 1
            if len(frame) < frame_size:
                frame.append(p)
            else:
                old = recent.pop(0)
                frame[frame.index(old)] = p
        recent.append(p)
        print(f"| {i+1:<2} | {p:<4} | {status:<6} | {frame} |")

    print("-"*47)
    print("Total Page Fault LRU :", fault)
    return fault


print("Dataset Loaded :", pages)
print("Jumlah Frame  :", frame_size)

f_fifo = fifo(pages)
f_lru  = lru(pages)

print("\n=== PERBANDINGAN ===")
print("FIFO Page Fault :", f_fifo)
print("LRU Page Fault  :", f_lru)
print("Kesimpulan: Algoritma LRU lebih efisien pada dataset ini.")