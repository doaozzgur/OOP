class Araba:
    def __init__(self, marka, model, yil, renk="Beyaz"):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.renk = renk

    def bilgileri_goster(self):
        return f"{self.yil} Model {self.marka} {self.model} - Renk: {self.renk}"

# Örnek Kullanım
if __name__ == "__main__":
    araba = Araba("Ford", "Fiesta", 2021, "Mavi")
    print(araba.bilgileri_goster())

    # Renk verilmezse default renk beyaz olur
    araba2 = Araba("Opel", "Corsa", 2020)
    print(araba2.bilgileri_goster())
