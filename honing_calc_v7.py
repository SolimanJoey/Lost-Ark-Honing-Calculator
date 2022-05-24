from sre_parse import State
from tkinter import *
from  tkinter import ttk
import time
import copy


# receives user input and outputs materials needed
def honing_calc(values, armor_1302, armor_1340, weapon_1302, weapon_1340, items):
    # putting user input into variables
    item = values[0]
    slvl = values[1]
    elvl = values[2]
    num = values[3]
    
    # armor 1302
    if item == 1:
        # getting materials needed for each level from json file into a list for each material type
        armor_silver_1302 = armor_1302[0]
        armor_gold_1302 = armor_1302[1]
        armor_shards_1302 = armor_1302[2]
        armor_fusion_1302 = armor_1302[3]
        armor_crystals_1302 = armor_1302[4]
        armor_leapstones_1302 = armor_1302[5]

        # creating item_total objects
        for i in range(slvl, elvl):
            name = 'armor_1302 +{} ({})'.format(i+1, num)
            item_mats = item_totals(name, armor_silver_1302[i] * num, armor_gold_1302[i] * num, armor_shards_1302[i] * num, armor_fusion_1302[i] * num, 
                0, armor_crystals_1302[i] * num, 0, armor_leapstones_1302[i] * num, 0)
            items.append(item_mats)
        
        # caclulating total materials
        items[0].silver += sum(armor_silver_1302[slvl:elvl]) * num
        items[0].gold += sum(armor_gold_1302[slvl:elvl]) * num
        items[0].shards += sum(armor_shards_1302[slvl:elvl]) * num
        items[0].sfusion += sum(armor_fusion_1302[slvl:elvl]) * num
        items[0].gcrystals += sum(armor_crystals_1302[slvl:elvl]) * num
        items[0].hleapstones += sum(armor_leapstones_1302[slvl:elvl]) * num


    # armor 1340
    elif item == 2:
        armor_silver_1340 = armor_1340[0]
        armor_gold_1340 = armor_1340[1]
        armor_shards_1340 = armor_1340[2]
        armor_fusion_1340 = armor_1340[3]
        armor_crystals_1340 = armor_1340[4]
        armor_leapstones_1340 = armor_1340[5]

        for i in range(slvl, elvl):
            name = 'armor_1340 +{} ({})'.format(i+1, num)
            item_mats = item_totals(name, armor_silver_1340[i] * num, armor_gold_1340[i] * num, armor_shards_1340[i] * num, 0, armor_fusion_1340[i] * num, 
                armor_crystals_1340[i] * num, 0, 0, armor_leapstones_1340[i] * num)
            items.append(item_mats)

        items[0].silver = sum(armor_silver_1340[slvl:elvl]) * num
        items[0].gold = sum(armor_gold_1340[slvl:elvl]) * num
        items[0].shards = sum(armor_shards_1340[slvl:elvl]) * num
        items[0].bfusion = sum(armor_fusion_1340[slvl:elvl]) * num
        items[0].gcrystals = sum(armor_crystals_1340[slvl:elvl]) * num
        items[0].ghleapstones = sum(armor_leapstones_1340[slvl:elvl]) * num

    # weapon 1302
    elif item == 3:
        weapon_silver_1302 = weapon_1302[0]
        weapon_gold_1302 = weapon_1302[1]
        weapon_shards_1302 = weapon_1302[2]
        weapon_fusion_1302 = weapon_1302[3]
        weapon_crystals_1302 = weapon_1302[4]
        weapon_leapstones_1302 = weapon_1302[5]

        for i in range(slvl, elvl):
            name = 'weapon_1302 +{} ({})'.format(i+1, num)
            item_mats = item_totals(name, weapon_silver_1302[i] * num, weapon_gold_1302[i] * num, weapon_shards_1302[i] * num, weapon_fusion_1302[i] * num, 
                0, 0, weapon_crystals_1302[i] * num, weapon_leapstones_1302[i] * num, 0)
            items.append(item_mats)

        items[0].silver = sum(weapon_silver_1302[slvl:elvl]) * num
        items[0].gold = sum(weapon_gold_1302[slvl:elvl]) * num
        items[0].shards = sum(weapon_shards_1302[slvl:elvl]) * num
        items[0].sfusion = sum(weapon_fusion_1302[slvl:elvl]) * num
        items[0].dcrystals = sum(weapon_crystals_1302[slvl:elvl]) * num
        items[0].hleapstones = sum(weapon_leapstones_1302[slvl:elvl]) * num

    # weapon 1340
    else:
        weapon_silver_1340 = weapon_1340[0]
        weapon_gold_1340 = weapon_1340[1]
        weapon_shards_1340 = weapon_1340[2]
        weapon_fusion_1340 = weapon_1340[3]
        weapon_crystals_1340 = weapon_1340[4]
        weapon_leapstones_1340 = weapon_1340[5]

        for i in range(slvl, elvl):
            name = 'weapon_1340 +{} ({})'.format(i+1, num)
            item_mats = item_totals(name, weapon_silver_1340[i] * num, weapon_gold_1340[i] * num, weapon_shards_1340[i] * num, 0, weapon_fusion_1340[i] * num, 
                0, weapon_crystals_1340[i] * num, 0, weapon_leapstones_1340[i] * num)
            items.append(item_mats)
        
        items[0].silver = sum(weapon_silver_1340[slvl:elvl]) * num
        items[0].gold = sum(weapon_gold_1340[slvl:elvl]) * num
        items[0].shards = sum(weapon_shards_1340[slvl:elvl]) * num
        items[0].bfusion = sum(weapon_fusion_1340[slvl:elvl]) * num
        items[0].dcrystals = sum(weapon_crystals_1340[slvl:elvl]) * num
        items[0].ghleapstones = sum(weapon_leapstones_1340[slvl:elvl]) * num


