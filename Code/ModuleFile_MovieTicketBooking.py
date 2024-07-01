#Module file of name MovieMenuB 
def ShowMenu():
    print('''---Movies Available---
1. Mr & Ms Ramachari - Kannada - 2D
2. K.G.F             - Kannada - 2D
3. Bahubali          - Telugu  - 2D
4. RRR               - Telugu  - 3D
5. Bharath ane nenu  - Telugu  - 2D''')
def Menu():
    while 1:
        print('''Select the movie
1. Mr & Ms Ramachari - Kannada - 2D
2. K.G.F             - Kannada - 2D
3. Bahubali          - Telugu  - 2D
4. RRR               - Telugu  - 3D
5. Bharath ane nenu  - Telugu  - 2D''')
        m=int(input("= "))
        if m<=5 and m>=1:
            break
        else:
            print('Invalid Choice')
    return m
def Select(m):
    l=['Kannada','Telugu']
    if m==1:
        mov='Mr & Ms Ramachari'
        while 1:
            print('Select the Theater')
            print('''1.Radhika Theatre
2.Nataraj Theatre''')
            t=int(input("= "))
            if t==1:
                theatre='Radhika Theatre'
                break
            elif t==2:
                theatre='Nataraj Theatre'
                break
            else:
                print('Invalid choice\n')
        lan=l[0]
        dim='2D'
    elif m==2:
        mov='K.G.F '
        while 1:
            print('Select the Theater')
            print('''1.RR Theatre
2.Uma Theatre''')
            t=int(input("= "))
            if t==1:
                theatre='RR Theatre'
                break
            elif t==2:
                theatre='Uma Theatre'
                break
            else:
                print('Invalid choice\n')
        lan=l[0]
        dim='2D'
    elif m==3:
        mov='Bahubali'
        while 1:
            print('Select the Theater')
            print('''1.SRR Theatre
2.Balaji Theatre ''')
            t=int(input("= "))
            if t==1:
                theatre='SRR Theatre '
                break
            elif t==2:
                theatre='Balaji Theatre'
                break
            else:
                print('Invalid choice\n')
        lan=l[1]
        dim='2D'
    elif m==4:
        mov='RRR'
        while 1:
            print('Select the Theater')
            print('''1.Shiva Theatre
2.Ramakrishna Theatre''')
            t=int(input("= "))
            if t==1:
                theatre='Shiva Theatre'
                break
            elif t==2:
                theatre='Ramakrishna Theatre'
                break
            else:
                print('Invalid choice\n')
        lan=l[1]
        dim='3D'
    elif m==5:
        mov='Bharath ane nenu'
        while 1:
            print('Select the Theater')
            print('''1.Vibha Theatre
2.SRS Theatre''')
            t=int(input("= "))
            if t==1:
                theatre='Vibha Theatre'
                break
            elif t==2:
                theatre='SRS Theatre'
                break
            else:
                print('Invalid choice\n')
        lan=l[1]
        dim='2D'
    return mov,theatre,lan,dim
def Time():
    while 1:
        print('''Select Time
        1. 11:00 AM
        2. 02:00 PM
        3. 05:00 PM
        4. 08:15 PM''')
        ti=int(input("= "))
        if ti==1:
            time='11:00 AM'
            break
        elif ti==2:
            time='02:00 PM'
            break
        elif ti==3:
            time='05:00 PM'
            break
        elif ti==4:
            time='08:15 PM'
            break
        else:
            print('Invalid Choice')
    return time
def Type():
    while 1:
        print('''Select the type of seat you want to Book
        1.Balcony = 150rs
        2.Second class = 100rs''')
        ty=int(input("= "))
        if ty>2 or ty<0:
            print('Invalid Choice')
        else:
            break
    return ty
def Cost(seats,ty):
    if ty==1:
        tcost=seats*150
    elif ty==2:
            tcost=seats*100
    gst=(tcost*18)/100
    return tcost,gst
