import os
from datetime import datetime
def duzenle():
    klasor = input("Duzenlenecek Klasor : ")
    dosyalar = []
    tarihler = []
    def list_dir():
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor,dosya)):
                continue
            if dosya.startswith("."):
                continue
            else:
                dosyalar.append(dosya)
    list_dir()
    for dosya in dosyalar:
        tarih_damgası = os.stat(os.path.join(klasor,dosya))
        tarih = datetime.fromtimestamp(tarih_damgası).strftime("%d-%m-%Y")
        if tarih in tarihler:
            continue
        else:
            tarihler.append(tarih)

    for tarih in tarihler:
        if os.path.isdir(os.path.join(klasor,tarih)):
            continue
        else:
            os.mkdir(os.path.join(klasor,tarih))
    for dosya in dosyalar:
        tarih_damgası = os.stat(os.path.join(klasor, dosya)).st_birthtime()
        tarih = datetime.fromtimestamp(tarih_damgası).strftime("%d-%m-%Y")
        os.rename(os.path.join(klasor,dosya), os.path.join(klasor, tarih, dosya))

if __name__ == "__main__":
     duzenle()

