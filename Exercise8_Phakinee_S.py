while True:
    id = input('Enter Your ID : ')
    pw = input('Enter Your Password : ')
    print('Correct!')
    if id == '1' and pw == '2':
        print('-------Welcome to Mugiwara store-------')
        print('1.Compass                  20 beri')
        print('2.Fish from all brue    3,000 beri')
        print('3.ONE PIECE       999,999,999 beri')
        print('4.Cruise            8,000,999 beri')
        print('5.Cotton Candy            100 beri')
        print('6.Orange                   99 beri')
        print('7.Poneglyph           345,657 beri')
        print('8.Katana                9,000 beri')
        prod = {1:20,2:3000,3:999999999,4:8000999,5:100,6:99,7:345657,8:9000}
        summ = 0
        sel = -1
        while sel != 0:
            sel = int(input("Which one? (enter 0 to stop): "))
            if sel == 0 :
                break
            num = int(input("How many? : "))
            summ += prod[sel]*num
        print('Total : ',summ)
        break
    else:
        print('Incorrect password. Please try again.')
