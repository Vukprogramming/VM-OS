import tkinter as tk
from tkinter import messagebox

# sigma python
# ezz ezz ezz



# Cookier clicker functions and window

cookies = 0
cookies_per_click = 1
upgrades_cost = 10
timer_id = None
time_in_ms = 0

def open_cookie_clicker():
    global cookies, cookies_per_click, upgrades_cost
    
    cookie_clicker_window = tk.Toplevel()
    cookie_clicker_window.title("Cookie Clicker")
    cookie_clicker_window.resizable(False, False)
    cookie_clicker_window.geometry("300x200")
    center_window(cookie_clicker_window, 300, 200)

    def click_cookie():
        global cookies
        cookies += cookies_per_click
        update_display()

    def upgrade_click():
        global cookies, cookies_per_click, upgrades_cost
        
        if cookies >= upgrades_cost:
            cookies -= upgrades_cost
            cookies_per_click += 1
            upgrades_cost *= 2
            update_display()
            messagebox.showinfo("Upgrade Purchased", f"Cookies per click increased to {cookies_per_click}.")
        else:
            messagebox.showwarning("Not Enough Cookies", "You need more cookies to buy this upgrade!")

    def update_display():
        cookie_label.config(text=f"Cookies: {cookies}")
        upgrade_button.config(text=f"Upgrade: {upgrades_cost} cookies")

    cookie_label = tk.Label(cookie_clicker_window, text=f"Cookies: {cookies}", font=('Arial', 20))
    cookie_label.grid(row=0, column=0, padx=20, pady=10)

    cookie_button = tk.Button(cookie_clicker_window, text="Click me!", font=('Arial', 20), command=click_cookie, bg="#ffcc00")
    cookie_button.grid(row=1, column=0, padx=20, pady=10)

    upgrade_button = tk.Button(cookie_clicker_window, text=f"Upgrade: {upgrades_cost} cookies", font=('Arial', 20), command=upgrade_click, bg="#4CAF50")
    upgrade_button.grid(row=2, column=0, padx=20, pady=10)

# System window

def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("System")
    new_window.geometry("600x400")
    center_window(new_window, 600, 400)
    new_window.resizable(False, False)

    label = tk.Label(new_window, text="OS = VM", font=("Arial", 20))
    label2 = tk.Label(new_window, text="CPU = Intel i7 3770", font=("Arial", 20))
    label3 = tk.Label(new_window, text="RAM = 8GB, DDR4", font=("Arial", 20))
    label4 = tk.Label(new_window, text="GPU = AMD HD 7700", font=("Arial", 20))
    label_mem = tk.Label(new_window, text="Memory = 1TB SSD", font=("Arial", 20))
    label5 = tk.Label(new_window, text="Motherboard = Fujitsu MB Esprimo P556", font=("Arial", 20))

    label.place(x=20, y=20)
    label2.place(x=20, y=60)
    label3.place(x=20, y=100)
    label4.place(x=20, y=140)
    label_mem.place(x=20, y= 180)
    label5.place(x=20, y=220)

# Downloader

def open_new_window2():
    new_window2 = tk.Toplevel()
    new_window2.title('Downloader')
    new_window2.geometry("600x400")
    center_window(new_window2, 600, 400)
    new_window2.resizable(False, False)

    button_games = tk.Button(new_window2, text="Games", font=("Arial", 18), command=gamewin)
    button_games.place(x=50, y=50)

    button3 = tk.Button(new_window2, text="5 Songs", font=("Arial", 24), command=lambda: install_quiz(5))
    button3.place(x=220, y=100)

    button4 = tk.Button(new_window2, text="10 Songs", font=("Arial", 24), command=lambda: install_quiz(10))
    button4.place(x=220, y=200)

    button5 = tk.Button(new_window2, text="15 Songs", font=("Arial", 24), command=lambda: install_quiz(15))
    button5.place(x=220, y=300)

    label6 = tk.Label(new_window2, text="Click what you want to download :)", font=('Arial', 20))
    label6.place(x=100, y=10)

# Game library

def gamewin():
    gameins = tk.Toplevel()
    gameins.title("Game Library")
    gameins.geometry("600x400")
    center_window(gameins, 600, 400)

    label_gamer = tk.Label(gameins, text="Choose a game to download :)", font=("Arial", 24))
    label_gamer.pack()

    button_virus = tk.Button(gameins, text="Free CS2", font=("Arial", 24), command=antivirus)
    button_virus.place(x=50, y=100)

# Virus and Antivirus functions

def antivirus():
    result = messagebox.showwarning(
        "{VM Security} Malware detected!", 
        "Malware has been detected and the installation has been stopped. This program may harm your computer!")
    
    if result is None: 
        return
    
    open_confirmation()

