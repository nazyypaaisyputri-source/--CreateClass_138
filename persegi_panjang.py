class PersegiPanjang:
    # 1. Konstruktor (__init__) untuk properti panjang dan lebar
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    # 2. Fungsi untuk menghitung keliling
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    # 3. Fungsi untuk menghitung luas
    def luas(self):
        return self.panjang * self.lebar

    # 4. Fungsi __str__ untuk menampilkan format teks
    def __str__(self):
        return f"persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"