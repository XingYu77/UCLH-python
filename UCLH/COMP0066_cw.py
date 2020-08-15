import numpy as np
import sys
'''
patient_list_title=[[0,'name','username','password','email','account_status','unconfirmed_appoinment','confirmed_appoinment','perscripition']]
a = np.load('patient.npy',allow_pickle=True)
if(a!=None):
    b = np.array(patient_list_title)
    np.save('patient.npy', b)
'''


def createacc():
    old_np_list = np.load('patient.npy',allow_pickle=True)
    old_list = old_np_list.tolist()
    #print(old_list)
    patient_num = len(old_list)
    new_patient = []
    print('To create a new patient account, please complete the followings:')
    uname = input('Please enter your username:')
    pw = input('Please enter your password:')
    name = input('Please enter your name:')
    email = input('Please enter your email:')
    while('@' not in email):
        print('Please enter a valid email')
        email = input('Please enter your email:')
    new_patient.append([patient_num, name, uname, pw, email, 0, [], [], []])
    new_patient = new_patient[0]
    old_list.append(new_patient)
    a = np.array(old_list)
    np.save('patient.npy', a)
    #b= np.load('patient.npy',allow_pickle=True)
    #b=b.tolist()
    #print(b)
    print('You have created a new account, please wait for activation')
    print(' ')

def addgp():
    old_np_list = np.load('gp.npy', allow_pickle=True)
    old_list = old_np_list.tolist()
    # print(old_list)
    gp_num = len(old_list)
    new_gp = []
    print('To create a new GP account, please complete the followings:')
    uname = input('Please enter username:')
    pw = input('Please enter password:')
    name = input('Please enter GP name:')
    new_gp.append([gp_num, name, uname, pw, 1, [], [], []])
    new_gp = new_gp[0]
    old_list.append(new_gp)
    a = np.array(old_list)
    np.save('gp.npy', a)
    b= np.load('gp.npy',allow_pickle=True)
    b=b.tolist()
    #print(b)
    print('You have created a new GP account')

def deactivategp():
    print('Which GP do you want to deactivate? (account status = 1)')
    a = np.load('gp.npy', allow_pickle=True)
    a = a.tolist()
    # print(a)
    num = 1
    for row in a:
        if (int(row[0]) > 0):
            print('id:', num, '', 'name:', row[1], '', 'username:', row[2],'', 'account status:', row[4])
            num = num + 1
    index = input()
    while ((not (index.isdigit())) or (int(index) > (num - 1))):
        print('Please enter a valid number')
        index = input()
    a[int(index)][4] = 0
    a = np.array(a)
    np.save('gp.npy', a)
    print('account deactivated')
    print(' ')

def reactivategp():
    print('Which GP do you want to reactivate? (account status = 0)')
    a = np.load('gp.npy', allow_pickle=True)
    a = a.tolist()
    # print(a)
    num = 1
    for row in a:
        if (int(row[0]) > 0):
            print('id:', num, '', 'name:', row[1], '', 'username:', row[2],'', 'account status:', row[4])
            num = num + 1
    index = input()
    while ((not (index.isdigit())) or (int(index) > (num - 1))):
        print('Please enter a valid number')
        index = input()
    a[int(index)][4] = 1
    a = np.array(a)
    np.save('gp.npy', a)
    print('account reactivated')
    print(' ')

def deletegp():
    print('Which GP do you want to delete?')
    a = np.load('gp.npy', allow_pickle=True)
    a = a.tolist()
    # print(a)
    num = 1
    for row in a:
        if (int(row[0]) > 0):
            print('id:', num, '', 'name:', row[1], '', 'username:', row[2], '', 'account_status:', row[4])
            num = num +1
    index = input()
    while ((not (index.isdigit())) or (int(index) > (num - 1))):
        print('Please enter a valid number')
        index = input()
    del a[int(index)]
    a = np.array(a)
    np.save('gp.npy', a)
    print('account deleted')