# get mats from microservice
def get_mats(item, mat):
    f = open("./text_files/list.txt", "w")
    f.write("1\n")
    f.write("./text_files/materials.json\n")
    f.write(item + "\n")
    f.write(mat)
    f.close()
    time.sleep(2)
    f = open("./text_files/list.txt", "r")
    mats = f.readline()
    # if microservice is not running fill arrays with 0
    if mats == "1\n":
        values = [0] * 20
    else:
        print("Grabbing " + mat)
        temp = mats.split(",")
        values = [int(i) for i in temp]
    f.close()
    return values


# get mats into arrays
def get_mats_r():
    print("Grabbing mats...")
    print("Armor 1302...")
    # get mats into lists
    armor_1302 = []
    armor_1302.append(get_mats('armor1302', 'silver'))
    armor_1302.append(get_mats('armor1302', 'gold'))
    armor_1302.append(get_mats('armor1302', 'shards'))
    armor_1302.append(get_mats('armor1302', 'fusion'))
    armor_1302.append(get_mats('armor1302', 'crystals'))
    armor_1302.append(get_mats('armor1302', 'leapstones'))

    print("Armor 1340...")
    # get mats into lists
    armor_1340 = []
    armor_1340.append(get_mats('armor1340', 'silver'))
    armor_1340.append(get_mats('armor1340', 'gold'))
    armor_1340.append(get_mats('armor1340', 'shards'))
    armor_1340.append(get_mats('armor1340', 'fusion'))
    armor_1340.append(get_mats('armor1340', 'crystals'))
    armor_1340.append(get_mats('armor1340', 'leapstones'))

    print("Weapon 1302...")
    # get mats into lists
    weapon_1302 = []
    weapon_1302.append(get_mats('weapon1302', 'silver'))
    weapon_1302.append(get_mats('weapon1302', 'gold'))
    weapon_1302.append(get_mats('weapon1302', 'shards'))
    weapon_1302.append(get_mats('weapon1302', 'fusion'))
    weapon_1302.append(get_mats('weapon1302', 'crystals'))
    weapon_1302.append(get_mats('weapon1302', 'leapstones'))

    print("Weapon 1340...")
    # get mats into lists
    weapon_1340 = []
    weapon_1340.append(get_mats('weapon1340', 'silver'))
    weapon_1340.append(get_mats('weapon1340', 'gold'))
    weapon_1340.append(get_mats('weapon1340', 'shards'))
    weapon_1340.append(get_mats('weapon1340', 'fusion'))
    weapon_1340.append(get_mats('weapon1340', 'crystals'))
    weapon_1340.append(get_mats('weapon1340', 'leapstones'))

    return [armor_1302, armor_1340, weapon_1302, weapon_1340]



class item_totals:
    name = ''
    silver = 0
    gold = 0
    shards = 0
    sfusion = 0
    bfusion = 0
    gcrystals = 0
    dcrystals = 0
    hleapstones = 0
    ghleapstones = 0
    
    def __init__(self, name, silver, gold, shards, sfusion, bfusion, gcrystals, dcrystals, hleapstones, ghleapstones):
        self.name = name
        self.silver = silver
        self.gold = gold
        self.shards = shards
        self.sfusion = sfusion
        self.bfusion = bfusion
        self.gcrystals = gcrystals
        self.dcrystals = dcrystals
        self.hleapstones = hleapstones
        self.ghleapstones = ghleapstones


