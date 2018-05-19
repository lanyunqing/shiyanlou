import sys

s = sys.argv[1:]
s_li = []
for li in s:
    l = li.split(":")
    s_li.append(l)

for li in s_li:
    number, gz = li
    sd = 0
    try:
        gz = float(gz)
        sd = gz - (gz * 0.165) - 3500
    except ValueError:
        print("Parmaeter Error")

    if sd > 80000:
        se = sd * 0.45 - 13505
        sh = gz - (gz * 0.165) - se
        print("{}:{:.2f}".format(number, sh))
    elif sd > 55000:
        se = sd * 0.35 - 5505
        sh = gz - (gz * 0.165) - se
        print("{}:{:.2f}".format(number, sh))
    elif sd > 35000:
        se = sd * 0.3 - 2755
        sh = gz - (gz * 0.165) - se
        print("{}:{:.2f}".format(number, sh))
    elif sd > 9000:
        se = sd * 0.25 - 1005
        sh = gz - (gz * 0.165) - se
        print("{}:{:.2f}".format(number, sh))
    elif sd > 4500:
        se = sd * 0.2 - 555
        sh = gz - (gz * 0.165) - se
        print("{}:{:.2f}".format(number, sh))
    elif sd > 1500:
        se = sd * 0.1 - 105
        sh = gz - (gz * 0.165) - se
        print("{}:{:.2f}".format(number, sh))
    elif sd > 0:
        se = sd * 0.03
        sh = gz - (gz * 0.165) - se
        print("{}:{:.2f}".format(number, sh))
    elif sd <  0:
        se = 0
        sh = gz - (gz * 0.165) - se
        print("{}:{:.2f}".format(number, sh))
