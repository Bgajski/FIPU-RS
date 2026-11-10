import asyncio
import random

# korutina za provjeru parnost
async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    
    if broj%2==0:
        return f"Broj {broj} je prazan"
    else:
        return f"Broj {broj} je neparan"

# generiranje brojeva 
async def main():
    brojevi=[random.randint(1,100) for i in range(10)]
    
    zadaci=[asyncio.create_task(provjeri_parnost(broj)) for broj in brojevi]
    
    rezultati=await asyncio.gather(*zadaci)
    
    for i in rezultati:
        print(i)
        
asyncio.run(main())