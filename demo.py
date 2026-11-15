"""Demo non-interaktif: menghasilkan output untuk laporan & video."""
from data_contoh import struktur_baru, struktur_uin
from org_tree import tampilkan

t = struktur_uin()
print("== STRUKTUR ORGANISASI ==")
t.cetak_pohon()
print(f"\nNode={t.jumlah_node()}  Tinggi={t.tinggi()} level")

print("\n== INSERT ==")
n = t.insert_node("Ketua Program Studi Sistem Informasi", "DS4", "Lutfi Hakim, M.Kom.", "Dosen Sistem Informasi")
print("Ditambahkan:", n, "-> atasan:", n.atasan)
try:
    t.insert_node("XYZ", "ZZ", "A", "B")
except ValueError as e:
    print("Error ditangani:", e)

print("\n== SEARCH ==")
for k in ["Dosen", "dewi", "Dekan"]:
    print(f"'{k}':", t.search_node(k))
print("Rantai komando DS4:", " <- ".join(x.jabatan for x in t.jalur_ke_root(n)))

tampilkan("PREORDER", t.preorder())
tampilkan("INORDER", t.inorder())
tampilkan("POSTORDER", t.postorder())

b = struktur_baru()
print("\n\n== STRUKTUR BARU (soal No. 11) ==")
b.cetak_pohon()
print(f"Node={b.jumlah_node()}  Tinggi={b.tinggi()} level")
for judul, urutan in [("Pre-order", b.preorder()), ("In-order", b.inorder()), ("Post-order", b.postorder())]:
    print(f"\n{judul}:\n  " + " → ".join(x.jabatan for x in urutan))
