import unicodedata, argparse
from rich.console import Console

console = Console()

def parser():
    p = argparse.ArgumentParser()
    p.add_argument('-s', type=str, help='String to unormalize')
    p.add_argument('-f', default=['NFC','NFD','NFKC','NFKD'], help='Normalisation format')
    p.add_argument('--verbose', action='store_true', help='Verbose mode')
    return p.parse_args()

def find_characters_normalized_to_l(character, format):
    results = []
    for code_point in range(0x110000):  # Unicode range
        char = chr(code_point)
        normalized = unicodedata.normalize(format, char)
        if normalized == character:
            results.append(char)
    return results


if __name__ == '__main__':
    print('unormalizer --- by 0xlildoudou')
    args = parser()

    all = []

    with console.status("[bold green]Convert characters...") as status:
        for character in args.s:
            special_characters = find_characters_normalized_to_l(character, args.f)
            all.append(special_characters)
            if args.verbose:
                console.log(f"Characters that normalize to {character} :", special_characters)

    max_length = max(len(sublist) for sublist in all)

    for i in range(max_length):
        chars = []
        for sublist in all:
            if i < len(sublist):
                chars.append(sublist[i])
            else:
                chars.append(all[0][i] if i < len(all[0]) else '')
        print(''.join(chars))