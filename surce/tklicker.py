import tkinter as tk
import threading
import json
import time
import random

# Load from save.json
with open('save.json', 'r') as save_file:
    save = json.load(save_file)

# from save.json
Points = save['Points']
clicker_upgrade_lv = save['clicker_upgrade_lv']
autoclicker1_lv = save['autoclicker1_lv']
autoclicker2_lv = save['autoclicker2_lv']
autoclicker3_lv = save['autoclicker3_lv']
XP = save['XP']
Level = save['Level']
next_level = save['next_level']
gem = save['gem']
autogem1_lv = save ['autogem1_lv']
prestige_lv = save['prestige_lv']

# others
Points_s = 0

root = tk.Tk()

root.title('tklicker')
root.iconbitmap(r'Images\tklicker icon.ico')

frame = tk.Frame(root, bg='white', padx=150, pady=150)
frame.pack(padx=0, pady=0)

lot_frame = tk.Frame(frame, bg='white', padx=20, pady=0)
lot_frame.grid(row=1, column=2)

prestige_lv_label = tk.Label(frame, text=('Prestige Level  ' + str(prestige_lv-1)), bg='white', font=('courier', 20), fg='#EFCC00', pady=20)
prestige_lv_label.grid(row=0, column=0)

level = tk.Label(frame, text=('Level ' + str(Level)), bg='white', font=('courier', 25))
level.grid(row=1, column=1)

xp = tk.Label(frame, text=(str(XP) + ' XP/' + str(next_level) + ' XP'), bg='white', fg='#0087BD')
xp.grid(row=2, column=1)

label = tk.Label(frame, text=round(Points), bg='white', font=('courier', 20), pady=15, width=25)
label.grid(row=3, column=1)

# gems
Lot_text = tk.Label(lot_frame, text=(str(gem) + ' Gems'), bg='white', font=('courier', 15), width=25)
Lot_text.grid(row=0, column=0)

def lot():
    global gem
    global clicker_upgrade_lv
    global autoclicker1_lv
    global autoclicker2_lv
    global autoclicker3_lv
    if gem >= 5:

        while True:
            x = random.randint(1, 4)

            if x == 1:
                clicker_upgrade_lv += 1
                break
            elif x == 2 and autoclicker1_lv > 0:
                autoclicker1_lv += 1
                break
            elif x == 3 and autoclicker2_lv > 0:
                autoclicker2_lv += 1
                break
            elif x == 4 and autoclicker3_lv > 0:
                autoclicker3_lv += 1
                break
        gem -= 5
        order()

Lot = tk.Button(lot_frame, text=('use 5 Gems for 1 upgrade' + '\n' + str(gem) + '/5 Gems'), command=lot, width=25)
Lot.grid(row=1, column=0)

def lot1():
    global gem
    global clicker_upgrade_lv
    global autoclicker1_lv
    global autoclicker2_lv
    global autoclicker3_lv
    if gem >= 40:
        x = 10
        while x > 0:
            y = random.randint(1, 4)
            if y == 1:
                clicker_upgrade_lv += 1
                x -= 1
            elif y == 2 and autoclicker1_lv > 0:
                autoclicker1_lv += 1
                x -= 1
            elif y == 3 and autoclicker2_lv > 0:
                autoclicker2_lv += 1
                x -= 1
            elif y == 4 and autoclicker3_lv > 0:
                autoclicker2_lv += 1
                x -= 1
        gem -= 40
        order()

Lot1 = tk.Button(lot_frame, text=('use 40 Gems for 10 upgrades' + '\n' + str(gem) + '/40 Gems'), command=lot1, width=25,)
Lot1.grid(row=2, column=0)

def autogem1():
    global gem
    global autogem1_lv
    if gem >= round(20 * (autogem1_lv * 1.5)) and autogem1_lv > 0:
        if autogem1_lv < 1:
            gem -= 20
        else:
            gem -= round(20 * (autogem1_lv * 1.5))
            autogem1_lv += 1
            autogem_1_num['text'] = (str(autogem1_lv))
            order()
            autogem_1['text'] = ('Gemgenerator\ncost: ' + str(round(20 * (autogem1_lv * 1.5))))
    elif gem >= 20 and autogem1_lv == 0:
        gem -= 20
        autogem1_lv += 1
        autogem_1_num['text'] = (str(autogem1_lv))
        order()
        autogem_1['text'] = ('Autoclicker' + '\ncost: ' + str(round(20*(autogem1_lv*1.5))))

