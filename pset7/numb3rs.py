import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search('^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', ip):
        n_ip = ip.split('.')
        for number in n_ip:
            if int(number) > 255 or int(number) < 0:
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    main()
# 18.07