def deletepat():
    print('Which patient do you want to delete?')
    a = np.load('patient.npy', allow_pickle=True)
    a = a.tolist()
    # print(a)
    num = 1
    for row in a:
        if (int(row[0]) > 0):
            print('id:', num, '', 'name:', row[1], '', 'username:', row[2])
            num = num +1
    index = input()
    while ((not (index.isdigit())) or (int(index) > (num - 1))):
        print('Please enter a valid number')
        index = input()
    del a[int(index)]
    a = np.array(a)
    np.save('patient.npy', a)
    print('account deleted')

def confirm_regist():

    a = np.load('patient.npy', allow_pickle=True)
    a = a.tolist()
    # print(a)
    num = 1
    for row in a:
        if (int(row[0]) > 0 and int(row[5]) == 0):
            print(num, ' ', 'name:', row[1], '', 'username:', row[2], '', 'email:', row[4], '',
                  'account_status:', row[5])
            num = num + 1
    if(num ==1):
        print('You have no registration to approve')
        print(' ')
    else:
        print('Which registration do you want to approve?')
        count = 0
        index = input()
        while((not(index.isdigit())) or (int(index)>(num-1)) ):
            print('Please enter a valid number')
            index = input()
        index = int(index)
        for row in a:
            if (row[5] == 0):
                index = index - 1
            if(index >0):
                count = count + 1

        #print(count)

        a[int(count)][5] = 1
        a = np.array(a)
        np.save('patient.npy', a)
        print('registration approved')
        print(' ')

def update_info():
    a = np.load('patient.npy',allow_pickle=True)
    if (len(a) == 1):
        print('There are no patient accounts now')
    else:
    #print(a)
        print('Which patient do you want to update?')
        num = 1
        for row in a:
            if (int(row[0]) > 0):
                print(num, '', 'name:', row[1], '', 'username:', row[2], '', 'email:', row[4], '','account_status:', row[5])
                num = num + 1
        index = input()
        while ((not (index.isdigit())) or (int(index) > (num - 1))):
            print('Please enter a vaild number')
            index = input()
        print('Which information do you want to update?')
        print('1. name')
        print('2. email')
        choose = input()
        while (choose not in ['1','2']):
            print('Please enter a vaild number')
            choose = input()
        if (choose == '1'):
            print('Please enter a new name')
            new = input()
            acc_list[int(index)][1] = new
        if (choose == '2'):
            print('Please enter a new email')
            new = input()
            while('@' not in new):
                print('Please enter a vaild email')
                new = input
            acc_list[int(index)][4] = new
        a = np.array(acc_list)
        np.save('patient.npy', a)
        print('Information updated')
        print(' ')

def patient_update():
    print('Which information do you want to update?')
    print('1. name')
    print('2. username')
    print('3. password')
    print('4. email')
    index = input()
    while (index not in ['1','2','3','4']):
        print('Please enter a vaild number')
        index = input()
    if (index == '1'):
        print('Please enter a new name')
        new = input()
        acc_list[i][1] = new
    if (index == '2'):
        print('Please enter a new username')
        new = input()
        acc_list[i][2] = new
    if (index == '3'):
        print('Please enter a new password')
        new = input()
        acc_list[i][3] = new
    if (index == '4'):
        print('Please enter a new email')
        new = input()
        while ('@' not in new):
            print('Please enter a vaild email')
            new = input
        acc_list[i][4] = new
    a = np.array(acc_list)
    np.save('patient.npy', a)
    print('Information updated')
    print(' ')

def view_info():
    print('Your profile information are as followings:')
    print('Name:'+acc_list[i][1]+' | '+ 'Username:'+acc_list[i][2]+' | '+'Email:'+acc_list[i][4])
    print(' ')