def open_confirmation():
    result2 = messagebox.askyesno(
        "{VM Security} Malware detected!", 
        "Malware has been detected on this program! Are you sure you want to proceed with the installation (THIS MAY HARM YOUR COMPUTER)?")
    
    if result2:
        open_virus()

def open_virus():
    open_bgcol()
    open_butcus()
    open_cookie_clicker()
    open_label_terminal()
    open_notepad()
    button.config(state="disabled")
    button2.config(state="disabled")
    button6.config(state="disabled")
    button_cookie_clicker.config(state="disabled")
    button_notepad.config(state="disabled")
    button_Sett.config(state="disabled")
    button_SIfolder.config(state="disabled")
    button_SM.config(state="disabled")
    button_filex.config(state="disabled")
    
    root.config(bg="red")
    button.config(bg="teal")
    button2.config(bg="magenta")
    button6.config(bg="green")
    button_cookie_clicker.config(bg="blue")
    root.after(9000, show_final_warning)
    messagebox.showerror("100111001010", "1001111010101110001111")
    messagebox.showerror("100111001010", "1001111010101110001111")
    messagebox.showerror("100111001010", "1001111010101110001111")
    messagebox.showerror("100111001010", "1001111010101110001111")
    messagebox.showerror("100111001010", "1001111010101110001111")
    messagebox.showinfo("FY7&TGF30(*)&(&DEK::", "DEN&yGD48Y4809olDW][P;]KR")
    messagebox.showwarning("HACK", "YOU HAVE BEEN HACKED")
    messagebox.showerror("100111001010", "1001111010101110001111")
    messagebox.showerror("100111001010", "1001111010101110001111")
    messagebox.showerror("100111001010", "1001111010101110001111")
    messagebox.showerror("100111001010", "1001111010101110001111")
    messagebox.showerror("100111001010", "1001111010101110001111")
    messagebox.showinfo("FY7&TGF30(*)&(&DEK::", "DEN&yGD48Y4809olDW][P;]KR")


def show_final_warning():
    messagebox.showwarning("{VM Security} Malware has infected your PC!", "Malware has infected your PC! VM Security has stopped it and all other programs from executing the malware will be deleted. Your PC will restart.")
    root.destroy()

# Downloader functions

def install_quiz(num_songs):
    new_window3 = tk.Toplevel()
    new_window3.title("Song Downloader")
    new_window3.geometry("400x200")
    new_window3.resizable(False, False)
    center_window(new_window3, 400, 200)

    label7 = tk.Label(new_window3, text=f"Downloading {num_songs} songs.", font=("Arial", 20))
    label7.place(x=100, y=70)

    update_download_label(label7, 0, new_window3)

def update_download_label(label, count, window):
    downloading_texts = ["Downloading.", "Downloading..", "Downloading..."]
    label.config(text=downloading_texts[count % 3])
    
    if count < 17:
        label.after(1000, update_download_label, label, count + 1, window)
    elif count == 17:
        label.config(text="Download finished")
        label.after(2000, window.destroy)

# Label terminal

def open_label_terminal():
    label_terminal_window = tk.Toplevel() 
    label_terminal_window.title("MIP Terminal")
    label_terminal_window.geometry("600x400")
    center_window(label_terminal_window, 600, 400)

    text_box = tk.Text(label_terminal_window, font=('Arial', 14), width=40, height=10)
    text_box.pack(pady=20)

    submit_button = tk.Button(label_terminal_window, text="Submit", font=('Arial', 14), command=lambda: submit_text(text_box, label_terminal_window))
    submit_button.pack(pady=10)

# Circle command

def open_circle_window():
    circle_window = tk.Toplevel()
    circle_window.title("PXL.ter")
    circle_window.geometry("600x350")
    center_window(circle_window, 600, 350)

    labelc1 = tk.Label(circle_window, text="      ****      ", font=("Arial", 24))
    labelc1.pack()
    labelc2 = tk.Label(circle_window, text="    *       *   ", font=("Arial", 24))
    labelc2.pack()
    labelc3 = tk.Label(circle_window, text="  *           * ", font=("Arial", 24))
    labelc3.pack()
    labelc4 = tk.Label(circle_window, text=" *             * ", font=("Arial", 24))
    labelc4.pack()
    labelc5 = tk.Label(circle_window, text=" *             * ", font=("Arial", 24))
    labelc5.pack()
    labelc6 = tk.Label(circle_window, text="  *           *  ", font=("Arial", 24))
    labelc6.pack()
    labelc7 = tk.Label(circle_window, text="    *       *   ", font=("Arial", 24))
    labelc7.pack()
    labelc8 = tk.Label(circle_window, text="      ****     ", font=("Arial", 24))
    labelc8.pack()

