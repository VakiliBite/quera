used_benzin = int(input())
sahmiye_inmah = int(input())

sahmiye_mahbad = sahmiye_inmah + 60

if used_benzin <= sahmiye_mahbad:
    result = used_benzin * 1500
    print(result)
else:
    valid_usedbenzin = (used_benzin - sahmiye_mahbad) * 3000
    benzin_basahmie = sahmiye_mahbad * 1500
    
    result = valid_usedbenzin + benzin_basahmie
    print(result)
    
    