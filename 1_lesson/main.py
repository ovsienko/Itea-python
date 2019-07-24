cap = {
    'Ukraine': 'Kyiv',
    'Poland': 'Warsaw',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'Norway': 'Oslo'}
countryes = ['Poland', 'Canada', 'Spain', 'Moldova']

for x in countryes:
    if cap.has_key(x):
            print(cap[x])
