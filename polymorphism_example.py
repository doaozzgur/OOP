class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgileri_goster(self):
        return f"{self.yil} Model {self.marka} {self.model}"

class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, batarya_durum):
        super().__init__(marka, model, yil)
        self.batarya_durum = batarya_durum

    def bilgileri_goster(self):
        return f"{super().bilgileri_goster()} - Batarya Durumu: {self.batarya_durum}%"

# Polymorphism
def araba_bilgisi(araba):
    print(araba.bilgileri_goster())

if __name__ == "__main__":
    araba = Araba("Ford", "Focus", 2021)
    elektrikli_araba = ElektrikliAraba("Tesla", "Model 3", 2023, 80)

    araba_bilgisi(araba)
    araba_bilgisi(elektrikli_araba)