autogem_1_num = tk.Label(lot_frame, text=str(autogem1_lv), bg='white')
autogem_1_num.grid(row=3, column=0)

autogem_1 = tk.Button(lot_frame, text=('Gemgenerator\ncost: 20 Gems'), command=autogem1, height=2, width=25)
autogem_1.grid(row=4, column=0)

def order():
    global save
    global clicker_upgrade_lv
    global autoclicker1_lv
    global autoclicker2_lv
    global autoclicker3_lv
    global XP
    global Level
    global next_level
    global gem
    global autogem1_lv
    global prestige_lv

    save = {
        "Points": Points,
        "clicker_upgrade_lv": clicker_upgrade_lv,
        "autoclicker1_lv": autoclicker1_lv,
        "autoclicker2_lv": autoclicker2_lv,
        "autoclicker3_lv": autoclicker3_lv,
        "XP": XP,
        "Level": Level,
        "next_level": next_level,
        "gem": gem,
        "autogem1_lv": autogem1_lv,
        "prestige_lv": prestige_lv
    }

    if Points >= 1000000000000:
        points_t = str(Points/1000000000000)
        label['text'] = (str(points_t[:5]) + 'T' + ' Points')
    elif Points >= 1000000000:
        points_b = str(Points/1000000000)
        label['text'] = (str(points_b[:5]) + 'B' + ' Points')
    elif Points >= 1000000:
        points_m = str(Points/1000000)
        label['text'] = (str(points_m[:5]) + 'M' + ' Points')
    elif Points >= 1000:
        points_k = str(Points/1000)
        label['text'] = (str(points_k[:5]) + 'K' + ' Points')
    else:
        label['text'] = (str(round(Points)) + ' Points')

    if XP >= 1000000000000:
        XP_t = str(XP/1000000000000)
        next_level_t = str(next_level/1000000000000)
        xp['text'] = (str(XP_t[:5]) + 'T XP' + '/' + str(next_level_t[:5]) + 'T XP')
    elif XP >= 1000000000:
        XP_b = str(XP/1000000000)
        next_level_b = str(next_level/1000000000)
        xp['text'] = (str(XP_b[:5]) + 'B XP' + '/' + str(next_level_b[:5]) + 'B XP')
    elif XP >= 1000000:
        XP_m = str(XP/1000000)
        next_level_m = str(next_level/1000000)
        xp['text'] = (str(XP_m[:5]) + 'M XP' + '/' + str(next_level_m[:5]) + 'M XP')
    elif XP >= 1000:
        XP_k = str(XP/1000)
        next_level_k = str(next_level / 1000)
        xp['text'] = (str(XP_k[:5]) + 'K XP' + '/' + str(next_level_k[:5]) + 'K XP')
    else:
        xp['text'] = (str(XP) + ' XP/' + str(next_level) + ' XP')
    Lot_text['text'] = (str(gem) + ' Gems')

    if gem >= 1000000000:
        gem_b = str(gem/1000000000)
        Lot_text['text'] = (str(gem_b[:5]) + 'B' + ' Gems')
    elif gem >= 1000000:
        gem_m = str(gem/1000000)
        Lot_text['text'] = (str(gem_m[:5]) + 'M' + ' Gems')
    elif gem >= 1000:
        gem_k = str(gem/1000)
        Lot_text['text'] = (str(gem_k[:5]) + 'K' + ' Gems')
    else:
        gem_ = str(gem)
        Lot_text['text'] = (str(gem_[:5]) + ' Gems')

    Lot['text'] = ('use 5 Gems for 1 upgrade\n' + str(gem_[:5]) + '/5 Gems')
    Lot1['text'] = ('use 40 Gems for 10 upgrades\n' + str(gem_[:5]) + '/40 Gems')
    upgrade_clicker_num['text'] = str(clicker_upgrade_lv-1)
    autoclicker_1_num['text'] = str(autoclicker1_lv)
    autoclicker_2_num['text'] = str(autoclicker2_lv)
    autoclicker_3_num['text'] = str(autoclicker3_lv)
    if autoclicker1_lv > 0:
        autoclicker_1['text'] = ('Autoclicker\ncost: ' + str(500*(autoclicker1_lv*1.5)))
    else:
        autoclicker_1['text'] = ('Autoclicker\ncost: 500')
    if autoclicker2_lv > 0:
        autoclicker_2['text'] = ('Super Autoclicker\ncost: ' + str(10000*(autoclicker2_lv*1.5)))
    else:
        autoclicker_2['text'] = ('Super Autoclicker\ncost: 1000')
    if autoclicker3_lv > 0:
        autoclicker_3['text'] = ('Deluxe Autoclicker\ncost: ' + str(100000*(autoclicker3_lv*1.5)))
    else:
        autoclicker_3['text'] = ('Deluxe Autoclicker\ncost: 100000')
    prestige['text'] = ('Prestige\n' + str(Level) + '/50 Level')
    # write to save.json
    with open('save.json', 'w') as save_file:
        save = json.dump(save, save_file)

