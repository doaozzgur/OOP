class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgileri_goster(self):
        return f"{self.yil} Model {self.marka} {self.model}"

# Örnek Kullanım
if __name__ == "__main__":
    araba = Araba("Toyota", "Corolla", 2022)
    print(araba.bilgileri_goster())
