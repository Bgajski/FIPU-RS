import asyncio

# korutina za simulaciju enkripcije
async def secure_data(podaci):
    await asyncio.sleep(3)
    
    return{
        "prezime": podaci["prezime"],
        "broj_kartice": hash(podaci["broj_kartice"]),
        "CVV": hash(podaci["CVV"])
    }