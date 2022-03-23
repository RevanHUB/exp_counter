import keyboard;
import time;
from tkinter import *;
from tkinter import messagebox



def btn_clicked():
    print("Button Clicked")

#graphic UI
window = Tk();
window.title("Multitool by REVAN");
window.geometry("1283x718");
bg = PhotoImage(file = "media/home_bg.png")
exp_bg = PhotoImage(file = "media/exp_bg.png")
gear_bg = PhotoImage(file = "media/gear_bg.png")
window.wm_iconbitmap('media/myicon.ico');
window.configure(bg = "#FF295E");

window.resizable(False, False)


#creacion del bg y las entradas
l0 = Label(window, image = bg)
l0.place(x = 0, y = 0)

def left_menu_funct():
    left_bar = Frame(window,width=470,height=718, bg="#FF295E");
    left_bar.place(x=2, y=3);

    def close_bar():
        left_bar.destroy();
    global button_close_img;
    global button_close_img_resize;
    button_close_img = PhotoImage(file="media/close_button_circle.png");
    Button(left_bar, image = button_close_img, command=close_bar, border=0, activebackground="#FF295E", bg="#FF295E").place(x=5, y=5);
    Button(left_bar, text = "Home", command=home_frame, border=0, activebackground="#FF295E", bg="#FF295E").place(x=35, y=50);
    Button(left_bar, text = "Exp Frame", command=exp_frame, border=0, activebackground="#FF295E", bg="#FF295E").place(x=35, y=100);
    Button(left_bar, text = "Gear Calculator", command=gear_frame, border=0, activebackground="#FF295E", bg="#FF295E").place(x=35, y=150);

button_open_img = PhotoImage(file='media/menu.png');
left_bar_button = Button(window, command=left_menu_funct, image=button_open_img, activebackground="#FF295E", border=0, bg="#FF295E").place(x=10, y=10);