def autopoints():
    global Points
    global autoclicker1_lv
    global autoclicker2_lv
    global autoclicker3_lv
    global XP
    global Level
    global next_level
    global gem
    global autogem1_lv
    global prestige_lv

    while True:
        Points_s1 = Points
        if prestige_lv > 1:
            Points += round((10*autoclicker1_lv*(prestige_lv*1.4)))
            Points += round((250*autoclicker2_lv*(prestige_lv*1.4)))
            Points += round((5000*autoclicker3_lv*(prestige_lv * 1.4)))
            gem += (0.05*autogem1_lv*(prestige_lv * 1.4))
        else:
            Points += round(10*autoclicker1_lv)
            Points += round(250*autoclicker2_lv)
            Points += round(5000*autoclicker3_lv)
            gem += (0.05*autogem1_lv)
        time.sleep(1)
        if Points - Points_s1 > 0:
            XP += (Points - Points_s1)
        if XP >= next_level:
            Level += 1
            if Level > 20:
                next_level = round(next_level * 1.25)
            else:
                next_level = round(next_level * 1.7)
            gem_temp = round(Level / 10)
            if gem_temp == 0:
                gem += 1
            else:
                gem += gem_temp
        level['text'] = ('Level ' + str(Level))
        pps['text'] = (str(Points - Points_s1) + 'pp/s')
        order()

t1 = threading.Thread(target=autopoints)
t1.start()

def click():
    global Points
    global clicker_upgrade_lv
    if clicker_upgrade_lv > 2:
        Points += round(((1*(prestige_lv*1.4)*(clicker_upgrade_lv*2))))
    elif clicker_upgrade_lv == 2:
        Points += round(((1*(prestige_lv*1.4)*(clicker_upgrade_lv*2))))
    else:
        Points += round((1*(prestige_lv*1.4)))
    order()

pps = tk.Label(frame, text=Points_s, bg='white', pady=10)
pps.grid(row=4, column=1)

button_1 = tk.Button(frame, text='click me!', height=3, width=20, bg='grey', fg='black', command=click)
button_1.grid(row=5, column=1)

upgrade_frame = tk.Frame(frame, bg='white', padx=20, pady=0)
upgrade_frame.grid(row=1, column=0)

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
upgrade_clicker_num.grid(row=1, column=0)

upgrade_clicker = tk.Button(upgrade_frame, text=('Clickerupgrade' + '\ncost: ' + str(100*(clicker_upgrade_lv*2))), command=Upgrade_Clicker, height=2)
upgrade_clicker.grid(row=2, column=0)

def autoclicker1():
    global Points
    global autoclicker1_lv

    if Points >= round(500*(autoclicker1_lv*1.5)) and autoclicker1_lv > 0:
        if autoclicker1_lv < 1:
            Points -= 500
        else:
            Points -= round(500*(autoclicker1_lv*1.5))
            autoclicker1_lv += 1
            autoclicker_1_num['text'] = (str(autoclicker1_lv))
            order()
            autoclicker_1['text'] = ('Autoclicker' + '\ncost: ' + str(round(500*(autoclicker1_lv*1.5))))
    elif Points >= 500 and autoclicker1_lv == 0:
        Points -= 500
        autoclicker1_lv += 1
        autoclicker_1_num['text'] = (str(autoclicker1_lv))
        order()
        autoclicker_1['text'] = ('Autoclicker' + '\ncost: ' + str(round(500*(autoclicker1_lv*1.5))))

