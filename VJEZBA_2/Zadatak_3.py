import asyncio

# simulacija baze podataka
baza_korisnika = [
  {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
  {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
  {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
  {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

# korutina 
async def autentifikacija(korisnik):
    await asyncio.sleep(3)
    
    for i in baza_korisnika:
        if(i["korisnicko_ime"]==korisnik["korisnicko_ime"]
            and i["email"]==korisnik["email"]):
            return True
    
    return False