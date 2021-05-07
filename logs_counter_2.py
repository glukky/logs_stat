import sys
import re

def main():
	stat = {}
	with open(sys.argv[1], 'r') as f:
		line = ' '
		while line:
			match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
			if match:
				ip = match[0]
				stat.setdefault(ip, {})
				stat[ip].setdefault('all', 0)
				match = re.search(r'" (\d{3})', line)
				if match:
					code = match[1]
					stat[ip].setdefault(code, 0)
					stat[ip][code] += 1
				stat[ip]['all'] += 1
			line = f.readline()

	list_stat = []
	for key, value in stat.items():
		list_stat.append((key, value['all']))
	list_stat = sorted(list_stat, key=lambda x: x[1], reverse=True)
	for ip, count in list_stat:
		list_codes = [(code, code_count) for code, code_count in stat[ip].items()]
		list_codes = sorted(list_codes, key=lambda x: x[1], reverse=True)
		print(ip, count)
		for code, code_count in list_codes:
			if code != 'all':
			    print('   ', code, code_count)

if __name__ == '__main__':
	main()
