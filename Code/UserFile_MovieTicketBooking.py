#-------------------------Movie Ticket Booking-------------------------
import ModuleFile_MovieTicketBooking as MovieMenuB
print("----------------------WELCOME TO BOOK MY SHOW----------------------")
while 1:
    print('''---Home---
    1.Movie List
    2.Book my show
    3.Exit''')
    try:
        choice=int(input('Enter your choice = '))
    except:
        print('Invalid Choice\n')
    if choice==1:
        MovieMenuB.ShowMenu()
    elif choice==2:
        m=MovieMenuB.Menu()
        mov,theatre,lan,dim=MovieMenuB.Select(m)
        d=input('Enter date (dd-mm-yyyy) = ')
        time=MovieMenuB.Time()
        ty=MovieMenuB.Type()
        seats=int(input('Enter total number of seats = '))
        tcost,gst=MovieMenuB.Cost(seats,ty)
        Ticket=('''----------------------------------------------------------------
                                   My Show                              
----------------------------------------------------------------
{}                                                      {}
{}  -  {}                                          M-Ticket
{} | {}
{}
----------------------------------------------------------------
Tickets price                                        {}rs 
GST                                                  {}rs
----------------------------------------------------------------
Total Cost                                           {}rs
----------------------------------------------------------------
'''.format(mov,seats,lan,dim,d,time,theatre,tcost,gst,(tcost+gst)))
        print(Ticket)
        c=input('Confirm Ticket (y/n) = ')
        if c=='y':
            print('Your Ticket Booked')
            f=open('Ticket.txt','w')
            f.write(Ticket)
            f.close
        else :
            print('Your Ticket Cancelled')
    elif choice==3:
        print('\nThank You......:)')
        break
    else:
        print('Invalid Choice\n')