autoclicker_1_num = tk.Label(upgrade_frame, text=str(autoclicker1_lv), bg='white')
autoclicker_1_num.grid(row=3, column=0)

autoclicker_1 = tk.Button(upgrade_frame, text=('Autoclicker\ncost: 500'), command=autoclicker1, height=2)
autoclicker_1.grid(row=4, column=0)

def autoclicker2():
    global Points
    global autoclicker2_lv

    if Points >= (10000*(autoclicker2_lv*1.5)) and autoclicker2_lv > 0:
        if autoclicker2_lv < 1:
            Points -= 10000
        else:
            Points -= (10000*(autoclicker2_lv*1.5))
            autoclicker2_lv += 1
            autoclicker_2_num['text'] = (str(autoclicker2_lv))
            order()
            autoclicker_2['text'] = ('Super Autoclicker' + '\ncost: ' + str(10000*(autoclicker2_lv*1.5)))
    elif Points >= 10000 and autoclicker2_lv == 0:
        Points -= 10000
        autoclicker2_lv += 1
        autoclicker_2_num['text'] = (str(autoclicker2_lv))
        order()
        autoclicker_2['text'] = ('Super Autoclicker' + '\ncost: ' + str(10000*(autoclicker2_lv*1.5)))

autoclicker_2_num = tk.Label(upgrade_frame, text=str(autoclicker2_lv), bg='white')
autoclicker_2_num.grid(row=5, column=0)

autoclicker_2 = tk.Button(upgrade_frame, text=('Super Autoclicker' + '\ncost: 1000'), command=autoclicker2, height=2)
autoclicker_2.grid(row=6, column=0)

def autoclicker3():
    global Points
    global autoclicker3_lv

    if Points >= (100000*(autoclicker3_lv*1.5)) and autoclicker3_lv > 0:
        if autoclicker3_lv < 1:
            Points -= 100000
        else:
            Points -= (100000*(autoclicker3_lv*1.5))
            autoclicker3_lv += 1
            autoclicker_3_num['text'] = (str(autoclicker3_lv))
            order()
            autoclicker_3['text'] = ('Deluxe Autoclicker' + '\ncost: ' + str(100000*(autoclicker3_lv*1.5)))
    elif Points >= 100000 and autoclicker3_lv == 0:
        Points -= 100000
        autoclicker3_lv += 1
        autoclicker_3_num['text'] = (str(autoclicker3_lv))
        order()
        autoclicker_3['text'] = ('Deluxe Autoclicker' + '\ncost: ' + str(100000*(autoclicker3_lv*1.5)))

autoclicker_3_num = tk.Label(upgrade_frame, text=str(autoclicker3_lv), bg='white')
autoclicker_3_num.grid(row=7, column=0)

autoclicker_3 = tk.Button(upgrade_frame, text=('Deluxe Autoclicker' + '\ncost: 100000'), command=autoclicker3, height=2)
autoclicker_3.grid(row=8, column=0)

def Prestige():
    global Points
    global clicker_upgrade_lv
    global autoclicker1_lv
    global autoclicker2_lv
    global autoclicker3_lv
    global XP
    global Level
    global next_level
    global prestige_lv

    if Level >= 50:
        prestige_lv += 1
        Points = 0
        clicker_upgrade_lv = 1
        autoclicker1_lv = 0
        autoclicker2_lv = 0
        autoclicker3_lv = 0
        XP = 0
        Level = 0
        next_level = 100
        order()
        prestige_lv_label['text'] = ('Prestige Level  ' + str(prestige_lv - 1))

prestige = tk.Button(upgrade_frame, text=('Prestige\n' + str(Level) + '/50 Level'), command=Prestige, height=2, width=14, bg='red', fg='black', pady=10)
prestige.grid(row=9, column=0)

root.mainloop()