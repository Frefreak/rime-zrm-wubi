# like `gen_anxiliary` but use simplified code if presented

wubi_dict = {}
with open('../data/wubi86.dict.yaml') as f:
    table = f.read().split('...', 1)[1].strip()
    for line in table.splitlines():
        char, code, _ = line.split('\t', 2)
        if len(char) == 1:
            if len(code) < len(wubi_dict.get(char, '?????')):
                wubi_dict[char] = code

with open('anxiliary-simplified.txt', 'w') as f:
    for ch, code in wubi_dict.items():
        f.write(f'{ch}={code[:1]}\n')
