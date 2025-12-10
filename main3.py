import os

def duzenle():
    klasor = input("Düzenlenecek klasor:")
    dosyalar= []
    uzantilar = []
    def list_dir():
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor, dosya)):
                continue
            if dosya.startswith("."):
                continue
            else:
                dosyalar.append(dosya)
    list_dir()
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        if uzanti in uzantilar:
            continue
        else:
            uzantilar.append(uzanti)
    for uzanti in uzantilar:
        if os.path.isdir(os.path.join(klasor,uzanti)):
            continue
        else:
            os.mkdir(os.path.join(klasor,uzanti))
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        os.rename(os.path.join(klasor, dosya),os.path.join(klasor,uzanti, dosya))

if __name__ == ("__main__"):
    duzenle()