def add_availability():
    weekdays = [("1.", "Monday"),
                ("2.", "Tuesday"),
                ("3.", "Wednesday"),
                ("4.", "Thursday"),
                ("5.", "Friday"),
                ("6.", "Saturday"),
                ("7.", "Sunday")]

    times = [("1.", "9:00~10:00am"),
             ("2.", "10:00~11:00am"),
             ("3.", "11:00~12:00am"),
             ("4.", "12:00~13:00pm"),
             ("5.", "13:00~14:00pm"),
             ("6.", "14:00~15:00pm"),
             ("7.", "15:00~16:00pm"),
             ("8.", "16:00~17:00pm"),]
    print('Please add your available day')
    for row in weekdays:
        print(row)
    day = input()
    while (day not in ['1','2','3','4','5','6','7']):
        print('Please enter a vaild number')
        day = input()
    day = weekdays[int(day) - 1]
    print('Please add your available time')
    for row in times:
        print(row)
    time = input()
    while (time not in ['1','2','3','4','5','6','7','8']):
        print('Please enter a vaild number')
        time = input()
    time = times[int(time) - 1]
    gp_list[i][5].append(day+time)
    a = np.array(gp_list)
    np.save('gp.npy', a)
    print('new availability added')
    print('Your availability time:')
    num = 1
    for row in gp_list[i][5]:
        print( str(num) +' '+ row[1] + ' ' + row[3])
        num = num+1
    print(' ')

def delete_availability():
    print('Which time do you want to delete?')
    num = 1
    for row in gp_list[i][5]:
        print(str(num) + ' ' + row[1] + ' ' + row[3])
        num = num + 1
    index = input()
    while ((not (index.isdigit())) or (int(index) > (num - 1))):
        print('Please enter a valid number')
        index = input()
    del gp_list[i][5][int(index)-1]
    a = np.array(gp_list)
    np.save('gp.npy', a)
    print('One availability deleteed')
    print('Your availability time:')
    num = 1
    for row in gp_list[i][5]:
        print(str(num) + ' ' + row[1] + ' ' + row[3])
        num = num + 1
    print(' ')

def view_availability():
    if(gp_list[i][5] ==[]):
        print('You have not add any availability')
        print(' ')
    else:
        print('Your availability are as followings:')
        num = 1
        for row in gp_list[i][5]:
            print(str(num) + ' ' + row[1] + ' ' + row[3])
            num = num + 1
        print(' ')

def book_appoint():
    print('Available GP and time are as followings,which one do you want to book?')
    num = 1
    global avail_list
    avail_list = []
    booked_list = []
    for row in gp_list:
        if (int(row[0]) > 0 and row[5] != []):
            for list in row[5]:
                new = str(row[1]) + ' ' + str(list[1]) + ' ' + str(list[3])
                avail_list.append(new)
                print(str(num) + ' ' + str(row[1]) + ' ' + str(list[1]) + ' ' + str(list[3]))
                num = num + 1
    index = input()
    while ((not (index.isdigit())) or (int(index) > (num - 1))):
        print('Please enter a valid number')
        index = input()
    booked_list.append('patient: ' + acc_list[i][1] + ', ' + 'doctor: '+ avail_list[int(index) - 1])
    #print(booked_list)
    acc_list[i][6].append(booked_list)
    #print(acc_list[i][6])
    a = np.array(acc_list)
    np.save('patient.npy', a)
    for gp in gp_list:
        if(gp[1] in booked_list[0]):
            gp[6].append(booked_list)
    a = np.array(gp_list)
    np.save('gp.npy', a)
    print('Appointment booked, please wait for approve')
    print(' ')

def cancel_appoint():
    print('Please choose a list')
    print('1. unconfirmed appoinments')
    print('2. confirmed appoinments')
    index = input()
    while(index not in['1','2']):
        print('Please enter a valid number')
        print(' ')
        index = input()
    if (int(index) ==1):
        if (acc_list[i][6] == []):
              print('You have no unconfirmed appointments')
              print(' ')

        else:
            num = 1
            for row in acc_list[i][6]:
                print(num,' ',row)
                num = num + 1
            index = input()
            while ((not (index.isdigit())) or (int(index) > (num - 1))):
                print('Please enter a vaild number')
                index = input()
            cancel = acc_list[i][6][int(index)-1]
            del acc_list[i][6][int(index)-1]
            a = np.array(acc_list)
            np.save('patient.npy', a)
            for gp in gp_list:
                for book in gp[6]:
                    if (book == cancel):
                        gp[6].remove(book)
            a = np.array(gp_list)
            np.save('gp.npy', a)
            print('Appointment canceled')

    if (int(index) == 2):
        if (acc_list[i][7] == []):
              print('You have no confirmed appoinments')
              print(' ')
        else:
            num = 1
            for row in acc_list[i][7]:
                print(num,' ',row)
                num = num + 1
            index = input()
            while ((not (index.isdigit())) or (int(index) > (num - 1))):
                print('Please enter a vaild number')
                index = input()
            cancel = acc_list[i][7][int(index) - 1]
            del acc_list[i][7][int(index)-1]
            a = np.array(acc_list)
            np.save('patient.npy', a)
            for gp in gp_list:
                for book in gp[7]:
                    if (book == cancel):
                        gp[7].remove(book)
            a = np.array(gp_list)
            np.save('gp.npy', a)
            print('Appointment canceled')

