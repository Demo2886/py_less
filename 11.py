from collections import Counter
import re

# commit
def main():
    data = open('log').read()

    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ips = re.findall(pattern, data)

    result = Counter(ips)
    print(result)

if __name__ == '__name__':
    main()
