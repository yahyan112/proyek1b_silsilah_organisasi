"""Data contoh (nama pegawai FIKTIF) untuk demo."""
from org_tree import Node, OrgTree


def struktur_uin() -> OrgTree:
    """Struktur buatan sendiri: Rektor > Dekan > Ketua Prodi > Dosen/Staf."""
    t = OrgTree(Node("R01", "Prof. Ahmad Fauzi", "Rektor"))
    data = [
        ("Rektor", "WR1", "Dr. Siti Rahmah", "Wakil Rektor I"),
        ("Rektor", "WR2", "Dr. Budi Santoso", "Wakil Rektor II"),
        ("Rektor", "WR3", "Dr. Nurul Huda", "Wakil Rektor III"),
        ("Rektor", "D01", "Dr. Hendra Wijaya", "Dekan Fakultas Sains dan Teknologi"),
        ("D01", "WD1", "Dr. Rina Marlina", "Wakil Dekan I"),
        ("D01", "WD2", "Dr. Yusuf Hakim", "Wakil Dekan II"),
        ("D01", "KP1", "Dr. Dewi Lestari", "Ketua Program Studi Teknik Informatika"),
        ("D01", "KP2", "Dr. Andi Pratama", "Ketua Program Studi Sistem Informasi"),
        ("KP1", "DS1", "Rizky Maulana, M.Kom.", "Dosen Teknik Informatika"),
        ("KP1", "DS2", "Putri Anggraini, M.T.", "Dosen Teknik Informatika"),
        ("KP1", "ST1", "Fajar Nugroho, S.Kom.", "Staf Administrasi Prodi TI"),
        ("KP2", "DS3", "Dian Permata, M.Kom.", "Dosen Sistem Informasi"),
    ]
    for atasan, id_, nama, jabatan in data:
        t.insert_node(atasan, id_, nama, jabatan)
    return t


def struktur_baru() -> OrgTree:
    """Struktur pada soal No. 11 (diagram dari lembar aktivitas)."""
    t = OrgTree(Node("N01", "-", "Rektor"))
    data = [
        ("Rektor", "N02", "Senat Universitas"),
        ("Rektor", "N03", "Wakil Rektor I (Bidang Akademik)"),
        ("Rektor", "N04", "Wakil Rektor II (Bidang Administrasi Umum & Keuangan)"),
        ("Rektor", "N05", "Wakil Rektor III (Bidang Kemahasiswaan & Kerja Sama)"),
        ("Rektor", "N06", "Dekan Fakultas Sains dan Teknologi"),
        ("N06", "N07", "Wakil Dekan I (Bidang Akademik & Kelembagaan)"),
        ("N06", "N08", "Wakil Dekan II (Bidang AUPK)"),
        ("N06", "N09", "Wakil Dekan III (Bidang Kemahasiswaan)"),
        ("N06", "N10", "Ketua Program Studi Teknik Informatika"),
        ("N10", "N11", "Sekretaris Program Studi"),
        ("N10", "N12", "Kepala Laboratorium Komputer"),
        ("N10", "N13", "Koordinator Dosen"),
        ("N12", "N14", "Asisten Laboratorium"),
        ("N12", "N15", "Teknisi Laboratorium"),
        ("N13", "N16", "Dosen Pembimbing Akademik"),
        ("N13", "N17", "Dosen Pengampu Mata Kuliah"),
        ("N16", "N18", "Mahasiswa Bimbingan"),
    ]
    for atasan, id_, jabatan in data:
        t.insert_node(atasan, id_, "-", jabatan)
    return t