def view_appoint():
    print('unconfirmed appoinments:')
    if (acc_list[i][6] ==[]):
        print('You have no unconfirmed appoinments')
        print(' ')
    else:
        for row in acc_list[i][6]:
            print(row[0])
        print(' ')
    print('confirmed appoinments:')
    if (acc_list[i][7] == []):
        print('You have no confirmed appoinments')
        print(' ')
    else:
        for row in acc_list[i][7]:
            print(row[0])
        print(' ')

def view_books():
    print('unapproved bookings:')
    if (gp_list[i][6] == []):
        print('You have no unapproved bookings')
        print(' ')
    else:
        for row in gp_list[i][6]:
            print(row[0])
        print(' ')
    print('approved bookings:')
    if (gp_list[i][7] == []):
        print('You have no approved bookings')
        print(' ')
    else:
        for row in gp_list[i][7]:
            print(row[0])
        print(' ')

def confirm_books():
    if (gp_list[i][6] == []):
        print('You have no bookings to approve')
        print(' ')
    else:
        print('Which booking do you want to approve?')
        num = 1
        for row in gp_list[i][6]:
            print(num,'',row[0])
            num =  num+1
        print(' ')
        index = input()
        while ((not (index.isdigit())) or (int(index) > (num-1))):
            print('Please enter a vaild number')
            index = input()
        approve = gp_list[i][6][int(index)-1]
        gp_list[i][7].append(gp_list[i][6][int(index)-1])
        del gp_list[i][6][int(index)-1]
        a = np.array(gp_list)
        np.save('gp.npy', a)
        for acc in acc_list:
            for book in acc[6]:
                if (book == approve):
                    acc[6].remove(approve)
                    acc[7].append(approve)
        a = np.array(acc_list)
        np.save('patient.npy', a)
        print('Booking approved')
        print(' ')

def add_prescription():
    if (gp_list[i][7] == []):
        print('You have no finished appointments')
        print(' ')

    else:
        print('Please choose a record to add prescription')
        num = 1
        for row in gp_list[i][7]:
            print(num,' ',row[0])
            num = num + 1
        index = input()
        while ((not (index.isdigit())) or (int(index) > (num - 1))):
            print('Please enter a valid number')
            index = input()
        print()
        print('Please add prescription: ')
        presc = input()
        for row in acc_list:
            if(row[1] in gp_list[i][7][int(index)-1][0]):
                row[8].append('Appointment:'+gp_list[i][7][int(index)-1][0]+' || ' + 'Prescription: '+presc)
        b = np.array(acc_list)
        np.save('patient.npy', b)
        print('Prescripption added')
        print(' ')

def view_prescription():
    if(acc_list[i][8]==[]):
        print('You have no prescription now')
    else:
        print('Your prescription are as followings:')
        num = 1
        for row in acc_list[i][8]:
            print(num,row)
            num = num+1
    print(' ')

def admin_home():
    print('You have logged in as administrator')
    print('1. Add new GP')
    print('2. Deactivate GP')
    print('3. Delete GP')
    print('4. Delete patient account')
    print('5. Confirm patients registration')
    print('6. Reactivate GP')
    print('7. Update patient information')
    print('8. log out')
    index = input()
    while (index not in ['1', '2', '3', '4', '5', '6','7','8']):
        print('Please enter a valid number')
        index = input()

    if (int(index) == 1):
        addgp()
        admin_home()
    if (int(index) == 2):
        deactivategp()
        admin_home()
    if (int(index) == 3):
        deletegp()
        admin_home()
    if (int(index) == 4):
        deletepat()
        admin_home()
    if (int(index) == 5):
        confirm_regist()
        admin_home()
    if (int(index) == 6):
        reactivategp()
        admin_home()
    if (int(index) == 7):
        update_info()
        admin_home()
    if (int(index) == 8):
        print('You are logged out')
        admin_page()