if __name__ == '__main__':   
    item_mats_init = get_mats_r()
    armor_1302 = item_mats_init[0]
    armor_1340 = item_mats_init[1]
    weapon_1302 = item_mats_init[2]
    weapon_1340 = item_mats_init[3]

    # current state of materials
    item_list = []
    u_item_list = []
    totals = item_totals("Total", 0, 0, 0, 0, 0, 0, 0, 0, 0)
    u_totals = item_totals("Total", 0, 0, 0, 0, 0, 0, 0, 0, 0)
    item_list.append(totals)
    u_item_list.append(u_totals)

    def reset():
        for i in my_game.get_children():
            my_game.delete(i)

        global item_list
        global u_item_list

        u_item_list = copy.deepcopy(item_list)

        item_list = []
        totals = item_totals("Total", 0, 0, 0, 0, 0, 0, 0, 0, 0)
        item_list.append(totals)

        undo_button['state'] = ACTIVE

        my_game.grid(row=3, column=5)
    
    item = ""
    def add():
        for i in my_game.get_children():
            my_game.delete(i)

        global item_list
        global u_item_list

        u_item_list = copy.deepcopy(item_list)

        values=[item, int(slvl), int(elvl_entry.get()), int(count_entry.get())]
        honing_calc(values, armor_1302, armor_1340, weapon_1302, weapon_1340, item_list)

        undo_button['state'] = ACTIVE

        for i in range(len(item_list)):
            my_game.insert(parent='',index='end',iid=i,text='',
                values=(item_list[i].name, item_list[i].silver, item_list[i].gold, item_list[i].shards, 
                item_list[i].sfusion, item_list[i].bfusion, item_list[i].gcrystals, 
                item_list[i].dcrystals, item_list[i].hleapstones, item_list[i].ghleapstones))

        my_game.grid(row=3, column=5)


    def undo():
        def yes():
            warning.destroy()
            for i in my_game.get_children():
                my_game.delete(i)

            global item_list
            global u_item_list

            item_list = copy.deepcopy(u_item_list)

            undo_button['state'] = DISABLED

            for i in range(len(item_list)):
                my_game.insert(parent='',index='end',iid=i,text='',
                    values=(item_list[i].name, item_list[i].silver, item_list[i].gold, item_list[i].shards, 
                    item_list[i].sfusion, item_list[i].bfusion, item_list[i].gcrystals, 
                    item_list[i].dcrystals, item_list[i].hleapstones, item_list[i].ghleapstones))
        
        warning = Toplevel(ws)
        warning.geometry("360x100")
        warning.title("Warning!")
        Label(warning, text="There is no redo option. Would you like to continue with undo?").grid(row=0, column=0)
        Button(warning, text="Undo", command=yes).grid(row=1, column=0)
        Button(warning, text="Cancel", command=warning.destroy).grid(row=2, column=0)

        my_game.grid(row=3, column=5)
        warning.mainloop()


    def delete():
        global item_list
        global u_item_list

        u_item_list = copy.deepcopy(item_list)

        selected_item = my_game.focus()
        select = my_game.item(selected_item, "values")
        del_name = select[0]

        for i in range(1, len(item_list)):
            if item_list[i].name == del_name:
                item_list[0].silver -= item_list[i].silver
                item_list[0].gold -= item_list[i].gold
                item_list[0].shards -= item_list[i].shards
                item_list[0].sfusion -= item_list[i].sfusion
                item_list[0].bfusion -= item_list[i].bfusion
                item_list[0].gcrystals -= item_list[i].gcrystals
                item_list[0].dcrystals -= item_list[i].dcrystals
                item_list[0].hleapstones -= item_list[i].hleapstones
                item_list[0].ghleapstones -= item_list[i].ghleapstones
                item_list.pop(i)
                break          
        
        undo_button['state'] = ACTIVE

        for i in my_game.get_children():
            my_game.delete(i)

        for i in range(len(item_list)):
            my_game.insert(parent='',index='end',iid=i,text='',
                values=(item_list[i].name, item_list[i].silver, item_list[i].gold, item_list[i].shards, 
                item_list[i].sfusion, item_list[i].bfusion, item_list[i].gcrystals, 
                item_list[i].dcrystals, item_list[i].hleapstones, item_list[i].ghleapstones))

        my_game.grid(row=3, column=5)


    def item_select(e):
        global item
        options_1302 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        options_1340 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        options_armor = [1, 2, 3, 4, 5]
        options_weapons = [1]
        eoptions_1302 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        eoptions_1340 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        item_option = item_entry.get()
        if item_option == "Armor 1302":
            item = 1
        if item_option == "Armor 1340":
            item = 2
        if item_option == "Weapon 1302":
            item = 3
        if item_option == "Weapon 1340":
            item = 4
        
        if item_option == "Armor 1302" or item_option == "Weapon 1302":
            slvl_entry.config(value=options_1302)
            elvl_entry.config(value=eoptions_1302)

        else:
            slvl_entry.config(value=options_1340)
            elvl_entry.config(value=eoptions_1340)

        if item_option == "Armor 1302" or item_option == "Armor 1340":
            count_entry.config(value=options_armor)

        else:
            count_entry.config(value=options_weapons)

        slvl_entry.current(0)
        elvl_entry.current(0)
        count_entry.current(0)
    
    slvl = 0
    def slvl_select(e):
        global slvl
        elvl = []
        item = item_entry.get()
        if item == "Armor 1302" or item == "Weapon 1302":
            limit = 16
        else:
            limit = 21
        slvl = slvl_entry.get()
        for i in range(int(slvl) + 1, limit):
            elvl.append(i)
        elvl_entry.config(value=elvl)
        elvl_entry.current(0)


    # initialize gui
    ws  = Tk()
    ws.title('Honing Calculator')
    ws.geometry('933x879')
    ws['bg'] = '#AC99F2'

    game_frame = Frame(ws)
    game_frame.grid(row=3, column=0, columnspan=10)

    item_options = ["Armor 1302", "Armor 1340", "Weapon 1302", "Weapon 1340"]

    item_entry_label = Label(ws, text="Item")
    item_entry_label.grid(row=0, column=0, sticky=NSEW)
    item_entry = ttk.Combobox(ws, value=item_options)
    item_entry.current(0)
    item_entry.grid(row=0, column=1, sticky=NSEW)
    item_entry.bind("<<ComboboxSelected>>", item_select)

    slvl_entry_label = Label(ws, text="Starting Level")
    slvl_entry_label.grid(row=0, column=2, sticky=NSEW)
    slvl_entry = ttk.Combobox(ws, value=[" "])
    slvl_entry.current(0)
    slvl_entry.grid(row=0, column =3, sticky=NSEW)
    slvl_entry.bind("<<ComboboxSelected>>", slvl_select)

    elvl_entry_label = Label(ws, text="End Level")
    elvl_entry_label.grid(row=0, column=4, sticky=NSEW)
    elvl_entry = ttk.Combobox(ws, value=[" "])
    elvl_entry.current(0)
    elvl_entry.grid(row=0, column =5, sticky=NSEW)

    count_entry_label = Label(ws, text="Count")
    count_entry_label.grid(row=0, column=6, sticky=NSEW)
    count_entry = ttk.Combobox(ws, value=[" "])
    count_entry.current(0)
    count_entry.grid(row=0, column =7, sticky=NSEW)

    add_button = Button(ws, text="Add", command=add)
    add_button.grid(row=0, column=8, sticky=NSEW)

    undo_button = Button(ws, text="Undo", command=undo, state=DISABLED)
    undo_button.grid(row=1, column=0, sticky=NSEW)

    reset_button = Button(ws, text="Reset", command=reset)
    reset_button.grid(row=1, column=1, sticky=NSEW)

    delete_button = Button(ws,text="Delete", command=delete)
    delete_button.grid(row=1, column=2, sticky=NSEW)

    my_game = ttk.Treeview(game_frame, selectmode="browse", height=40)

    my_game['columns'] = ('Item', 'Silver', 'Gold', 'Honing Shards', 'Simple Oreha Fusion Materials', 'Basic Oreha Fusion Materials',
        'Guardian Stone Crystals', 'Destruction Stone Crystals', 'Honor Leapstones', 'Great Honor Leapstones')

    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("Item",anchor=CENTER, width=200)
    my_game.column("Silver",anchor=CENTER,width=80)
    my_game.column("Gold",anchor=CENTER,width=80)
    my_game.column("Honing Shards",anchor=CENTER,width=80)
    my_game.column("Simple Oreha Fusion Materials",anchor=CENTER,width=80)
    my_game.column("Basic Oreha Fusion Materials",anchor=CENTER, width=80)
    my_game.column("Guardian Stone Crystals",anchor=CENTER,width=80)
    my_game.column("Destruction Stone Crystals",anchor=CENTER,width=80)
    my_game.column("Honor Leapstones",anchor=CENTER,width=80)
    my_game.column("Great Honor Leapstones",anchor=CENTER,width=90)

    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("Item",text="Item",anchor=CENTER)
    my_game.heading("Silver",text="Silver",anchor=CENTER)
    my_game.heading("Gold",text="Gold",anchor=CENTER)
    my_game.heading("Honing Shards",text="Shards",anchor=CENTER)
    my_game.heading("Simple Oreha Fusion Materials",text="Simple Oreha",anchor=CENTER)
    my_game.heading("Basic Oreha Fusion Materials",text="Basic Oreha",anchor=CENTER)
    my_game.heading("Guardian Stone Crystals",text="Guardian",anchor=CENTER)
    my_game.heading("Destruction Stone Crystals",text="Destruction",anchor=CENTER)
    my_game.heading("Honor Leapstones",text="HLeapstones",anchor=CENTER)
    my_game.heading("Great Honor Leapstones",text="GHLeapstones",anchor=CENTER)

    my_game.grid(row=3, column=5)

    ws.mainloop()
