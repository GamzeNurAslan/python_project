with open("ornek_metin.txt", "r") as f:
    with open("gecenler.txt", "w") as g:
        with open("kalanlar.txt", "w") as k:
            icerik = f.readlines()
            n = 0
            for satir in icerik:
                if n==0:
                    n+=1
                    continue
                satir = satir.replace("\n", "")
                bosluk_sayisi = 0
                bosluk_indeksleri = []
                index = 0
                for karakter in satir:
                    if karakter == " ":
                        bosluk_sayisi += 1
                        bosluk_indeksleri.append(index)
                    index += 1
                ad_soyad = satir[:bosluk_indeksleri[0]]
                soyad = ad_soyad.split("-")[-1]
                ad = ad_soyad[:ad_soyad.index(soyad)-1].replace("-", " ")
                notlar = satir.split(" ")[-1]
                notlar = notlar.split("/")
                birinci_vize = int(notlar[0])
                ikinci_vize = int(notlar[1])
                final = int(notlar[2])
                ortalama = (birinci_vize * 0.3) + (ikinci_vize * 0.3) + (final * 0.4)
                bolum = satir[bosluk_indeksleri[0] + 1:bosluk_indeksleri[len(bosluk_indeksleri) - 1]]
                if ortalama >= 70 and final >= 70:
                    g.write(ad)
                    g.write(" " * (25- len(ad)))
                    g.write(soyad)
                    g.write(" " * (25 - len(soyad)))
                    g.write(bolum)
                    g.write(" " * (25 - len(bolum)))
                    g.write(str(round(ortalama, 1)))
                    g.write(" " * 21)
                    g.write("Geçti")
                    g.write("\n")
                else:
                    k.write(ad)
                    k.write(" " * (25 - len(ad)))
                    k.write(soyad)
                    k.write(" " * (25 - len(soyad)))
                    k.write(bolum)
                    k.write(" " * (25 - len(bolum)))
                    k.write(str(round(ortalama, 1)))
                    k.write(" " * 21)
                    k.write("Kaldı")

                    k.write("\n")




ornek_metin.txt
Adı-soyadı Bölümü Birinci Vize/İkinci Vize/Final
Eleanor-Taylor Fizik 78/90/70
Lyla-Dawson Matematik 98/67/100
Cora-Gill-Maryam Matematik Müh 76/78/93
Darcey-Parker Fizik 10/50/100
Jorgie-James Bilgisayar Müh 81/62/92
Amara-Allen-Eloise Kimya Müh 98/0/100
Keira-Khan Bilgisayar Müh 77/46/99
Scarlett-Stone Matematik 98/67/100
Arabella-Wallace Bilgisayar Müh 90/66/70
Darcey-Woods Fizik 42/87/98
Brynn-Thomas Kimya Müh 70/90/68
Robin-Spencer Matematik 89/98/97
Jamie-Dawson Fizik Müh 42/87/98
Val-Kaur Matematik Müh 67/54/100
Morgan-Pearson Bilgisayar Müh 42/87/98
Bailey-Gill-River Fizik 87/77/90
Alexis-Hamilton Fizik 42/87/98
Shay-Smith Matematik Müh 76/70/98
Silver-Barker Matematik 81/62/92
Brook-Kaur Matematik Müh 80/70/70
James-Harper Bilgisayar Müh 78/84/68
John-Hunter Fizik 48/60/72
Robert-Harper Kimya 96/86/70
Michael-Alex Kimya Müh 86/56/98
William-Hussain Fizik Müh 64/74/69
David-Knight Bilgisayar Müh 42/87/98
Richard-Jeff Matematik 68/76/45
Charles-Booth-Hamish Bilgisayar Müh 16/88/78
Joseph-Dillon-Spencer Matematik Müh 98/67/100
Thomas-James-Zachary Gıda Müh 86/77/81
Christopher-Dawson Bilgisayar Müh 81/62/92
Daniel-Porter Fizik Müh 16/88/92
Paul-Rufus-Pearson Matematik 60/84/95
Mark-Conor-Smith Kimya Müh 96/86/90
Donald-Kenneth-Eğilmez Kimya Müh 85/79/92
Steven-Johnson Fizik 89/68/84
Martin-Hank Bilgisayar Müh 86/89/67
George-Aston Kimya Müh 66/76/78
Kenneth-Rogers Fizik 46/73/60
Tim-Jack Matematik Müh 86/77/58
Edward-Frankie-Adams Fizik 100/100/67
Brian-John Kimya 86/90/70
Ronald-Tate Bilgisayar Müh 60/48/91
Anthony-Casper Fizik Müh 48/64/78
Kevin-Maxwell-Kennedy Matematik 62/85/71
Jason-Rogers Fizik Müh 85/26/98
Glen-Francis Fizik 88/76/78
Lee-Fletcher Bilgisayar Müh 93/56/71
Jo-Khan Matematik Müh 18/76/49
Bev-Cunningham Kimya Müh 18/88/90
Brook-Duncan Bilgisayar Müh 98/67/98
Phoenix-Phillips Matematik 67/87/79
Alicia-Jody-Pearson Fizik 56/76/99
Amalia-Atkinson Fizik Müh 83/73/60
Marley-Sienna-Robertson Bilgisayar Müh 99/100/69
Ariella-Hamilton Fizik 36/87/94
Rose-Jasmine-Francis Matematik 88/66/90
Lara-Mccarthy Kimya Müh 76/94/70
Jemima-Fox Matematik Müh 63/26/79
Blossom-Cooper Bilgisayar Müh 67/79/87
Stella-Thompson Fizik 95/78/94
Ariella-Davies Fizik Müh 17/89/98
Lily-Rose-Kelly Matematik 75/81/80
Gabe-Wells Bilgisayar Müh 56/94/72
Taylor-Evans Kimya Müh 67/84/69
Jamie-Henderson Matematik 28/88/94
