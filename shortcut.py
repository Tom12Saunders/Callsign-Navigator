import csv, webbrowser, os, typing

# Functions
def search_up(url):
    webbrowser.open_new(str(url))

def app_launch(app):
    os.system(str(app))


#executes each callsign in a polysign
def execute(x, t, url):
    if t == 'a':
        app_launch(x)
    elif t == 'w':
        search_up(url)
    else:
        p=1


def refind_callsigns(polysign):
    callsign_list = []
    counter = 1
    with open('callsign.csv', 'r') as call:
        reader = csv.reader(call)
        reader_list = []
        type_list = []
        url_list = []
        counter=1
        for i in reader:
            reader_list.append(i[0])
            type_list.append(i[1])
            url_list.append(i[2])
        #print('reader_list', reader_list)
        #print('type_list: ', type_list)
        #print('url_list', url_list)
        reader_list.pop(0)
        type_list.pop(0)
        url_list.pop(0)
        #print(reader_list)
        #print(type_list)
        #print(url_list)
        for i in range(len(reader_list)):
            #print(reader_list[i], type_list[i], url_list[i])
            execute(reader_list[i], type_list[i], url_list[i])
        #execute(callsign_list)
    #for i in callsign_list:
        #execute(i)

# Loop
with open('polysign.csv', 'r') as pol:
    reader = csv.reader(pol)
    polysigns=[]
    for i in reader:
        if i[0] != 'Name':
            print(i[0])
            polysigns.append(i[0])
    polysign = input('\nSelect Polysign: ')
    refind_callsigns(polysign)