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
                stat.setdefault(ip, 0)
                stat[ip] += 1

        print(stat)
if __name__ == main():
    main()