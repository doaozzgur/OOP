class Araba:
    def __init__(self, marka, model, yil):
        self.__marka = marka
        self.__model = model
        self.__yil = yil

    def bilgileri_goster(self):
        return f"{self.__yil} Model {self.__marka} {self.__model}"

    def set_marka(self, marka):
        self.__marka = marka

    def get_marka(self):
        return self.__marka

# Örnek Kullanım
if __name__ == "__main__":
    araba = Araba("BMW", "M3", 2022)
    print(araba.bilgileri_goster())

    araba.set_marka("Audi")
    print(araba.get_marka())
