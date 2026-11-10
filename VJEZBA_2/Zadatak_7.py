# 1. asyncio.run(main()) pokrece event loop
# 2. asyncio.create_task() kreira tri Task objekta i rasporeduje ih za izvrsavanje
# 3. await asyncio.gather(*timers) event loop pokrece sva tri zadatka
# 4. await asyncio.sleep(1) privremeno se zaustavlja korutina tako da event loop
# izvrsava druge zadatke
# 5. nakon sekunde, suspendirane korutine su ponovno spremne za izvrsavanje
# 6. zakljucno: nakon 3 sekunde zavrsava timer 1, nakon 5 sec timer 2, nakon 7 sec timer 3
# 7. izlaz: asyncio.gather() ceka da se sva tri zadatka izvrse te zavrsava main() te se zatvara event loop
 