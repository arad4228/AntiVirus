import os
import hashlib

vf = open('eicat.txt', 'w')
virus = 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
vf.write(virus)
vf.close()

# 바이너리 모드로 읽기
fp = open('eicat.txt', 'rb')
fbuf = fp.read()
fp.close()

m = hashlib.md5()
m.update(fbuf)
fmd5 = m.hexdigest()

if fmd5 == '44d88612fea8a8f36de82e1278abb02f':
    print("Virus")
    os.remove('eicat.txt')
else:
    print("No Virus")