def gp_home():
    print('You have logged in as GP')
    print('1. Add new availability')
    print('2. Delete  availability')
    print('3. View  availability')
    print('4. View  bookings')
    print('5. Approve  bookings')
    print('6. Add prescription')
    print('7. Log out')
    index = input()
    while (index not in ['1', '2', '3', '4', '5', '6','7']):
        print('Please enter a valid number')
        index = input()

    if (int(index) == 1):
        add_availability()
        gp_home()
    if (int(index) == 2):
        delete_availability()
        gp_home()
    if (int(index) == 3):
        view_availability()
        gp_home()
    if (int(index) == 4):
        view_books()
        gp_home()
    if (int(index) == 5):
        confirm_books()
        gp_home()
    if (int(index) == 6):
        add_prescription()
        gp_home()
    if (int(index) == 7):
        print('You are logged out')
        admin_page()

def patient_home():
    print('You have logged in as patient')
    print('1. Book appointment')
    print('2. Cancel appointment')
    print('3. View  appointments')
    print('4. View  prescriptions')
    print('5. Update information')
    print('6. View my information')
    print('7. Log out')
    index = input()
    while (index not in ['1', '2', '3', '4', '5', '6','7']):
        print('Please enter a valid number')
        index = input()

    if (int(index) == 1):
        book_appoint()
        patient_home()
    if (int(index) == 2):
        cancel_appoint()
        patient_home()
    if (int(index) == 3):
        view_appoint()
        patient_home()
    if (int(index) == 4):
        view_prescription()
        patient_home()
    if (int(index) == 5):
        patient_update()
        patient_home()
    if (int(index) == 6):
        view_info()
        patient_home()
    if (int(index) == 7):
        print('You are logged out')
        admin_page()


def accept_login():
    users_admin = {"admin": "admin"}
    global acc_list
    acc_list = np.load('patient.npy', allow_pickle=True)
    acc_list = acc_list.tolist()
    #print(acc_list)
    acc_num = len(acc_list)
    global gp_list
    gp_list = np.load('gp.npy', allow_pickle=True)
    gp_list = gp_list.tolist()
    # print(acc_list)
    gp_num = len(gp_list)

    username = input('Please enter username:')
    password = input('Please enter password:')
    login = 'invalid'
    if (username in users_admin.keys() and users_admin[username] == password):
        login = 'valid'
        admin_home()

    global i
    for i in range(1, gp_num):
        if (gp_list[i][2] == username and gp_list[i][3] == password and gp_list[i][4] == 1):
            login = 'valid'
            gp_home()

        if (gp_list[i][2] == username and gp_list[i][3] == password and gp_list[i][4] == 0):
            print('This account is not activated, please contact administrator ')
            print('')
            login = 'valid'
            admin_page()
    for i in range (1,acc_num):
         if (acc_list[i][2]==username and acc_list[i][3]==password and acc_list[i][5] == 1):
            login = 'valid'
            patient_home()
         if (acc_list[i][2]==username and acc_list[i][3]==password and acc_list[i][5] == 0):
            print('Your registration are not confirmed,please contact administrator')
            print(' ')
            login = 'valid'
            admin_page()
    if login == 'invalid':
        print('Please enter valid username and password')
        print(' ')
        admin_page()


def admin_page():
    print('Welcome to UCLH!')
    index = input('0: log in:\n1: create new patient account\n2: exit app\n')

    if (index !='0' and index!= '1'and index!= '2'):
        print('Please enter a vaild number')
        print(' ')
        admin_page()
    if (index == '0'):
        accept_login()
    if (index == '1'):
        createacc()
        admin_page()
    if (index == '2'):
        sys.exit()


admin_page()


