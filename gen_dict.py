version = '0.1'
wubi_dict = {}
with open('data/wubi86.dict.yaml') as f:
    table = f.read().split('...', 1)[1].strip()
    for line in table.splitlines():
        char, code, _ = line.split('\t', 2)
        if len(char) == 1:
            if len(code) >= len(wubi_dict.get(char, '')):
                wubi_dict[char] = code
print(f'got {len(wubi_dict)} wubi character code mappings')

lines = [
    '---',
    'name: zrm_wubi',
    f'version: {version}',
    'sort: original',
    '...'
]

handled = set()
with open('data/zrm2000.dict.yaml') as f:
    table = f.read().split('...', 1)[1].strip()
    for line in table.splitlines():
        if line.startswith('#'):
            continue
        # do not need reverse lookup by original rules
        if '[' in line and ']' in line:
            continue
        if line.endswith(','):
            lines.append(line)
            continue
        chars, code = line.split('\t')
        chars_len = len(chars)

        if chars in handled:
            continue

        if chars_len == 1:
            try:
                wubi_code = wubi_dict[chars]
            except KeyError:
                print(f'skipping {chars}')
                continue
            new_code = code[:chars_len * 2] + wubi_code
            lines.append(f'{chars}\t{new_code[:4]}')
            handled.add(chars)
        elif chars_len * 2 >= len(code):
            lines.append(line)
            continue
        else:
            try:
                wubi_code = ''.join([wubi_dict[c][0] for c in chars])
            except KeyError:
                print(f'skipping {chars}')
                continue
            new_code = code[:chars_len * 2] + wubi_code
            lines.append(f'{chars}\t{new_code}')
            handled.add(chars)

with open('zrm_wubi.dict.yaml', 'w') as f:
    f.write('\n'.join(lines))


