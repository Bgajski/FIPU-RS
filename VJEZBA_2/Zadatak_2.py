import asyncio

# korutina za dohvacanje korisnika
async def dohvati_korisnike():
    await asyncio.sleep(3)
    
    korisnici=[
        {"id": 1, "ime":"Benjamin"},
        {"id": 2, "ime":"Ana"},
        {"id": 3, "ime":"Marko"}
    ]
    
    return korisnici

# korutina za dohvacanje proizvoda
async def dohvati_proizvode():
    await asyncio.sleep(5)
    
    proizvodi=[
        {"id": 1, "ime":"Tipkovnica"},
        {"id": 2, "ime":"Mis"},
        {"id": 3, "ime":"usb"}
    ]