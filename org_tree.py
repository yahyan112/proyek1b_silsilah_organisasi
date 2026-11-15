"""Silsilah Organisasi UIN Suska Riau - General Tree (OOP).

Dipilih GENERAL TREE (bukan BST) karena satu atasan dapat memiliki banyak
bawahan dan urutan antar-node ditentukan hierarki jabatan, bukan nilai kunci.
"""
from collections import deque
from typing import Callable, Optional


class Node:
    """Satu simpul = satu pegawai/jabatan."""

    def __init__(self, id_pegawai: str, nama: str, jabatan: str):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.jabatan = jabatan
        self.atasan: Optional["Node"] = None      # pointer ke parent
        self.bawahan: list["Node"] = []           # daftar child

    def __repr__(self) -> str:
        return f"{self.jabatan} - {self.nama}"


class OrgTree:
    def __init__(self, root: Node):
        self.root = root

    # ------------------------------------------------------------------
    # Operasi dasar
    # ------------------------------------------------------------------
    def _cari_atasan(self, kunci: str) -> Optional[Node]:
        """Cari atasan berdasarkan ID, nama, atau jabatan (persis, tanpa huruf besar/kecil)."""
        k = kunci.strip().lower()
        for n in self._dfs():
            if k in (n.id_pegawai.lower(), n.nama.lower(), n.jabatan.lower()):
                return n
        return None

    def insert_node(self, atasan: str, id_pegawai: str, nama: str, jabatan: str) -> Node:
        """Menyisipkan pegawai baru sebagai bawahan dari `atasan`.

        `atasan` boleh berupa ID, nama, atau jabatan atasan. Kompleksitas O(n)
        karena atasan dicari lebih dulu; penyisipan node itu sendiri O(1).
        """
        if any(n.id_pegawai == id_pegawai for n in self._dfs()):
            raise ValueError(f"ID {id_pegawai} sudah dipakai.")
        induk = self._cari_atasan(atasan)
        if induk is None:
            raise ValueError(f"Atasan '{atasan}' tidak ditemukan.")
        baru = Node(id_pegawai, nama, jabatan)
        baru.atasan = induk
        induk.bawahan.append(baru)
        return baru

    def search_node(self, kata_kunci: str, berdasarkan: str = "semua") -> list[Node]:
        """Mencari pegawai berdasarkan nama atau jabatan (mengandung kata kunci).

        berdasarkan: "nama" | "jabatan" | "semua" (nama ATAU jabatan).
        Mengembalikan daftar node yang cocok. Kompleksitas O(n).
        """
        k = kata_kunci.strip().lower()
        hasil = []
        for n in self._dfs():
            cocok_nama = k in n.nama.lower()
            cocok_jabatan = k in n.jabatan.lower()
            if (berdasarkan == "nama" and cocok_nama) or \
               (berdasarkan == "jabatan" and cocok_jabatan) or \
               (berdasarkan == "semua" and (cocok_nama or cocok_jabatan)):
                hasil.append(n)
        return hasil

    def _dfs(self):
        """Iterasi seluruh node (iteratif, aman untuk pohon yang sangat dalam)."""
        stack = [self.root]
        while stack:
            n = stack.pop()
            yield n
            stack.extend(reversed(n.bawahan))

    # ------------------------------------------------------------------
    # Traversal  (masing-masing O(n), mengunjungi tiap node tepat sekali)
    # ------------------------------------------------------------------
    def preorder(self, node: Optional[Node] = None, hasil: Optional[list] = None) -> list[Node]:
        """Preorder: NODE -> semua anak (kiri ke kanan)."""
        node = node or self.root
        hasil = [] if hasil is None else hasil
        hasil.append(node)
        for anak in node.bawahan:
            self.preorder(anak, hasil)
        return hasil

    def inorder(self, node: Optional[Node] = None, hasil: Optional[list] = None) -> list[Node]:
        """Inorder (general tree): ANAK PERTAMA -> NODE -> anak-anak sisanya.

        Pada binary tree ini setara dengan Left -> Node -> Right.
        """
        node = node or self.root
        hasil = [] if hasil is None else hasil
        if node.bawahan:
            self.inorder(node.bawahan[0], hasil)
        hasil.append(node)
        for anak in node.bawahan[1:]:
            self.inorder(anak, hasil)
        return hasil

    def postorder(self, node: Optional[Node] = None, hasil: Optional[list] = None) -> list[Node]:
        """Postorder: semua anak (kiri ke kanan) -> NODE."""
        node = node or self.root
        hasil = [] if hasil is None else hasil
        for anak in node.bawahan:
            self.postorder(anak, hasil)
        hasil.append(node)
        return hasil

    # ------------------------------------------------------------------
    # Metrik bentuk pohon & utilitas tampilan
    # ------------------------------------------------------------------
    def jumlah_node(self) -> int:
        return sum(1 for _ in self._dfs())

    def tinggi(self) -> int:
        """Tinggi pohon dalam jumlah level (root saja = 1). Iteratif BFS."""
        level, antrean = 0, deque([self.root])
        while antrean:
            level += 1
            for _ in range(len(antrean)):
                antrean.extend(antrean.popleft().bawahan)
        return level

    def jalur_ke_root(self, node: Node) -> list[Node]:
        """Rantai komando dari node ke Rektor. O(h) dengan h = tinggi pohon."""
        jalur = []
        while node is not None:
            jalur.append(node)
            node = node.atasan
        return jalur

    def cetak_pohon(self, node: Optional[Node] = None, awalan: str = "", terakhir: bool = True,
                    akar: bool = True) -> None:
        node = node or self.root
        if akar:
            print(f"{node.jabatan} - {node.nama}")
        else:
            print(f"{awalan}{'└── ' if terakhir else '├── '}{node.jabatan} - {node.nama}")
        anak_awalan = awalan if akar else awalan + ("    " if terakhir else "│   ")
        for i, anak in enumerate(node.bawahan):
            self.cetak_pohon(anak, anak_awalan, i == len(node.bawahan) - 1, akar=False)


def tampilkan(judul: str, urutan: list[Node], fmt: Callable[[Node], str] = repr) -> None:
    print(f"\n{judul}")
    for i, n in enumerate(urutan, 1):
        print(f"  {i:>2}. {fmt(n)}")
