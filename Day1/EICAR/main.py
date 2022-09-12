import os
import hashlib

vf = open('eicat.txt', 'w')
virus = 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
vf.write(virus)
vf.close()

df = open('DummyTest.txt', 'w')
dummy = 'Dummy Engine test file = KICOM Anti-Virus Project, 2012, Kei Choi'
df.write(dummy)
df.close()

# 바이너리 모드로 읽기
fp = open('DummyTest.txt', 'rb')
fbuf = fp.read()
fp.close()

# 바이너리 모드로 읽기
fp = open('eicat.txt', 'rb')
# fp = open('DummyTest.txt', 'rb')
fbuf = fp.read()
fp.close()

m = hashlib.md5()
m.update(fbuf)
fmd5 = m.hexdigest()

if fmd5 == '44d88612fea8a8f36de82e1278abb02f':
    print("Virus")
    os.remove('eicat.txt')
elif fmd5 == '77bff0b143e4840ae73d4582a8914a43':
    print("Dummy Test Virus")
else:
    print("No Virus")