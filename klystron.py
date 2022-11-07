#############################
## Klystron Interpolation  ##
## ©2022 Brian Walters     ##
## v 0.9                   ##
#############################

import customtkinter
from idlelib.tooltip import Hovertip
#from tkinter import messagebox

root = customtkinter.CTk()
root.title("Klystron Interpolation")
#root.geometry("450x250")
root.resizable(False, False)
winwidth = 450
winheight = 250
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
winx = int((screenwidth/2) - (winwidth/2))
winy = int((screenheight/2) - (winheight/2))
root.geometry("{}x{}+{}+{}".format(winwidth, winheight, winx, winy))

def interp():
    freqx = []
    freqy = []
    freqz = freqX.get()
    cavityinterp = []

    freqx.append(freqL.get())
    freqy.append(freqU.get())

    freqx.append(cavityL1.get())
    freqx.append(cavityL2.get())
    freqx.append(cavityL3.get())
    freqx.append(cavityL4.get())
    freqx.append(cavityL5.get())
    freqx.append(cavityL6.get())
    freqy.append(cavityU1.get())
    freqy.append(cavityU2.get())
    freqy.append(cavityU3.get())
    freqy.append(cavityU4.get())
    freqy.append(cavityU5.get())
    freqy.append(cavityU6.get())

    print(freqx, freqy, freqz)

    for i in range(1,7):
        p1 = (int(freqy[i]) - int(freqx[i]))
        p2 = (int(freqy[0]) - int(freqx[0]))
        p3 = (int(freqz) - int(freqx[0]))
        p4 = (p1/p2)*p3
        interp = (int(freqx[i])+p4)
        cavityinterp.append(round(interp, 1))

    print(cavityinterp)
        #print(interp)

    cavityX1.configure(placeholder_text=cavityinterp[0])
    cavityX2.configure(placeholder_text=cavityinterp[1])
    cavityX3.configure(placeholder_text=cavityinterp[2])
    cavityX4.configure(placeholder_text=cavityinterp[3])
    cavityX5.configure(placeholder_text=cavityinterp[4])
    cavityX6.configure(placeholder_text=cavityinterp[5])

copydate = "© 2022"
version = "v 1.1.0"
auth = "Brian Walters"

freqL = customtkinter.CTkEntry(master=root, width=120, placeholder_text="Lower Frequency")
freqU = customtkinter.CTkEntry(master=root, width=120,  placeholder_text="Upper Frequency")
freqX = customtkinter.CTkEntry(master=root, width=120,  placeholder_text="XMT Frequency")
cavityL1 = customtkinter.CTkEntry(master=root, width=40)
cavityL2 = customtkinter.CTkEntry(master=root, width=40)
cavityL3 = customtkinter.CTkEntry(master=root, width=40)
cavityL4 = customtkinter.CTkEntry(master=root, width=40)
cavityL5 = customtkinter.CTkEntry(master=root, width=40)
cavityL6 = customtkinter.CTkEntry(master=root, width=40)
cavityU1 = customtkinter.CTkEntry(master=root, width=40)
cavityU2 = customtkinter.CTkEntry(master=root, width=40)
cavityU3 = customtkinter.CTkEntry(master=root, width=40)
cavityU4 = customtkinter.CTkEntry(master=root, width=40)
cavityU5 = customtkinter.CTkEntry(master=root, width=40)
cavityU6 = customtkinter.CTkEntry(master=root, width=40)
cavityX1 = customtkinter.CTkEntry(master=root, width=40, fg_color="light green", placeholder_text_color="black")
cavityX2 = customtkinter.CTkEntry(master=root, width=40, fg_color="light green", placeholder_text_color="black")
cavityX3 = customtkinter.CTkEntry(master=root, width=40, fg_color="light green", placeholder_text_color="black")
cavityX4 = customtkinter.CTkEntry(master=root, width=40, fg_color="light green", placeholder_text_color="black")
cavityX5 = customtkinter.CTkEntry(master=root, width=40, fg_color="light green", placeholder_text_color="black")
cavityX6 = customtkinter.CTkEntry(master=root, width=40, fg_color="light green", placeholder_text_color="black")
interpbtn = customtkinter.CTkButton(master=root, text="Interpolate", command=interp)
exitbtn = customtkinter.CTkButton(master=root, text="Quit", command=root.destroy)
versionlabel = customtkinter.CTkLabel(master=root, text=version, width=30, text_font=("", 8))
copylabel = customtkinter.CTkLabel(master=root, text=copydate, width=30, text_font=("", 8))
authlabel = customtkinter.CTkLabel(master=root, text=auth, width=60, text_font=("", 8))

