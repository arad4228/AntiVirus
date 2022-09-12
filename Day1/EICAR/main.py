import os

vf = open('eicat.txt', 'w')
virus = 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
vf.write(virus)
vf.close()

# 바이너리 모드로 읽기
fp = open('eicat.txt', 'rb')
fbuf = fp.read()
fp.close()

if fbuf[0:3] == b'X5O':
    print("Virus")
    os.remove('eicat.txt')
else:
    print("No Virus")