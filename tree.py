# =========================================
# TREE
# Digunakan untuk merepresentasikan struktur
# hierarki sel penjara.
# =========================================

class TreeNode: # membuat satu node pada Tree

    def __init__(self, nama):
        self.nama = nama  # menyimpan nama node
        self.child1 = None # anak/cabang pertama
        self.child2 = None  # anak/cabang kedua

# Fungsi rekursif untuk menampilkan tree
def tampil_tree(node, level=0):

    if node is not None: # Jika node masih ada
        
        # Menampilkan nama node sesuai level
        print("  " * level + node.nama)

        # Menampilkan cabang kiri
        tampil_tree(node.child1, level + 1)

        # Menampilkan cabang kanan
        tampil_tree(node.child2, level + 1)