import csv, webbrowser, typing

#Welcome
from typing import List, Union, Any

print('------------Welcome to the Builder!------------')

#functions
def search(url):
    webbrowser.open_new(url)

def start(app):
    os.system(app)

#executes each callsign in a polysign
def execute(callsign):
    if callsign[1]=='a':
        start(callsign[0])
    elif callsign[1]=='w':
        search(callsign[2])
    else:
        pass

#Select Designation Family
print("\nEnter 1 for a new callsign  OR  Enter 2 for a new polysign")
fam = input('Selection: ') # type: object

####################################################################################

#Callsign Family Builder
if fam == 1:
    callsign_type=input("\nEnter 'a' for an application  OR  Enter 'w' for a website\nMake sure include the single quotes. Selection: ") #Callsign Type
    cname=input("\nName of Callsign: ")
    urla=1
    url=[]
    if callsign_type == 'a':
        urla=0
    elif callsign_type == 'w':
        url.append(input('URL: '))
    if urla==0:
        call_list_a = [cname, str(callsign_type)]
    else:
        call_list_w = [cname, str(callsign_type), url[0]]
    with open('callsign.csv', 'a') as call:
        writer=csv.writer(call)
        if urla == 0:
            writer.writerow(call_list_a)
        else:
            writer.writerow(call_list_w)
        call.close()
#Polysign Family Builder
elif fam==2:
    p_name=str(input('Name of Polysign: '))
    stop = 0
    polysign = []
    with open('callsign.csv', 'r') as call:
        reader=csv.reader(call)
        print('Previously Designated Callsigns:\n')
        for i in reader:
            if i[0] != 'Callsign':
                print(i[0])
        print('\nEnter the callsigns that make up this polysign one at a time and hit enter each time, with single quotations.')
        print("When you are finished, enter 'stop', with single quotations")
        while stop==0:
            addendum=input('Callsign to enter: ')
            if addendum == 'stop':
                stop=1
            else:
                polysign.append(addendum)
        call.close()
    with open('polysign.csv', 'a') as pol:
        writer = csv.writer(pol)
        writer.writerow(polysign)
        pol.close()