# Something for notepad commands also

def submit_text(text_box, label_terminal_window):
    entered_text = text_box.get("1.0", "end-1c").strip()  

    if entered_text.startswith("run.cmd:opn<com>:; cmd.label<terminal>::"):
  
        label_text = entered_text[len("run.cmd:opn<com>:; cmd.label<terminal>::"):].strip()

        new_label_window = tk.Toplevel()
        new_label_window.title("Command Output")
        new_label_window.geometry("400x200")
        center_window(new_label_window, 400, 200)

        label = tk.Label(new_label_window, text=label_text, font=("Arial", 20))
        label.place(x=20, y=300)

        print(f"Label updated to: {label_text}")
    else:
        print("Invalid command or no command detected.")

def open_new_window4():
    new_window4 = tk.Toplevel()
    new_window4.title("Stopwatch")
    new_window4.geometry("600x400")
    center_window(new_window4, 600, 400)
    new_window4.config(bg="lightyellow")

    button7 = tk.Button(new_window4, text="Start", font=("Arial", 20), command=lambda: play_music(new_window4))
    button7.place(x=250, y=250)

    button8 = tk.Button(new_window4, text="0:00:00", font=("Arial", 50), command=lambda: stop_music(new_window4))
    button8.place(x=150, y=100)

# Notepad and command functions

def open_notepad():
    def submit_text():
        entered_text = text_box.get("1.0", "end-1c")


        if entered_text == "run.cmd:quit, True, True::":
            notepad.destroy()

        if entered_text == "run.cmd:opn<com>:; sys::":
            open_new_window()

        if entered_text == "run.cmd:opn<com>:; dlnw::":
            open_new_window2()

        if entered_text == "run.cmd:opn<com>:; stpwat<time>::":
            open_new_window4()
        
        if entered_text == "run.cmd:opn<com>:; coki_clk<game>::":
            open_cookie_clicker()
        
        if entered_text == "run.cmd:opn<com>:; cmd.label<terminal>::":
            open_label_terminal()

        if entered_text == "run.cmd//admin::_per:; cmd_.del /rq {dl} /sys_main/::":
            open_confirmation2()

        if entered_text == "run:cmd//comp:%s<<trigmet>>%//lambda/VM.ter;%c,,cmd..{i in 10},, |program|, 3.13::":
            open_circle_window()

    label_breakin2.config(fg="green", bg="black")
    label_break.config(fg="green", bg="black")
    label_breakin.config(fg="green", bg="black")
    label_breakin2.config(fg="green", bg="black")

    notepad = tk.Toplevel()
    notepad.title("Notepad")
    notepad.geometry("600x400")
    center_window(notepad, 600, 400)

    text_box = tk.Text(notepad, font=('Arial', 14), width=40, height=10)
    text_box.pack(pady=20)

    submit_button = tk.Button(notepad, text="Submit", font=('Arial', 14), command=submit_text)
    submit_button.place(x=250,  y=270)

# Break system cmd

def open_confirmation2():
    if messagebox.askyesno("Adm_perm", "For this command to run you must grant admin permissions. Press yes to grant"):
        confirm()

def confirm():
    if messagebox.askyesno("Confirmation", "Are you sure you want to run this command? This command will delete important files and deleting them may cause VM to break! Are you sure?"):
        break_system()

def break_system():
    root.config(bg="black")
    button_filex.destroy()
    button.destroy()
    button2.destroy()
    button6.destroy()
    button_cookie_clicker.destroy()
    button_notepad.destroy()
    button_Sett.destroy()
    button_SIfolder.destroy()
    button_SM.destroy()
    label_break.place(x=100, y=100)
    label_breakin.place(x=0, y=450)
    label_breakin2.place(x=0, y=489)

# SI folder function

def open_success():
    success = tk.Toplevel()
    success.title("SI")
    success.geometry("800x400")
    success.config(bg="black")
    center_window(success, 900, 400)

    label10 = tk.Label(success, text="Python; High_Level<<>> |n  {C}  Prog== VM__//sys_Vm{OS}", font=("Arial", 25))
    label10.config(fg="green", bg="black")
    label10.pack(expand=True)


