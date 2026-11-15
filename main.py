"""Demo CLI Silsilah Organisasi UIN Suska Riau."""
from data_contoh import struktur_uin
from org_tree import tampilkan


def main() -> None:
    t = struktur_uin()
    while True:
        print("\n=== SILSILAH ORGANISASI ===")
        print("1. Tampilkan struktur (pohon)")
        print("2. Tambah pegawai (insert_node)")
        print("3. Cari pegawai (search_node)")
        print("4. Traversal preorder / inorder / postorder")
        print("5. Info bentuk pohon")
        print("0. Keluar")
        p = input("Pilih: ").strip()
        if p == "1":
            t.cetak_pohon()
        elif p == "2":
            try:
                n = t.insert_node(input("Atasan (ID/nama/jabatan): "), input("ID baru: "),
                                  input("Nama: "), input("Jabatan: "))
                print(f"  ✔ {n} ditambahkan di bawah {n.atasan}")
            except ValueError as e:
                print("  ✘", e)
        elif p == "3":
            hasil = t.search_node(input("Kata kunci nama/jabatan: "))
            print(f"  Ditemukan {len(hasil)} hasil")
            for n in hasil:
                print("  -", n, "| atasan:", n.atasan.jabatan if n.atasan else "-")
        elif p == "4":
            tampilkan("PREORDER", t.preorder())
            tampilkan("INORDER", t.inorder())
            tampilkan("POSTORDER", t.postorder())
        elif p == "5":
            print(f"  Jumlah node: {t.jumlah_node()} | Tinggi: {t.tinggi()} level")
        elif p == "0":
            break


if __name__ == "__main__":
    main()
