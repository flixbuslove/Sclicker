import tkinter as tk

okno = tk.Tk()
okno.title("SClicker")
okno.geometry("300x300")

ilosc_klikniec = 0
poziom = 0
dodawane_klik = 1



iloscklikniec_label = tk.Label(okno, text=ilosc_klikniec)
iloscklikniec_label.pack()


def ending(ktory):
    global iloscklikniec_label
    global kliknij
    global ulepszbutton
    if ktory == "za duzo":
        kliknij.pack_forget()
        ulepszbutton.pack_forget()
        iloscklikniec_label.pack_forget()
        ending_zaduzo = tk.Label(okno,text="ENDING \n ZA DUŻO \n nie musisz tyle klikać \n Dzięki za gre :) \n oceń na githubie pls", font="Arial" "Bold", )
        ending_zaduzo.pack()
    if ktory == "WOW":
        kliknij.pack_forget()
        ulepszbutton.pack_forget()
        iloscklikniec_label.pack_forget()
        ending_wow = tk.Label(okno,text="ENDING \n WOW \n przeszedłeś całą GRE! \n gratulacje czy coś \n Dzięki za gre :) \n oceń na githubie pls", font="Arial" "Bold", )
        ending_wow.pack()
    if ktory == "1 poziom serio":
        kliknij.pack_forget()
        ulepszbutton.pack_forget()
        iloscklikniec_label.pack_forget()
        ending_1poziomserio = tk.Label(okno,text="ENDING \n 1 poziom SERIO? \n przeszedłeś całą GRE! \n gratulacje czy coś \n Dzięki za gre :) \n oceń na githubie pls", font="Arial" "Bold", )
        ending_1poziomserio.pack()
    




def dodajklikniecie():
    global ilosc_klikniec
    if ilosc_klikniec >= 99999:
        ending("za duzo")

    if poziom == 6:
        if ilosc_klikniec >= 0:
            ending("WOW")
        else:
            ilosc_klikniec += dodawane_klik
            iloscklikniec_label.config(text=ilosc_klikniec)
    if poziom == 0:
        if ilosc_klikniec >= 150:
            ending("1 poziom serio")
        else:
            ilosc_klikniec += dodawane_klik
            iloscklikniec_label.config(text=ilosc_klikniec)

    else:    

        ilosc_klikniec += dodawane_klik
        iloscklikniec_label.config(text=ilosc_klikniec)

def ref():
    iloscklikniec_label.config(text=ilosc_klikniec)

def napij_sie_wody():
    global kliknij
    global ilosc_klikniec
    napij_sie_wody_okno = tk.Tk()
    napij_sie_wody_okno.title("NAPIJ SIĘ WODY")
    ilosc_klikniec = -1000
    kliknij.config(command=dodajklikniecie)


def niezadlugo():
    global ilosc_klikniec
    global kliknij
    niezadlugo_okno = tk.Tk()
    niezadlugo_okno.title("nie za długi klikasz????")
    label = tk.Label(niezadlugo_okno,text="nie za długo klikasz???? \n NA ZNIECHETE USUNIEMY CI 5000 KLIKNIĘĆ :)")
    label.pack()
    ilosc_klikniec -= 5000
    kliknij.config(command=dodajklikniecie)
def utrudnienie():
    global ilosc_klikniec
    ilosc_klikniec = -150
    ref()
    kliknij.config(command=dodajklikniecie)



def reklama():
    
    global kliknij
    reklama_okno = tk.Tk()
    reklama_okno.geometry("300x300")
    reklama_okno.title("REKLAMA")
    jakis_label = tk.Label(reklama_okno,text="REKLAMA \n reklama")
    jakis_label.pack()
    kliknij.config(command=dodajklikniecie)


def ulepsz():
    global sprawdz_ending
    global kliknij
    global ulepszbutton
    global ilosc_klikniec
    global poziom
    global dodawane_klik
    if poziom == 0:
        if ilosc_klikniec >= 10:
            ilosc_klikniec -= 10
            ref()
            dodawane_klik = 2
            ulepszbutton.config(text="ulepsz (100 kliknięć)")
            poziom += 1
            print(poziom)
    elif poziom == 1:
        if ilosc_klikniec >= 100:
            ilosc_klikniec -= 100
            ref()
            dodawane_klik = 4
            ulepszbutton.config(text="ulepsz (500 kliknięć)")
            kliknij.config(command=reklama)
            poziom += 1
            print(poziom)
    elif poziom == 2:
        if ilosc_klikniec >= 500:
            ilosc_klikniec -= 500
            ref()
            dodawane_klik = 8
            ulepszbutton.config(text="ulepsz (1000 kliknięć)")

            
            poziom += 1
            print(poziom)
    elif poziom == 3:
         if ilosc_klikniec >= 1000:
            ilosc_klikniec -= 1000
            ref()
            dodawane_klik = 16
            ulepszbutton.config(text="ulepsz (5000 kliknięć)")
            kliknij.config(command=utrudnienie)
            poziom += 1
            print(poziom)
    elif poziom == 4:
         if ilosc_klikniec >= 5000:
            ilosc_klikniec -= 5000
            ref()
            dodawane_klik = 32
            ulepszbutton.config(text="ulepsz (10000 kliknięć)")
            kliknij.config(command=napij_sie_wody)
            poziom += 1
            print(poziom)
    elif poziom == 5:
         if ilosc_klikniec >= 10000:
            ilosc_klikniec -= 10000
            ref()
            dodawane_klik = 64
            ulepszbutton.config(text="ulepsz (20 000 kliknięć)")
            kliknij.config(command=niezadlugo)
            poziom += 1
            print(poziom)
    elif poziom == 6:
        
        if ilosc_klikniec >= 20000:
            dodawane_klik = 1
            
            ref()
        







kliknij = tk.Button(okno,text="KLIKNIJ MNIE", command=dodajklikniecie)
kliknij.pack()
ulepszbutton = tk.Button(okno,text="ulepsz (10 kliknięć)", command=ulepsz)
ulepszbutton.pack()

okno.mainloop() 