def open_SIfolder():
    SIfolder = tk.Toplevel()
    SIfolder.title("SI Folder")
    SIfolder.geometry("600x400")
    SIfolder.config(bg="gray")
    center_window(SIfolder, 600, 400)
    
    entry_box = tk.Entry(SIfolder, font=("Arial", 24))
    entry_box.place(x=120, y=100)

    error_label = tk.Label(SIfolder, text="", font=("Arial", 14), bg="gray", fg="red")
    error_label.place(x=215, y=200)

    def submit_password():
        entered_text = entry_box.get().strip()
        
        if entered_text == "!@#$%terabyte":
            open_success() 
        else:
            error_label.config(text="Invalid Password")

    submit_button = tk.Button(SIfolder, text="Submit", font=("Arial", 14), command=submit_password)
    submit_button.place(x=250, y=150)

# Timer (do not touch)

def play_music(window):
    global time_in_ms, timer_id
    
    time_in_ms = 0
    label8 = window.winfo_children()[1]  
    
    if timer_id is not None:
        window.after_cancel(timer_id)
    
    update_time(label8, time_in_ms, window)

def stop_music(window):
    global time_in_ms, timer_id
    
    if timer_id is not None:
        window.after_cancel(timer_id)
    
    time_in_ms = 0
    label8 = window.winfo_children()[1]  
    label8.config(text="0:00:00")  

