from abc import ABC, abstractmethod

class Araba(ABC):
    @abstractmethod
    def bilgileri_goster(self):
        pass

class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, batarya_durum):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.batarya_durum = batarya_durum

    def bilgileri_goster(self):
        return f"{self.yil} Model {self.marka} {self.model} - Batarya Durumu: {self.batarya_durum}%"

# Örnek Kullanım
if __name__ == "__main__":
    elektrikli_araba = ElektrikliAraba("Tesla", "Model S", 2023, 90)
    print(elektrikli_araba.bilgileri_goster())