cavitylabel = customtkinter.CTkLabel(master=root, text="Cavity", width=120)
cavity1label = customtkinter.CTkLabel(master=root, text="1", width=40)
cavity2label = customtkinter.CTkLabel(master=root, text="2", width=40)
cavity3label = customtkinter.CTkLabel(master=root, text="3", width=40)
cavity4label = customtkinter.CTkLabel(master=root, text="4", width=40)
cavity5label = customtkinter.CTkLabel(master=root, text="5", width=40)
cavity6label = customtkinter.CTkLabel(master=root, text="6", width=40)

freqL.place(x=15, y=60)
freqU.place(x=15, y=100)
freqX.place(x=15, y=140)
cavityL1.place(x=145, y=60)
cavityL2.place(x=195, y=60)
cavityL3.place(x=245, y=60)
cavityL4.place(x=295, y=60)
cavityL5.place(x=345, y=60)
cavityL6.place(x=395, y=60)
cavityU1.place(x=145, y=100)
cavityU2.place(x=195, y=100)
cavityU3.place(x=245, y=100)
cavityU4.place(x=295, y=100)
cavityU5.place(x=345, y=100)
cavityU6.place(x=395, y=100)
cavityX1.place(x=145, y=140)
cavityX2.place(x=195, y=140)
cavityX3.place(x=245, y=140)
cavityX4.place(x=295, y=140)
cavityX5.place(x=345, y=140)
cavityX6.place(x=395, y=140)
cavitylabel.place(x=225, y=10)
cavity1label.place(x=145, y=30)
cavity2label.place(x=195, y=30)
cavity3label.place(x=245, y=30)
cavity4label.place(x=295, y=30)
cavity5label.place(x=345, y=30)
cavity6label.place(x=395, y=30)
interpbtn.place(x=50, y=190)
exitbtn.place(x=250, y=190)
versionlabel.place(x=160, y=220)
copylabel.place(x=200, y=220)
authlabel.place(x=250, y=220)

#tkinter.messagebox.showinfo(title="Klystron Interpolation", message="From the klystron datasheet, enter the frequency "
#                                                                    "& cavity tuning for the closest frequency below "
#                                                                    "and above your site frequency. The green boxes"
#                                                                    "will be calculated for your site frequency.")

freqLtip = Hovertip(freqL, 'Closest frequency lower than site frequecy.', hover_delay=250)
freqUtip = Hovertip(freqU, 'Closest frequency higher than site frequecy.', hover_delay=250)
freqXtip = Hovertip(freqX, 'Your site transmit frequency.', hover_delay=250)
cavityL1tip = Hovertip(cavityL1, 'Cavity 1 from datasheet.', hover_delay=250)
cavityL2tip = Hovertip(cavityL2, 'Cavity 2 from datasheet.', hover_delay=250)
cavityL3tip = Hovertip(cavityL3, 'Cavity 3 from datasheet.', hover_delay=250)
cavityL4tip = Hovertip(cavityL4, 'Cavity 4 from datasheet.', hover_delay=250)
cavityL5tip = Hovertip(cavityL5, 'Cavity 5 from datasheet.', hover_delay=250)
cavityL6tip = Hovertip(cavityL6, 'Cavity 6 from datasheet.', hover_delay=250)
cavityU1tip = Hovertip(cavityU1, 'Cavity 1 from datasheet.', hover_delay=250)
cavityU2tip = Hovertip(cavityU2, 'Cavity 2 from datasheet.', hover_delay=250)
cavityU3tip = Hovertip(cavityU3, 'Cavity 3 from datasheet.', hover_delay=250)
cavityU4tip = Hovertip(cavityU4, 'Cavity 4 from datasheet.', hover_delay=250)
cavityU5tip = Hovertip(cavityU5, 'Cavity 5 from datasheet.', hover_delay=250)
cavityU6tip = Hovertip(cavityU6, 'Cavity 6 from datasheet.', hover_delay=250)
cavityX1tip = Hovertip(cavityX1, 'Leave empty', hover_delay=250)
cavityX2tip = Hovertip(cavityX2, 'Leave empty', hover_delay=250)
cavityX3tip = Hovertip(cavityX3, 'Leave empty', hover_delay=250)
cavityX4tip = Hovertip(cavityX4, 'Leave empty', hover_delay=250)
cavityX5tip = Hovertip(cavityX5, 'Leave empty', hover_delay=250)
cavityX6tip = Hovertip(cavityX6, 'Leave empty', hover_delay=250)

interpbtntip = Hovertip(interpbtn, 'Click to interpolate.', hover_delay=250)
exitbtntip = Hovertip(exitbtn, 'Quit', hover_delay=250)

def main():
    root.mainloop()

if __name__ == '__main__':
    main()