def update_time(label, time_in_ms, window):
    global timer_id
    
    minutes = (time_in_ms // 1000) // 60
    seconds = (time_in_ms // 1000) % 60
    milliseconds = time_in_ms % 1000
    
    if milliseconds == 0:
        time_str = f"{minutes}:{seconds:02d}"
    else:
        time_str = f"{minutes}:{seconds:02d}.{milliseconds:02d}"
    label.config(text=time_str)

    timer_id = window.after(10, update_time, label, time_in_ms + 10, window)

def toggle_fullscreen(event, window):
    is_fullscreen = window.attributes("-fullscreen")
    window.attributes("-fullscreen", not is_fullscreen)

# Settings

def open_Sett():
    sett = tk.Toplevel()
    sett.title("Settings")
    sett.geometry("600x400")
    center_window(sett, 600, 400)

    button_bg = tk.Button(sett, text="Background", font=("Arial", 24), command=open_bgcol)
    button_bg.place(x=20, y=20)

    button_wbg = tk.Button(sett, text="Button Customization", font=("Arial", 24), command=open_butcus)
    button_wbg.place(x=20, y=100)

    button_vm = tk.Button(sett, text="VM Customization", font=("Arial", 24), command=open_vmcus)
    button_vm.place(x=20, y=180)

# VM Customization

def open_vmcus():
    vmcus = tk.Toplevel()
    vmcus.title("VM Customization")
    vmcus.geometry("600x400")
    center_window(vmcus, 600, 400)

    button_full = tk.Button(vmcus, text="Fullscreen mode", font=("Arial", 24), command=switch_butt)
    button_full.place(x=20, y=20)

    button_defull = tk.Button(vmcus, text="Default", font=("Arial", 24), command=switch_defull)
    button_defull.place(x=20, y=100)

def switch_butt():
    button_Sett.place(x=1750, y=20)
    button_SM.place(x=1830, y=950)
    button_filex.place(x=1692, y=140)

def switch_defull():
    button_Sett.place(x=840, y=20)
    button_SM.place(x=900, y=620)
    button_filex.place(x=783, y=140)

# Button customization

def open_butcus():
    butcus = tk.Toplevel()
    butcus.title("Button Customization")
    butcus.geometry("700x400")
    center_window(butcus, 700, 400)

    label_syst = tk.Label(butcus, text="Select what color you want to your buttons to be", font=("Arial", 24))
    label_syst.pack()

    button_red = tk.Button(butcus, text="Red", font=("Arial", 24), command=change_bgred2)
    button_red.place(x=130, y=100)

    button_orange = tk.Button(butcus, text="Orange", font=("Arial", 24), command=change_bgorange2)
    button_orange.place(x=250, y=100)

    button_yellow = tk.Button(butcus, text="Yellow", font=("Arial", 24), command=change_bgyellow2)
    button_yellow.place(x=420, y=100)

    button_green = tk.Button(butcus, text="Green", font=("Arial", 24), command=change_bggreen2)
    button_green.place(x=130, y=200)

    button_cyan = tk.Button(butcus, text="Cyan", font=("Arial", 24), command=change_bgcyan2)
    button_cyan.place(x=280, y=200)

    button_blue = tk.Button(butcus, text="Blue", font=("Arial", 24), command=change_bgblue2)
    button_blue.place(x=420, y=200)

    button_purple = tk.Button(butcus, text="Purple", font=("Arial", 24), command=change_bgpurple2)
    button_purple.place(x=200, y=300)

    button_pink = tk.Button(butcus, text="Pink", font=("Arial", 24), command=change_bgpink2)
    button_pink.place(x=350, y=300)

def change_bgred2():
    button.config(bg="red")
    button2.config(bg="red")
    button6.config(bg="red")
    button6.config(bg="red")
    button_cookie_clicker.config(bg="red")
    button_notepad.config(bg="red")
    button_Sett.config(bg="red")
    button_SM.config(bg="red")
    button_SIfolder.config(bg="red")

def change_bgorange2():
    button.config(bg="orange")
    button2.config(bg="orange")
    button6.config(bg="orange")
    button6.config(bg="orange")
    button_cookie_clicker.config(bg="orange")
    button_notepad.config(bg="orange")
    button_Sett.config(bg="orange")
    button_SM.config(bg="orange")
    button_SIfolder.config(bg="orange")

def change_bgyellow2():
    button.config(bg="yellow")
    button2.config(bg="yellow")
    button6.config(bg="yellow")
    button6.config(bg="yellow")
    button_cookie_clicker.config(bg="yellow")
    button_notepad.config(bg="yellow")
    button_Sett.config(bg="yellow")
    button_SM.config(bg="yellow")
    button_SIfolder.config(bg="yellow")

def change_bggreen2():
    button.config(bg="green")
    button2.config(bg="green")
    button6.config(bg="green")
    button6.config(bg="green")
    button_cookie_clicker.config(bg="green")
    button_notepad.config(bg="green")
    button_Sett.config(bg="green")
    button_SM.config(bg="green")
    button_SIfolder.config(bg="green")

def change_bgcyan2():
    button.config(bg="cyan")
    button2.config(bg="cyan")
    button6.config(bg="cyan")
    button6.config(bg="cyan")
    button_cookie_clicker.config(bg="cyan")
    button_notepad.config(bg="cyan")
    button_Sett.config(bg="cyan")
    button_SM.config(bg="cyan")
    button_SIfolder.config(bg="cyan")

def change_bgblue2():
    button.config(bg="blue")
    button2.config(bg="blue")
    button6.config(bg="blue")
    button6.config(bg="blue")
    button_cookie_clicker.config(bg="blue")
    button_notepad.config(bg="blue")
    button_Sett.config(bg="blue")
    button_SM.config(bg="blue")
    button_SIfolder.config(bg="blue")
    
def change_bgpurple2():
    button.config(bg="#A020F0")
    button2.config(bg="#A020F0")
    button6.config(bg="#A020F0")
    button6.config(bg="#A020F0")
    button_cookie_clicker.config(bg="#A020F0")
    button_notepad.config(bg="#A020F0")
    button_Sett.config(bg="#A020F0")
    button_SM.config(bg="#A020F0")
    button_SIfolder.config(bg="#A020F0")

def change_bgpink2():
    button.config(bg="#FF69B4")
    button2.config(bg="#FF69B4")
    button6.config(bg="#FF69B4")
    button6.config(bg="#FF69B4")
    button_cookie_clicker.config(bg="#FF69B4")
    button_notepad.config(bg="#FF69B4")
    button_Sett.config(bg="#FF69B4")
    button_SM.config(bg="#FF69B4")
    button_SIfolder.config(bg="#FF69B4")

# BG color customization

def open_bgcol():
    bgcol = tk.Toplevel()
    bgcol.title("Background Customization")
    bgcol.geometry("650x400")
    center_window(bgcol, 650, 400)

    labelbgcol = tk.Label(bgcol, text="Select what color you want your background to be", font=("Arial", 20))
    labelbgcol.pack()

    button_red = tk.Button(bgcol, text="Red", font=("Arial", 24), command=change_bgred)
    button_red.place(x=130, y=100)

    button_orange = tk.Button(bgcol, text="Orange", font=("Arial", 24), command=change_bgorange)
    button_orange.place(x=250, y=100)

    button_yellow = tk.Button(bgcol, text="Yellow", font=("Arial", 24), command=change_bgyellow)
    button_yellow.place(x=420, y=100)

    button_green = tk.Button(bgcol, text="Green", font=("Arial", 24), command=change_bggreen)
    button_green.place(x=130, y=200)

    button_cyan = tk.Button(bgcol, text="Cyan", font=("Arial", 24), command=change_bgcyan)
    button_cyan.place(x=280, y=200)

    button_blue = tk.Button(bgcol, text="Blue", font=("Arial", 24), command=change_bgblue)
    button_blue.place(x=420, y=200)

    button_purple = tk.Button(bgcol, text="Purple", font=("Arial", 24), command=change_bgpurple)
    button_purple.place(x=200, y=300)

    button_pink = tk.Button(bgcol, text="Pink", font=("Arial", 24), command=change_bgpink)
    button_pink.place(x=350, y=300)

    button_defaultcol = tk.Button(bgcol, text="Default", font=("Arial", 10), command=change_bgdef)
    button_defaultcol.place(x=300, y=50)

def change_bgred():
    root.config(bg="red")

def change_bgorange():
    root.config(bg="orange")

def change_bgyellow():
    root.config(bg="yellow")

def change_bggreen():
    root.config(bg="#00FF00")

def change_bgcyan():
    root.config(bg="cyan")

def change_bgblue():
    root.config(bg="blue")
    
def change_bgpurple():
    root.config(bg="#A020F0")

def change_bgpink():
    root.config(bg="#FF69B4")

def change_bgdef():
    root.config(bg="lightblue")

# Start menu

def open_SM():
    SM = tk.Toplevel()
    SM.title("Start Menu")
    SM.geometry("600x400")
    SM.config(bg="gray")
    center_window(SM, 600, 400)


    button_search = tk.Button(SM, text="🔍", font=("Arial", 24), command=open_search)
    button_search.place(x=20, y=320)

    button_shut = tk.Button(SM, text="Shut down", font=("Arial", 24), command=shut_down)
    button_shut.place(x=20, y=20)

    button_shut = tk.Button(SM, text="Delete Programs", font=("Arial", 24), command=delete_box)
    button_shut.place(x=20, y=120)

# Search function

def check_text():
    search_input = search_box.get().lower()
    if search_input == "system":
        open_search_win()
    if search_input == "downloader":
        open_search_win2()
    if search_input == "stopwatch":
        open_search_win3()
    if search_input == "cookie clicker":
        open_search_win4()
    if search_input == "notepad":
        open_search_win5()
    if search_input == "si folder":
        open_search_win6()
    if search_input == "settings":
        open_search_win7()
    
# Search box

def open_search():
    global search_box
    search = tk.Toplevel()
    search.title("Search box")
    search.geometry("600x400")
    center_window(search, 600, 400)

    search_box = tk.Entry(search, font=("Arial", 24))
    search_box.place(x=120, y=120)

    search_butt = tk.Button(search, text="Search", font=("Arial", 24), command=check_text)
    search_butt.place(x=220, y=200)

def open_search_win():
    search_win = tk.Toplevel()
    search_win.title("Result")
    search_win.geometry("600x400")
    center_window(search_win, 600, 400)

    label_result = tk.Label(search_win, text="Your result: ", font=("Arial", 30))
    label_result.pack()

    button_searchsys = tk.Button(search_win, text="System", font=("Arial", 24), command=open_new_window)
    button_searchsys.place(x=220, y=150)

def open_search_win2():
    search_win2 = tk.Toplevel()
    search_win2.title("Result")
    search_win2.geometry("600x400")
    center_window(search_win2, 600, 400)

    label_result = tk.Label(search_win2, text="Your result: ", font=("Arial", 30))
    label_result.pack()

    button_searchsys = tk.Button(search_win2, text="Downloader", font=("Arial", 24), command=open_new_window2)
    button_searchsys.place(x=200, y=150)

def open_search_win3():
    search_win3 = tk.Toplevel()
    search_win3.title("Result")
    search_win3.geometry("600x400")
    center_window(search_win3, 600, 400)

    label_result = tk.Label(search_win3, text="Your result: ", font=("Arial", 30))
    label_result.pack()

    button_searchsys = tk.Button(search_win3, text="Stopwatch", font=("Arial", 24), command=open_new_window4)
    button_searchsys.place(x=200, y=150)

def open_search_win4():
    search_win4 = tk.Toplevel()
    search_win4.title("Result")
    search_win4.geometry("600x400")
    center_window(search_win4, 600, 400)

    label_result = tk.Label(search_win4, text="Your result: ", font=("Arial", 30))
    label_result.pack()

    button_searchsys = tk.Button(search_win4, text="Cookie Clicker", font=("Arial", 24), command=open_cookie_clicker)
    button_searchsys.place(x=185, y=150)

def open_search_win5():
    search_win5 = tk.Toplevel()
    search_win5.title("Result")
    search_win5.geometry("600x400")
    center_window(search_win5, 600, 400)

    label_result = tk.Label(search_win5, text="Your result: ", font=("Arial", 30))
    label_result.pack()

    button_searchsys = tk.Button(search_win5, text="Notepad", font=("Arial", 24), command=open_notepad)
    button_searchsys.place(x=210, y=150)

def open_search_win6():
    search_win6 = tk.Toplevel()
    search_win6.title("Result")
    search_win6.geometry("600x400")
    center_window(search_win6, 600, 400)

    label_result = tk.Label(search_win6, text="Your result: ", font=("Arial", 30))
    label_result.pack()

    button_searchsys = tk.Button(search_win6, text = "SI Folder", font=("Arial", 24), command=open_SIfolder)
    button_searchsys.place(x=200, y=150)

def open_search_win7():
    search_win7 = tk.Toplevel()
    search_win7.title("Result")
    search_win7.geometry("600x400")
    center_window(search_win7, 600, 400)

    label_result = tk.Label(search_win7, text="Your result: ", font=("Arial", 30))
    label_result.pack()

    button_searchsys = tk.Button(search_win7, text = "Settings", font=("Arial", 24), command=open_Sett)
    button_searchsys.place(x=210, y=150)

def shut_down():
    root.destroy()

# Delete app function

def delete_box():
    delbox = tk.Toplevel()
    delbox.title('Delete Menu')
    delbox.geometry("600x400")
    center_window(delbox, 600, 400)

    button_sys = tk.Button(delbox, text="System", font=("Arial", 24), command=delete_sys)
    button_sys.place(x=20, y=20)
    
    button_dow = tk.Button(delbox, text="Downloader", font=("Arial", 24), command=delete_dow)
    button_dow.place(x=20, y=100)

    button_stp = tk.Button(delbox, text="Stopwatch", font=("Arial", 24), command=delete_stp)
    button_stp.place(x=20, y=180)

    button_coc = tk.Button(delbox, text="Cookie clicker", font=("Arial", 24), command=delete_coc)
    button_coc.place(x=20, y=260)

    button_not = tk.Button(delbox, text="Notepad", font=("Arial", 24), command=delete_not)
    button_not.place(x=20, y=340)

    button_SIfolder = tk.Button(delbox, text="SI Folder", font=("Arial", 24), command=delete_sif)
    button_SIfolder.place(x=430, y=20)

# File explorer

def open_file_ex():
    files = tk.Toplevel()
    files.title("File Explorer")
    files.geometry("600x400")
    center_window(files, 600, 400)

    button_doc = tk.Button(files, text="Documents", font=("Arial", 24), command=open_docs)
    button_doc.place(x=20, y=50)

    button_pic = tk.Button(files, text="Pictures", font=("Arial", 24), command=open_pics)
    button_pic.place(x=250, y=50)

    button_mus = tk.Button(files, text="Music", font=("Arial", 24), command=open_music)
    button_mus.place(x=430, y=50)

    button_app = tk.Button(files, text="Apps", font=("Arial", 24), command=open_apps)
    button_app.place(x=150, y=150)

    button_game = tk.Button(files, text="Games", font=("Arial", 24), command=open_games)
    button_game.place(x=300, y=150)

    label_storage = tk.Label(files, text="{ |||||            }  Memory used", font=("Arial", 24))
    label_storage.place(x=150, y=300)

def open_games():
    games = tk.Toplevel()
    games.title("Games")
    games.geometry("600x400")
    center_window(games, 600, 400)

def open_apps():
    apps = tk.Toplevel()
    apps.title("Apps")
    apps.geometry("600x400")
    center_window(apps, 600, 400)

def open_music():
    music = tk.Toplevel()
    music.title("Music")
    music.geometry("600x400")
    center_window(music, 600, 400)

def open_docs():
    docs = tk.Toplevel()
    docs.title("Documents")
    docs.geometry("600x420")
    center_window(docs, 600, 420)

    doc1 = tk.Button(docs, text="Document 1", font=("Arial", 24), command=open_doc1)
    doc1.place(x=20, y=20)

    doc2 = tk.Button(docs, text="Document 2", font=("Arial", 24), command=open_doc2)
    doc2.place(x=20, y=100)

    doc3 = tk.Button(docs, text="Document 3", font=("Arial", 24), command=open_doc3)
    doc3.place(x=20, y=180)

    doc4 = tk.Button(docs, text="Document 4", font=("Arial", 24), command=open_doc4)
    doc4.place(x=20, y=260)

    doc5 = tk.Button(docs, text="Document 5", font=("Arial", 24), command=open_doc5)
    doc5.place(x=20, y=340)

def open_doc1():
    doc1 = tk.Toplevel()
    doc1.title("Document 1")
    doc1.geometry("600x400")
    center_window(doc1, 600, 400)

    label_doc1 = tk.Label(doc1, text="", font=("Arial", 15))
    label_doc1.place(x=20, y=20)

def open_doc2():
    doc2 = tk.Toplevel()
    doc2.title("Document 2")
    doc2.geometry("600x400")
    center_window(doc2, 600, 400)

    label_doc2 = tk.Label(doc2, text="", font=("Arial", 15))
    label_doc2.place(x=20, y=20)

def open_doc3():
    doc3 = tk.Toplevel()
    doc3.title("Document 3")
    doc3.geometry("600x400")
    center_window(doc3, 600, 400)

    label_doc3 = tk.Label(doc3, text="", font=("Arial", 15))
    label_doc3.place(x=20, y=20)

def open_doc4():
    doc4 = tk.Toplevel()
    doc4.title("Document 4")
    doc4.geometry("600x400")
    center_window(doc4, 600, 400)

    label_doc4 = tk.Label(doc4, text="", font=("Arial", 15))
    label_doc4.place(x=20, y=20)

def open_doc5():
    doc5 = tk.Toplevel()
    doc5.title("Document 5")
    doc5.geometry("600x400")
    center_window(doc5, 600, 400)

    label_doc5 = tk.Label(doc5, text="", font=("Arial", 15))
    label_doc5.place(x=20, y=20)

def open_pics():
    pics = tk.Toplevel()
    pics.title("Pictures")
    pics.geometry("600x400")
    center_window(pics, 600, 400)


# Delete apps

def delete_sif():
    response6 = messagebox.askyesno("Confirmation", "Are you sure? (THIS PROCESS CANNOT BE UNDONE)")
    
    if response6:
        on_yes6()

def on_yes6():
    button_SIfolder.destroy()

def delete_not():
    response5 = messagebox.askyesno("Confirmation", "Are you sure? (THIS PROCESS CANNOT BE UNDONE)")
    
    if response5:
        on_yes5()

def on_yes5():
    button_notepad.destroy()

def delete_coc():
    response4 = messagebox.askyesno("Confirmation", "Are you sure? (THIS PROCESS CANNOT BE UNDONE)")
    
    if response4:
        on_yes4()

def on_yes4():
    button_cookie_clicker.destroy()

def delete_stp():
    response3 = messagebox.askyesno("Confirmation", "Are you sure? (THIS PROCESS CANNOT BE UNDONE)")
    
    if response3:
        on_yes3()

def on_yes3():
    button6.destroy()

def delete_dow():
    response2 = messagebox.askyesno("Confirmation", "Are you sure? (THIS PROCESS CANNOT BE UNDONE)")
    
    if response2:
        on_yes2()

def on_yes2():
    button2.destroy()

def delete_sys():
    response = messagebox.askyesno("Confirmation", "Are you sure? (THIS PROCESS CANNOT BE UNDONE)")
    
    if response:
        on_yes()

def on_yes():
    button.destroy()

# Center window function (do not touch)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - height / 2)
    position_left = int(screen_width / 2 - width / 2)
    window.geometry(f'{width}x{height}+{position_left}+{position_top}')

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Root

root = tk.Tk()
root.title("VM")
root.config(bg="lightblue")


window_width = 1000
window_height = 700
center_window(root, window_width, window_height)

# Root app buttons

button = tk.Button(root, text="System", font=("Arial", 24), command=open_new_window)
button.place(x=20, y=20)

button2 = tk.Button(root, text="Downloader", font=("Arial", 24), command=open_new_window2)
button2.place(x=20, y=140)

button6 = tk.Button(root, text="Stopwatch", font=("Arial", 24), command=open_new_window4)
button6.place(x=20, y=260)

button_cookie_clicker = tk.Button(root, text="Cookie Clicker", font=("Arial", 24), command=open_cookie_clicker)
button_cookie_clicker.place(x=20, y=380)

button_notepad = tk.Button(root, text="Notepad", font=("Arial", 24), command=open_notepad)
button_notepad.place(x=20, y=500)

button_SIfolder = tk.Button(root, text="SI Folder", font=("Arial", 24), command=open_SIfolder)
button_SIfolder.place(x=20, y=620)

button_SM = tk.Button(root, text="SM", font=("Arial", 24), command=open_SM)
button_SM.place(x=900, y=620)

button_Sett = tk.Button(root, text="Settings", font=("Arial", 24), command=open_Sett)
button_Sett.place(x=840, y=20)

button_filex = tk.Button(root, text="File explorer", font=("Arial", 24), command=open_file_ex)
button_filex.place(x=783, y=140)

label_break = tk.Label(root, text=":(", font=("Arial", 150))
label_break.config(bg="black", fg="green")
#label_break.place(x=100, y=100)

label_breakin = tk.Label(root, text="VM has run into some problems! It cannot boot due to important files missing!", font=("Arial", 22), fg="green", bg="black")
label_breakin.config(bg="black", fg="green")
#label_breakin.place(x=0, y=450)

label_breakin2 = tk.Label(root, text="The files cannot be recovered. You will need to reinstall VM so it can work again.", font=("Arial", 20), fg="green", bg="black")
label_breakin2.config(bg="black", fg="green")
#label_breakin2.place(x=0, y=489)


root.mainloop()