# FRAME #1
def exp_frame():
    button_open_img = PhotoImage(file='media/menu.png');
    left_bar_button = Button(window, command=left_menu_funct, image=button_open_img, activebackground="#FF295E", border=0, bg="#FF295E").place(x=10, y=10);
    global exp_bg;
    background_change = Label(window, image = exp_bg)
    background_change.place(x = 0, y = 0)
    # menu 
    
    # añadir las entradas
    
    count_time = IntVar();
    el0=Entry(window, textvariable=count_time, width=10, font=("Calibri", 42), bd=0, bg = "white", justify="center");
    el0.place(x = 791, y = 190);
    #el0.insert('1.0', timer, "center");
    el0.config(state=DISABLED);

    exp_entry = IntVar();
    el1=Entry(window, textvariable=exp_entry, width=20, font=("Calibri", 13, "bold"),  bg = "white", bd=0, justify="center");
    #el1=Text(window, width=30);
    #el1.grid(row=1, column=0);
    #el1.insert('1.0', ""+exp_entry, "center");
    el1.place(x = 743, y = 343);

    exp_rendimiento_entry = IntVar();
    el2=Entry(window,textvariable=exp_rendimiento_entry, width=20,font=("Calibri", 13,  "bold"),  bg = "white", bd=0,justify="center");
    #el2.grid(row=1, column=1);
    #el2.place(x = 50, y = 40);
    el2.place(x = 741, y = 403);
    el2.config(state=DISABLED);

    exp_min_entry = IntVar();
    el3=Entry(window,textvariable=exp_min_entry, width=20, font=("Calibri", 13,  "bold"),  bg = "white", bd=0, justify="center");
    #el3.grid(row=1, column=2);
    el3.place(x = 741, y = 463);
    el3.config(state=DISABLED);

    exp_hour_entry = IntVar();
    el4=Entry(window,textvariable=exp_hour_entry, width=20, font=("Calibri", 13,  "bold"),  bg = "white", bd=0, justify="center");
    #el4.grid(row=1, column=3);
    el4.place(x = 741, y = 523);
    el4.config(state=DISABLED);
    #accion de botones
    global contador;
    contador = int();
    contador = 1;
    def pulsar_tecla(event):
        global contador;
        valor_exp = int(exp_entry.get());
        contador = contador + 1;
        cantidad = int();
        cantidad = contador * valor_exp
        exp_rendimiento_entry.set(cantidad);
        exp_min_entry.set(cantidad);
        exp_hour_entry.set(cantidad*60);
        return contador;
        
    def añadir_exp():
        valor_exp = int(exp_entry.get());
        exp_min = int();
        exp_min = valor_exp * 60;
        exp_hour = int();
        exp_hour = valor_exp * 3600;
        exp_min_entry.set(exp_min);
        exp_hour_entry.set(exp_hour);
    

    def añadir_exp_intro(event):
        global contador;
        valor_exp = int(exp_entry.get());
        exp_min = int();
        exp_min = valor_exp * 60;
        exp_hour = int();
        exp_hour = valor_exp * 3600;
        exp_rend = int();
        exp_rend = valor_exp * contador;
        exp_rendimiento_entry.set(exp_rend);
        exp_min_entry.set(exp_min);
        exp_hour_entry.set(exp_hour);
        contador +=1;

    def delete_onbutton():
        contador = 0;
        exp_entry.set(0);
        exp_min_entry.set(0);
        exp_hour_entry.set(0);
        exp_rendimiento_entry.set(0);

    def delete_onkey(event):
        global contador;
        contador = 0;
        exp_min_entry.set(0);
        exp_hour_entry.set(0);
        exp_rendimiento_entry.set(0);



    def countdown():
        t = 60;
        while t > -1:
            stop = int();
            if exp_rendimiento_entry.get() >= 0:
                valor_exp_new = int(exp_rendimiento_entry.get());
            else:
                valor_exp_new = int(exp_entry.get());
            
            count_time.set(t);
            time.sleep(1);
            t -= 1;
            window.update();
            
            if t < 0:
                break
            def stop(self):
                stop = 0;
                print(stop) 
                return stop;
            if stop == 0:
                break;
            
            window.bind("<Key>", stop)
            
       
       
            

    
    window.bind("<Insert>", pulsar_tecla)
    window.bind("<Return>", añadir_exp_intro)
    window.bind("<Delete>", delete_onkey)

    b1 = Button(window,text="Contar", font=("Calibri", 12), activebackground="white", width=15, height=1, bg = "white", bd = 0, command = countdown, highlightthickness=0);
    b1.place(x = 734, y = 650);
    b3 = Button(window,text="Restart",font=("Calibri", 12), width=15, bg = "white", activebackground="white", height=1, bd = 0, command = delete_onbutton, );
    b3.place(x = 903, y = 650);
    b2 = Button(window,text="Salir",font=("Calibri", 12), width=15, bg = "white", activebackground="white", height=1, bd = 0, command = quit );
    b2.place(x = 1075, y = 650);


