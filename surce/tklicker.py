import tkinter as tk
import threading
import time
import json

# Load from save.json
with open('save.json', 'r') as save_file:
    save = json.load(save_file)

# from save.json
Points = save['Points']
clicker_upgrade_lv = save['clicker_upgrade_lv']
autoclicker1_lv = save['autoclicker1_lv']
autoclicker2_lv = save['autoclicker2_lv']
XP = save['XP']
Level = save['Level']
next_level = save['next_level']

# other
Points_s = 0

root = tk.Tk()

root.title('tklicker')
root.iconbitmap(r'Images\tklicker icon.ico')

frame = tk.Frame(root, bg='white', padx=50, pady=80)
frame.pack(padx=0, pady=0)

level = tk.Label(frame, text=('Level ' + str(Level)), bg='white', font=('courier', 25), pady=-100)
level.grid(row=0, column=1)

xp = tk.Label(frame, text=(str(XP) + ' XP/' + str(next_level) + ' XP'), bg='white')
xp.grid(row=1, column=1)

label = tk.Label(frame, text=Points, bg='white', font=('courier', 20), pady=15)
label.grid(row=2, column=1)

def order():
    global save
    global clicker_upgrade_lv
    global autoclicker1_lv
    global autoclicker2_lv
    global XP
    global Level
    global next_level

    save = {
        "Points": Points,
        "clicker_upgrade_lv": clicker_upgrade_lv,
        "autoclicker1_lv": autoclicker1_lv,
        "autoclicker2_lv": autoclicker2_lv,
        "XP": XP,
        "Level": Level,
        "next_level": next_level
    }

    if Points >= 1000000:
        # points_m = str(Points/1000000)
        # label['text'] = (str(points_m[0:3]) + 'M' + ' Points')
        label['text'] = (str(Points/1000000) + 'M' + ' Points')
    elif Points >= 1000:
        label['text']=(str(Points/1000) + 'K' + ' Points')
    else:
        label['text'] = (str(Points) + ' Points')

    if XP >= 1000000:
        xp['text'] = (str(XP/1000000) + 'M XP' + '/' + str(next_level/1000000) + 'M')
    elif XP >= 1000:
        xp['text'] = (str(XP/1000) + 'K XP' + '/' + str(next_level/1000) + 'K')
    else:
        xp['text'] = (str(XP) + ' XP/' + str(next_level) + ' XP')

    # write to save.json
    with open('save.json', 'w') as save_file:
        save = json.dump(save, save_file)

def autopoints():
    global Points
    global autoclicker1_lv
    global XP
    global Level
    global next_level

    while True:
        Points_s1 = Points
        Points += (10*autoclicker1_lv)
        Points += (250*autoclicker2_lv)
        time.sleep(1)
        Points - Points_s1
        if Points - Points_s1 > 0:
            XP += (Points - Points_s1)
        if XP >= next_level:
            Level += 1
            next_level = round(next_level**1.05)
        level['text'] = ('Level ' + str(Level))
        pps['text'] = (str(Points - Points_s1) + 'pp/s')
        order()

t1 = threading.Thread(target=autopoints)
t1.start()

def click():
    global Points
    global clicker_upgrade_lv
    if clicker_upgrade_lv > 2:
        Points += (1 * (clicker_upgrade_lv*2))
    elif clicker_upgrade_lv == 2:
        Points += (1 * clicker_upgrade_lv)
    else:
        Points += 1
    order()

pps = tk.Label(frame, text=Points_s, bg='white', pady=10)
pps.grid(row=3, column=1)

button_1 = tk.Button(frame, text='click me!', height=3, width=20, bg='grey', fg='black', command=click)
button_1.grid(row=4, column=1)

upgrade_frame = tk.Frame(frame, bg='white', padx=20, pady=0)
upgrade_frame.grid(row=0, column=0)

def Upgrade_Clicker():
    global clicker_upgrade_lv
    global Points
    if Points >= (100*(clicker_upgrade_lv*2)):
        Points -= (100*(clicker_upgrade_lv*2))
        clicker_upgrade_lv += 1
        upgrade_clicker_num['text'] = (str(clicker_upgrade_lv-1))
        order()
        upgrade_clicker['text'] = ('Clickerupgrade' + '\ncost: ' + str(100*(clicker_upgrade_lv*2)))

upgrade_clicker_num = tk.Label(upgrade_frame, text=str(clicker_upgrade_lv-1), bg='white')
upgrade_clicker_num.grid(row=0, column=0)

upgrade_clicker = tk.Button(upgrade_frame, text=('Clickerupgrade' + '\ncost: ' + str(100*(clicker_upgrade_lv*2))), command=Upgrade_Clicker, height=2)
upgrade_clicker.grid(row=1, column=0)

def autoclicker1():
    global Points
    global autoclicker1_lv
    if Points >= (500*(autoclicker1_lv*2)) and autoclicker1_lv > 0:
        if autoclicker1_lv < 1:
            Points -= 500
        else:
            Points -= (500*(autoclicker1_lv*2))
            autoclicker1_lv += 1
            autoclicker_1_num['text'] = (str(autoclicker1_lv))
            order()
            autoclicker_1['text'] = ('Autoclicker' + '\ncost: ' + str(500 * (autoclicker1_lv * 2)))
    elif Points >= 500 and autoclicker1_lv == 0:
        Points -= 500
        autoclicker1_lv += 1
        autoclicker_1_num['text'] = (str(autoclicker1_lv))
        order()
        autoclicker_1['text'] = ('Autoclicker' + '\ncost: ' + str(500*(autoclicker1_lv*2)))

autoclicker_1_num = tk.Label(upgrade_frame, text=str(autoclicker1_lv), bg='white')
autoclicker_1_num.grid(row=2, column=0)

autoclicker_1 = tk.Button(upgrade_frame, text=('Autoclicker' + '\ncost: 500'), command=autoclicker1, height=2)
autoclicker_1.grid(row=3, column=0)

def autoclicker2():
    global Points
    global autoclicker2_lv
    if Points >= (10000*(autoclicker2_lv*2)) and autoclicker2_lv > 0:
        if autoclicker2_lv < 1:
            Points -= 10000
        else:
            Points -= (10000*(autoclicker2_lv*2))
            autoclicker2_lv += 1
            autoclicker_2_num['text'] = (str(autoclicker2_lv))
            order()
            autoclicker_2['text'] = ('Autoclicker' + '\ncost: ' + str(10000*(autoclicker2_lv*2)))
    elif Points >= 10000 and autoclicker2_lv == 0:
        Points -= 10000
        autoclicker2_lv += 1
        autoclicker_2_num['text'] = (str(autoclicker2_lv))
        order()
        autoclicker_2['text'] = ('Super Autoclicker' + '\ncost: ' + str(10000*(autoclicker2_lv * 2)))

autoclicker_2_num = tk.Label(upgrade_frame, text=str(autoclicker2_lv), bg='white')
autoclicker_2_num.grid(row=4, column=0)

autoclicker_2 = tk.Button(upgrade_frame, text=('Super Autoclicker' + '\ncost: 10000'), command=autoclicker2, height=2)
autoclicker_2.grid(row=5, column=0)

root.mainloop()