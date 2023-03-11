wubi_dict = {}
with open('../data/wubi86.dict.yaml') as f:
    table = f.read().split('...', 1)[1].strip()
    for line in table.splitlines():
        char, code, _ = line.split('\t', 2)
        if len(char) == 1:
            if len(code) >= len(wubi_dict.get(char, '')):
                wubi_dict[char] = code

with open('anxiliary.txt', 'w') as f:
    for ch, code in wubi_dict.items():
        if len(code) < 2:
            print(f"{ch} has code {code} whose length is smaller than 2")
        f.write(f'{ch}={code[:2]}\n')
