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

# provjera autentifikacije korisnika
baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def main():
    korisnik = {
        "korisnicko_ime": "mirko123",
        "email": "mirko123@gmail.com",
        "lozinka": "lozinka123"
    }

    rezultat = await autentifikacija(korisnik)

    if rezultat:
        print("Korisnik je pronaden u bazi.")
    else:
        print("Korisnik nije pronaden u bazi.")


asyncio.run(main())