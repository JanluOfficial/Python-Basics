def conatinsM(string: str) -> bool:
    return 'm' in string

names = [
    'Betti',
    'Kyle',
    'Quantum',
    'Damilare',
    'Janlu',
    'DevilKing',
    'Iridescent',
    'Antony',
    'BK1902',
    'Mr8long',
]

## Pre-reduced names
print(names)

## Reduced names
print(list(filter(conatinsM, names)))
