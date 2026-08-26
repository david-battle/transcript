import argparse
import re

pat = re.compile(r'^\d+:\d{2}\s*(?:\d+\s*minutes?\s*(?:,\s*)?)?(?:\d+\s*seconds?)?')


def strip_prefix(line):
    m = pat.match(line)
    if not m or m.end() == 0:
        return line
    return line[m.end():].lstrip()


def main():
    parser = argparse.ArgumentParser(description='Remove leading timestamps from transcript lines.')
    parser.add_argument('input', help='input transcript file')
    parser.add_argument('output', help='output file with timestamps removed')
    args = parser.parse_args()

    with open(args.input, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(args.output, 'w', encoding='utf-8') as f:
        f.writelines(strip_prefix(line) for line in lines)


if __name__ == '__main__':
    main()
