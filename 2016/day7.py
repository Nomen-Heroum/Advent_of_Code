import src
import regex as re

IPS = src.read()


def count_tls(ips: list):
    count = 0
    for ip in ips:
        valid = re.search(r'(\w)(?!\1)(\w)\2\1', ip)
        invalid = re.search(r'\[\w*(\w)(?!\1)(\w)\2\1\w*]', ip)
        if valid and not invalid:
            count += 1
    return count


def count_ssl(ips: list):
    count = 0
    for ip in ips:
        support = False
        sub = re.sub(r'\[\w+]', '-', ip)
        for mo in re.finditer(r'(\w)(?!\1)\w\1', sub, overlapped=True):
            aba = mo[0]
            bab = aba[1] + aba[0] + aba[1]
            if re.search(r'\[\w*' + bab + r'\w*\]', ip):
                support = True
        if support:
            count += 1
    return count


def main(ips=IPS):
    print("Part One:")
    ans1 = count_tls(ips)
    print(f"{ans1} IPs support TLS.")

    print("\nPart Two:")
    ans2 = count_ssl(ips)
    print(f"{ans2} IPs support SSL.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
