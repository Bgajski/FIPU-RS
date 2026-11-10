import asyncio
import re

# korutina za simulaciju enkripcije
async def secure_data(podaci):
    await asyncio.sleep(3)
    
    return{
        "prezime": podaci["prezime"],
        "broj_kartice": abs(hash(podaci["broj_kartice"])),
        "CVV": abs(hash(podaci["CVV"]))
    }
    
# definiranje podataka i pokretanje korutine
async def main():
    osjetljivi_podaci=[
        {"prezime": "Benjamin", "broj_kartice": "1234567812345678", "CVV": "123"},
        {"prezime": "Kovac", "broj_kartice": "8765432187654321", "CVV": "456"},
        {"prezime": "Novak", "broj_kartice": "1111222233334444", "CVV": "789"}
    ]
    
    zadaci=[asyncio.create_task(secure_data(podaci)) for podaci in osjetljivi_podaci]
    
    rezultati=await asyncio.gather(*zadaci)
    
    for i in rezultati:
        print(i)
        
asyncio.run(main())