import asyncio
import random

# korutina za provjeru parnost
async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    
    if broj%2==0:
        return f"Broj {broj} je prazan"
    else:
        return f"Broj {broj} je neparan"