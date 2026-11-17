from digital_garden.contract import get_contract


request = [1, 2, 'all-tags-format']
subset = get_contract(request)
for name in subset:
    print(name)
