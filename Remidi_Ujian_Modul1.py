# https://github.com/ridhoaryo/Ujian_Modul1_Remedi_JCDS_JKT_BDG/blob/main/README.md
print('Ujian Modul1 Remedi JCDS JKT BDG')

print('no. 1')
def find_short(s):
    return min(map(len,s.split()))

print("find_short(Many people get up early in the morning)")
print('The shortest word has',find_short('Many people get up early in the morning'),'char(s)')
print("find_short(Every office would getting newest monitor)")
print('The shortest word has',find_short('Every office would getting newest monitor'),'char(s)')
print("find_short(Create new file after this morning)")
print('The shortest word has',find_short('Create new file after this morning'),'char(s)')

print('======================================')
print('no. 2')
def persistence(num):
    res = 0
    temp = 1
    if (num >= 0):
        while (num > 9):
            if temp == 1:
                temp = num % 10
            num -= num % 10
            num /= 10
            temp *= (num % 10)
            if (num <= 9) :
                num = temp
                temp = 1
                res += 1
        print(res)
    else :
        print("Please input positive number only")
     
print('persistence(39)')     
persistence(39)
print('persistence(999)')  
persistence(999)
print('persistence(4)')  
persistence(4)
print('persistence(-12)')  
persistence(-12)


