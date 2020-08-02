#try...except...finally
try:
    print('trying...')
    r = 10/0#此处会产生错误进入except语句
    print('result', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
try:
    print('trying...')
    r = 10/2#若没有错误，则不会执行except内容，但是finally一定执行
    print('result', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
try:
    print('trying...')
    r = 10/int('2')#若没有错误，则不会执行except内容，但是finally一定执行
    print('result', r)
except ZeroDivisionError as e:
    print('except:', e)
except ValueError as e:
    print('except:', e)
else:
    print('ok')
finally:
    print('finally...')
    
