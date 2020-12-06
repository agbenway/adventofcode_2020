from passwords import DaylyInput
import re
import functools

class Passport(object):
    def __init__(self, initial_data):
        keys = initial_data.keys()
        if keys.__contains__('byr'):
            self.byr = initial_data['byr']
        if keys.__contains__('iyr'):
            self.iyr = initial_data['iyr']
        if keys.__contains__('eyr'):
            self.eyr = initial_data['eyr']
        if keys.__contains__('hgt'):
            self.hgt = initial_data['hgt']
        if keys.__contains__('hcl'):
            self.hcl = initial_data['hcl']
        if keys.__contains__('ecl'):
            self.ecl = initial_data['ecl']
        if keys.__contains__('pid'):
            self.pid = initial_data['pid']
        if keys.__contains__('cid'):
            self.cid = initial_data['cid']

    def hasRequiredFields(self):
        if hasattr(self, 'byr') and hasattr(self, 'iyr') and hasattr(self, 'eyr') and hasattr(self, 'hgt') and hasattr(self, 'hcl') and hasattr(self, 'ecl') and hasattr(self, 'pid'):
            return True

    def hasValidFields(self):
        vByr = vIyr = vEyr = vHgt = vHcl = vEcl = vPid = False
        if len(self.byr) == 4 and int(self.byr) >= 1920 and int(self.byr) <= 2002:
            print('byr = true')
            vByr = True
        if len(self.iyr) == 4 and int(self.iyr) >= 2010 and int(self.iyr) <= 2020:
            print('iyr = true')
            vIyr = True
        if len(self.eyr) == 4 and int(self.eyr) >= 2020 and int(self.eyr) <= 2030:
            print('eyr = true')
            vEyr = True
        if re.search('^#[a-f0-9]{6}$', self.hcl):
            print('hcl = true')
            vHcl = True
        if re.search('^[amb|blu|brn|gry|grn|hzl|oth]{3}$', self.ecl):
            print('ecl = true')
            vEcl = True
        if re.search(r'^\d{9}$', self.pid):
            print('pid = true')
            vPid = True
        height = re.split(r'(\d+)', self.hgt)
        print(height)
        if len(height) == 3 and re.search('[cm]|[in]', height[2]):
            if height[2] == 'cm' and re.search(r'^\d{3}$',height[1]) and int(height[1]) >= 150 and int(height[1]) <= 193:
                vHgt = True
            elif height[2] == 'in' and re.search(r'^\d{2}$',height[1]) and int(height[1]) >= 59 and int(height[1]) <= 76:
                vHgt = True
        isValid = vByr and vIyr and vEyr and vHgt and vHcl and vEcl and vPid and True
        print(f'isValid = {isValid}')
        return isValid

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        # hgt (Height) - a number followed by either cm or in:
            # If cm, the number must be at least 150 and at most 193.
            # If in, the number must be at least 59 and at most 76.
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        # cid (Country ID) - ignored, missing or not.

input = DaylyInput().GetDaylyInput(4).content.decode('utf-8').split('\n\n')

passports = [x.replace('\n', ' ') for x in input]
required = 0
count = 0
listOfPassports = [dict(x.split(":") for x in pa.split(" ") if x.find(':') != -1) for pa in passports]

for d in listOfPassports:
    print(d)
    p = Passport(d)
    if p.hasRequiredFields():
        required +=1
        if p.hasValidFields():
            count += 1

print(f'********* {count} && required {required}')
# for d in listOfPassports:
#     key = list(d.keys())
#     print(key)
#     if len(key) >= 7:
#         diff = list(set(valid) - set(key))
#         print(f'diff: {diff} & len: {len(diff)}')
#         if (len(diff) < 1):
#             count += 1
#         elif (diff[0] == 'cid'):
#             count += 1

