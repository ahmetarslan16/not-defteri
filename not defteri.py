notlar = []
while True:
    print("\nNOT DEFTERİ")
    print("1 - Not Ekle")
    print("2 - Notları Listele")
    print("3 - Çıkış")

    secim = input("Seçiminizi girin: ")

    if secim == "1":
        not_metni = input("Notunuzu yazın: ")
        notlar.append(not_metni)
        # Her eklemede dosyaya kaydedelim
        with open("notlar.txt", "w", encoding="utf-8") as f:
            for n in notlar:
                f.write(n + "\n")
        print("✅ Not eklendi.")

    elif secim == "2":
        if not notlar:
            print("📂 Henüz hiç not yok.")
        else:
            print("\n--- Notlar ---")
            for i, n in enumerate(notlar, 1):
                print(f"{i}. {n}")

    elif secim == "3":
        print("📌 Programdan çıkılıyor...")
        break

    else:
        print("⚠ Geçersiz seçim, tekrar deneyin.")

def kaydet():
    with open(notlarg)