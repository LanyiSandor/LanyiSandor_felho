# Függvény egy diagram sor elkészítésére egy adott nap és hőmérséklet alapján
def keszit_diagram_sort(nap_szama, homerseklet):
    csillagok_szama = int(homerseklet)  # A hőmérséklet alapján meghatározza, hány csillag legyen
    csillagok = '*' * csillagok_szama  # A csillagokból álló szöveg létrehozása
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)"  # A sor formázása: nap száma, csillagok, hőmérséklet
    return sor  # Visszatér a formázott sorral

# Függvény, amely kirajzolja az egész hőmérséklet diagramot
def rajzolj_diagram(homersekletek):
    print("Napi átlaghőmérséklet diagram (°C)")  # Címsor kiírása
    print("-" * 40)  # Elválasztó vonal kiírása

    # Végigmegy a hőmérsékletlista elemein
    for i in range(len(homersekletek)):
        nap = i + 1  # A napok számozása 1-től indul
        sor = keszit_diagram_sort(nap, homersekletek[i])  # Elkészíti a diagram sort az adott napra
        print(sor)  # Kiírja a sort

# Lista, amely tartalmazza egy hét napi átlaghőmérsékleteit
napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]

# Meghívja a rajzolj_diagram függvényt a hőmérsékleti adatokkal
rajzolj_diagram(napi_atlaghomersekletek)


