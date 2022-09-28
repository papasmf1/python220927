# demoFile.py
for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---서식지정---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("---서식지정---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(3))

#서식시정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000000))

#파일 쓰기(raw string notation) 유니코드 지정
f = open(r"c:\work\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일 읽기(c:\work, 리눅스, 맥 /users/kim/desktop)
f = open("c:/work/demo.txt", "rt", encoding="utf-8")
#처음부터 끝까지 하나의 문자열 
result = f.read()
print(result)
#어디쯤 읽고 있어?
print( f.tell() )
#리셋
f.seek(0)
lst = f.readlines()
print(lst)
f.close()


