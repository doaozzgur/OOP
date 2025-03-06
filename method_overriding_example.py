class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgileri_goster(self):
        return f"{self.yil} Model {self.marka} {self.model}"

class SporAraba(Araba):
    def __init__(self, marka, model, yil, hiz):
        super().__init__(marka, model, yil)
        self.hiz = hiz

    def bilgileri_goster(self):
        return f"{super().bilgileri_goster()} - Hız: {self.hiz} km/s"

# Örnek Kullanım
if __name__ == "__main__":
    spor_araba = SporAraba("Porsche", "911", 2023, 300)
    print(spor_araba.bilgileri_goster())
