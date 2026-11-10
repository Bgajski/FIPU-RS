import asyncio

# korutina za simulaciju dohvacanja podataka
async def dohvati_podatke():
    brojevi=[i for i in range(1,11)]
    await asyncio.sleep(3)
    
    print("Podaci dohvaceni")
    return brojevi

# pokretanje korutine
async def main():
    podaci=await dohvati_podatke()
    print(podaci)

asyncio.run(main())