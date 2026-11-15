"""Perbandingan kecepatan pada pohon SEIMBANG vs CONDONG (skewed), n sama."""
import json
import random
import sys
import time

from org_tree import Node, OrgTree

sys.setrecursionlimit(20000)


def seimbang(n: int, cabang: int = 3) -> tuple[OrgTree, list[Node]]:
    root = Node("0", "n0", "j0"); sem = [root]; i = 1
    while i < n:
        induk = sem[(i - 1) // cabang]
        c = Node(str(i), f"n{i}", f"j{i}"); c.atasan = induk; induk.bawahan.append(c); sem.append(c); i += 1
    return OrgTree(root), sem


def condong(n: int) -> tuple[OrgTree, list[Node]]:
    root = Node("0", "n0", "j0"); sem = [root]
    for i in range(1, n):
        c = Node(str(i), f"n{i}", f"j{i}"); c.atasan = sem[-1]; sem[-1].bawahan.append(c); sem.append(c)
    return OrgTree(root), sem


def ukur(fn, ulang=20):
    t0 = time.perf_counter()
    for _ in range(ulang):
        fn()
    return (time.perf_counter() - t0) / ulang * 1e3     # ms


def main():
    hasil = {}
    n = 3280                       # (3^8-1)/2 -> pohon 3-cabang penuh 8 level
    for nama, builder in [("Seimbang (3 cabang)", lambda: seimbang(n)), ("Condong (rantai)", lambda: condong(n))]:
        t, sem = builder()
        rnd = random.Random(7)
        targets = [rnd.choice(sem).nama for _ in range(100)]
        terdalam = max(sem, key=lambda x: len(t.jalur_ke_root(x)))
        r = {
            "n": t.jumlah_node(), "tinggi": t.tinggi(),
            "search_acak_ms": ukur(lambda: [t.search_node(x, "nama") for x in targets[:20]], 5) / 20,
            "search_terdalam_ms": ukur(lambda: t.search_node(terdalam.nama, "nama")),
            "preorder_ms": ukur(t.preorder), "inorder_ms": ukur(t.inorder), "postorder_ms": ukur(t.postorder),
            "jalur_ke_root_ms": ukur(lambda: t.jalur_ke_root(terdalam), 200),
            "panjang_jalur": len(t.jalur_ke_root(terdalam)),
        }
        hasil[nama] = r
        print(nama); [print(f"   {k:<20}{v:.4f}" if isinstance(v, float) else f"   {k:<20}{v}") for k, v in r.items()]
    json.dump(hasil, open("hasil_benchmark_bentuk.json", "w"), indent=2)


if __name__ == "__main__":
    main()