def gear_frame():

    global gear_bg;
    background_change = Label(window, image = gear_bg)
    background_change.place(x = 0, y = 0)
    # menu 
    
    # añadir las entradas

    gs_hel = IntVar();
    gs_1=Entry(window, textvariable=gs_hel, width=0, font=("Calibri", 30), bd=0, bg = "#222222", justify="center");
    gs_1.configure(fg = "white");
    gs_1.place(x = 45, y = 145);
    
    gs_chest = IntVar();
    gs_2=Entry(window, textvariable=gs_chest, width=0, font=("Calibri", 30), bd=0, bg = "#222222", justify="center");
    gs_2.configure(fg = "white");
    gs_2.place(x = 45, y = 220);

    gs_hands = IntVar();
    gs_3=Entry(window, textvariable=gs_hands, width=0, font=("Calibri", 30), bd=0, bg = "#222222", justify="center");
    gs_3.configure(fg = "white");
    gs_3.place(x = 45, y = 295);

    gs_legs = IntVar();
    gs_4=Entry(window, textvariable=gs_legs, width=0, font=("Calibri", 30), bd=0, bg = "#222222", justify="center");
    gs_4.configure(fg = "white");
    gs_4.place(x = 45, y = 370);

    gs_feets = IntVar();
    gs_5=Entry(window, textvariable=gs_feets, width=0, font=("Calibri", 30), bd=0, bg = "#222222", justify="center");
    gs_5.configure(fg = "white");
    gs_5.place(x = 45, y = 445);

    gs_shield = IntVar();
    gs_6=Entry(window, textvariable=gs_shield, width=0, font=("Calibri", 30), bd=0, bg = "#222222", justify="center");
    gs_6.configure(fg = "white");
    gs_6.place(x = 45, y = 520);

    gs_weapon = IntVar();
    gs_7=Entry(window, textvariable=gs_weapon, width=0, font=("Calibri", 30), bd=0, bg = "#222222", justify="center");
    gs_7.configure(fg = "white");
    gs_7.place(x = 435, y = 145);

    gs_weapon2 = IntVar();
    gs_8=Entry(window, textvariable=gs_weapon2, width=0, font=("Calibri", 30), bd=0, bg = "#222222", justify="center");
    gs_8.configure(fg = "white");
    gs_8.place(x = 435, y = 220);

    gs_amulet = IntVar();
    gs_9=Entry(window, textvariable=gs_amulet, width=0, font=("Calibri", 30), bd=0, bg = "#222222", justify="center");
    gs_9.configure(fg = "white");
    gs_9.place(x = 435, y = 295);

    gs_ring = IntVar();
    gs_10=Entry(window, textvariable=gs_ring, width=0, font=("Calibri", 30), bd=0, bg = "#222222", justify="center");
    gs_10.configure(fg = "white");
    gs_10.place(x = 435, y = 375);

    gs_earring = IntVar();
    gs_11=Entry(window, textvariable=gs_earring, width=0, font=("Calibri", 30), bd=0, bg = "#222222", justify="center");
    gs_11.configure(fg = "white");
    gs_11.place(x = 435, y = 455);

    gsvars = IntVar();
    gs_0=Entry(background_change, textvariable=gsvars, width=3, font=("Calibri", 42), bd=0, bg = "white", justify="center");
    gs_0.place(x = 861, y = 320);
    gs_0.config(state=DISABLED);

    

    def gs_calculate():
    
        shield = gs_shield.get();
        helmet = gs_hel.get();
        chest = gs_chest.get();
        hands = gs_hands.get();
        legs = gs_legs.get();
        feets = gs_feets.get();
        weapon = gs_weapon.get();
        weapon2 = gs_weapon2.get();
        amulet = gs_amulet.get();
        ring = gs_ring.get();
        earring = gs_earring.get();
        score = gsvars.get();

        if shield > 0:
            print("gs_calculate_event_shield")
            result = int();
            result = (helmet + chest + hands + legs + feets + shield + weapon + weapon2 + amulet + ring + earring)/11;
            gsvars.set(result);
            #return gsvar;
        if shield <= 0:
            print("gs_calculate_event_noshield")
            result = int();
            result = (helmet + chest + hands + legs + feets + weapon + weapon2 + amulet + ring + earring)/10;
            gsvars.set(result);
            #return gs_var

   
    window.bind("<Insert>", gs_calculate)

    b1 = Button(window,text="Contar", font=("Calibri", 12), activebackground="white", width=15, height=1, bg = "white", bd = 0, command = gs_calculate, highlightthickness=0);
    b1.place(x = 734, y = 650);
    b2 = Button(window,text="Salir",font=("Calibri", 12), width=15, bg = "white", activebackground="white", height=1, bd = 0, command = quit );
    b2.place(x = 1075, y = 650);

def home_frame():
    l0 = Label(window, image = bg)
    l0.place(x = 0, y = 0)




window.mainloop();


