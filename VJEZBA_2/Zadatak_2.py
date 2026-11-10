import asyncio

# korutina za dohvacanje
async def dohvati_korisnike():
    await asyncio.sleep(3)
    
    korisnici=[
        {"id": 1, "ime":"Benjamin"}
        {"id": 2, "ime":"Ana"}
        {"id": 3, "ime":"Marko"}
    ]
    
    return korisnici