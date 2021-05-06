import sys
import re

def main():
    with open(sys.argv[1], 'r') as f:
        stat = {}
        str_a = ' '
        while str_a:
            str_a = f.readline()
            # print(str_a)
            match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str_a)
            if match:
                ip = match[0]
                stat.setdefault(ip, {})
                match = re.search(r'" (\d{3}) ', str_a)
                if match:
                    code = match[1]
                    stat[ip].setdefault(code, 0)
                    stat[ip][code] += 1


        for k, v in stat.items():
            print(k)
            codes = sorted(
                [(code, count) for code, count in v.items()],
                key=lambda x: x[1],
                reverse=True,
            )
            for code, count in codes:
                print('    ', code, count)
if __name__ == main():
    main()