x = int(input("введіть номер місяця :"))

def season(x):
 if 1> x > 12:
    print('eror')
 elif x == 12 or x == 1 or x == 2:
    print('this is winter! brr...')
 elif x == 3 or x == 4 or x == 5:
    print('this is spring :)') 
 elif x == 6 or x==7 or x == 8:
    print('this is summer!!!')
 else: 
    x == 9 or x == 10 or x == 11
    print('this is autumn')

season(x)
