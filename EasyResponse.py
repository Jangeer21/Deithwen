from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import random
root = Tk()

root.geometry('800x650')
root.resizable(False,False)
root.title("AzInTicket")
root.wm_attributes('-alpha',0.9)
root['bg'] = '#70C1B3'
root.iconbitmap('.icon\\Icon3.ico')
#----------------------------------------------------------------------------------#
fill = StringVar()
fill2 = StringVar()
fill3 = StringVar()


photo = Image.open(".img\\Azin.png")
resized = photo.resize((170,170),Image.ANTIALIAS)
newpic = ImageTk.PhotoImage(resized)
photo_label = Label(image = newpic)
photo_label.place(x=630,y=0)

photo2 = Image.open(".img\\outlook.png")
resized22 = photo2.resize((50,50),Image.ANTIALIAS)
newpic22 = ImageTk.PhotoImage(resized22)
photo_label2 = Label(image = newpic22,bg = '#70C1B3')
photo_label2.place(x=530,y=160)

img = Image.open(".img\\copy2.png")
resized2 = img.resize((16,16),Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(resized2)

flag1 = Image.open(".img\\Eng.ico")
resizedf1 = flag1.resize((30,30),Image.ANTIALIAS)
flageng = ImageTk.PhotoImage(resizedf1)

flag2 = Image.open(".img\\Rus.ico")
resizedf2 = flag2.resize((30,30),Image.ANTIALIAS)
flagrus = ImageTk.PhotoImage(resizedf2)

flag3 = Image.open(".img\\Aze.ico")
resizedf3 = flag3.resize((30,30),Image.ANTIALIAS)
flagaze = ImageTk.PhotoImage(resizedf3)


#----------------------------------------------------------------------------------#
def Opent():
      output_box1.config(state='normal')
      output_box2.config(state='normal')
      output_box1.delete(0.0, 'end')
      output_box2.delete(0.0, 'end')
      ID = fill.get()
      Theme = fill2.get()
      lang = var_check.get()
      Subject = Theme + " // AzInTelecom Request [ID :##" + str(ID) + "##] ID" + str(ID)
      Service1 = ("Dear Colleagues, \n\n"
      "According to your request we have opened ticket ID" + str(ID) + ".\n"
      "Your request will be given priority.\n\n"
      "Thanks! \n\n"
      "Ticket number: ID" + str(ID) + "\n"  
      "Subject: " + Theme + "\n"
      "Status: Open \n")
      Service2 = ("Уважаемые Коллеги, \n\n"
      "По вашему запросу зарегистрирован тикет ID" + str(ID) + ". \n"
      "Вашему запросу будет присвоен приоритет.\n\n"
      "Спасибо! \n\n"
      "Ticket number: ID" + str(ID) + "\n"  
      "Subject: " + Theme + "\n"
      "Status: Open \n")
      Service3 = ("Hörmətli Həmkarlar, \n\n"
      "Sorğunuza əsasən biz tərəfdən ID" + str(ID) + " nömrəli ticket açılmışdır. \n"
      "Sizin Sorğuya Prioritet təyin olunacaq.\n\n"
      "Təşəkkür edirik! \n\n"
      "Ticket number: ID" + str(ID) + "\n"  
      "Subject: " + Theme + "\n"
      "Status: Open \n")
      if lang == 1:
          output_box1.insert(0.0,Subject)
          output_box2.insert(0.0,Service1)
      elif lang == 2:
          output_box1.insert(0.0, Subject)
          output_box2.insert(0.0, Service2)
      elif lang == 3:
          output_box1.insert(0.0, Subject)
          output_box2.insert(0.0, Service3)
      else: messagebox.askretrycancel("Attention!", "Do not forget to select language")
      if len(ID) == 0: messagebox.askretrycancel("Empty field", "Do not forget to enter ticket ID")
      if len(Theme) == 0: messagebox.askretrycancel("Empty field", "Do not forget to enter subject")
      output_box1.config(state='disabled')
      output_box2.config(state='disabled')


def Priority():
    output_box1.config(state='normal')
    output_box2.config(state='normal')
    output_box1.delete(0.0, 'end')
    output_box2.delete(0.0, 'end')
    Hours = fill3.get()
    ID = fill.get()
    Theme = fill2.get()
    lang = var_check.get()
    Hours = int(fill3.get())
    if Hours == 8: Level = "Urgent"
    elif Hours == 24: Level = "Average"
    elif Hours == 48: Level = "Normal"
    elif Hours == 72: Level = "Medium"
    elif Hours == 2: Level = "High"
    elif Hours == 1: Level = "Very High"
    elif Hours == 96: Level = "Medium Low"
    elif Hours == 120: Level = "Low"
    else: messagebox.showwarning("Warning","Wrong Priority")
    Subject = Theme + " // AzInTelecom Request [ID :##" + str(ID) + "##] ID" + str(ID)
    Service1 = ("Dear Colleagues, \n\n"
      "Your request will be processed within " + str(Hours) + " hours. \n"
      "Priority can be changed by you, given the severity of the request.\n\n"
      "Thanks for your understanding and co-operation! \n\n"
      "Priority: " + Level + "\n"
      "Response time: " + str(Hours) + " hours\n"
      "Ticket number: ID" + str(ID) + "\n"
      "Theme: " + Theme + "\n"
      "Status: Open \n")
    Service2 = ("Уважаемые Коллеги, \n\n"
      "Ваш запрос будет обработан в течение " + str(Hours) + " часов. \n"
      "Приоритет может быть изменен вами, учитывая серьезность запроса.\n\n"
      "Спасибо за ваше понимание и сотрудничество! \n\n"
      "Priority: " + Level + "\n"
      "Response time: " + str(Hours) + " hours\n"
      "Ticket number: ID" + str(ID) + "\n"
      "Theme: " + Theme + "\n"
      "Status: Open \n")
    Service3 = ("Hörmətli Həmkarlar, \n\n"
      "Sorğunuz " + str(Hours) + " saat ərzində cavablandırılacaq. \n"
      "Sorğunun ciddiliyi nəzərə alınaraq Prioritet siz tərəfdən dəyişdirilə bilər.\n\n"
      "Anlayışınız və əməkdaşlığınız üçün təşəkkür edirik! \n\n"
      "Priority: " + Level + "\n"
      "Response time: " + str(Hours) + " hours\n"
      "Ticket number: ID" + str(ID) + "\n"
      "Theme: " + Theme + "\n"
      "Status: Open \n")
    if lang == 1:
        output_box1.insert(0.0, Subject)
        output_box2.insert(0.0, Service1)
    elif lang == 2:
        output_box1.insert(0.0, Subject)
        output_box2.insert(0.0, Service2)
    elif lang == 3:
        output_box1.insert(0.0, Subject)
        output_box2.insert(0.0, Service3)
    else: messagebox.askretrycancel("Attention!","Do not forget to select language")
    if len(ID) == 0: messagebox.askretrycancel("Empty field", "Do not forget to enter ticket ID")
    if len(Theme) == 0: messagebox.askretrycancel("Empty field", "Do not forget to enter subject")
    output_box1.config(state='disabled')
    output_box2.config(state='disabled')


def Autoclose():
    output_box1.config(state='normal')
    output_box2.config(state='normal')
    output_box1.delete(0.0, 'end')
    output_box2.delete(0.0, 'end')
    ID = fill.get()
    Theme = fill2.get()
    lang = var_check.get()
    Subject = Theme + " // AzInTelecom Request [ID :##" + str(ID) + "##] ID" + str(ID)
    Service1 = ("Dear Colleagues, \n\n"
      "This message has been automatically sent. Please inform us about status of ticket.\n"
      "If we do not receive any response within the next 24 hours, the ticket will be closed.\n"
      "Please take into consideration.\n\n"
      "Thanks for your understanding and co-operation! \n\n"
      "Ticket number: ID" + str(ID) + "\n"  
      "Subject: " + Theme + "\n"
      "Status: Autoclose \n")
    Service2 = ("Уважаемые Коллеги, \n\n"
      "Это письмо отправлено автоматически. \n"
      "Пожалуйста сообщите нам о статусе тикета.\n"
      "В случае отсутствия ответа с вашей стороны, тикет будет закрыт в течении 24 часов.\n"
      "Пожалуйста, примите во внимание.\n\n"
      "Спасибо за ваше понимание и сотрудничество!\n\n"
      "Ticket number: ID" + str(ID) + "\n"  
      "Subject: " + Theme + "\n"
      "Status: Autoclose \n")
    Service3 = ("Hörmətli Həmkarlar, \n\n"
      "Bu məktub avtomatik göndərilib. \n"
      "Ticketin statusu barəsində məlumat verməyiniz xahiş olunur.\n"
      "24 saat ərzində bildiriş alınmadığı halda, ticket avtomatik olaraq bağlanacaqdır.\n"
      "Nəzərə almağınız xahiş olunur.\n\n"
      "Anlayışınız və əməkdaşlığınız üçün təşəkkür edirik!\n\n"
      "Ticket number: ID" + str(ID) + "\n"  
      "Subject: " + Theme + "\n"
      "Status: Autoclose \n")
    if lang == 1:
        output_box1.insert(0.0, Subject)
        output_box2.insert(0.0, Service1)
    elif lang == 2:
        output_box1.insert(0.0, Subject)
        output_box2.insert(0.0, Service2)
    elif lang == 3:
        output_box1.insert(0.0, Subject)
        output_box2.insert(0.0, Service3)
    else: messagebox.askretrycancel("Attention!", "Do not forget to select language")
    if len(ID) == 0: messagebox.askretrycancel("Empty field", "Do not forget to enter ticket ID")
    if len(Theme) == 0: messagebox.askretrycancel("Empty field", "Do not forget to enter subject")
    output_box1.config(state='disabled')
    output_box2.config(state='disabled')


def Update():
    output_box1.config(state='normal')
    output_box2.config(state='normal')
    output_box1.delete(0.0, 'end')
    output_box2.delete(0.0, 'end')
    ID = fill.get()
    Theme = fill2.get()
    lang = var_check.get()
    Subject = Theme + " // AzInTelecom Request [ID :##" + str(ID) + "##] ID" + str(ID)
    Service1 = ("Dear Colleagues, \n\n"
      "We put all our effort into resolving the reported issue.\n"
      "As soon as a new status update is available, we will contact you.\n"
      "Please take into consideration.\n\n"
      "Thanks for your understanding and co-operation! \n\n"
      "Ticket number: ID" + str(ID) + "\n"  
      "Subject: " + Theme + "\n"
      "Status: Reminder sent to Technical Support Team to speed up solution. \n")
    Service2 = ("Уважаемые Коллеги, \n\n"
      "Мы прилагаем все усилия, для того чтобы выполнить ваш запрос.\n"
      "Мы свяжемся с вами, как только появятся обновления.\n"
      "Пожалуйста, примите во внимание.\n\n"
      "Спасибо за ваше понимание и сотрудничество!\n\n"
      "Ticket number: ID" + str(ID) + "\n"  
      "Subject: " + Theme + "\n"
      "Status: Напоминание технической группе для ускорения работы.\n")
    Service3 = ("Hörmətli Həmkarlar, \n\n"
      "Bildirmək istərdik ki, sizin sorğunuzun icrası üzərində işlər aparılır. \n"
      "Hər hansı yenilənmə olarsa, sizə məlumat veriləcəkdir.\n"
      "Xahiş edirik nəzərə alasınız.\n\n"
      "Anlayışınız və əməkdaşlığınız üçün təşəkkür edirik!\n\n"
      "Ticket number: ID" + str(ID) + "\n"  
      "Subject: " + Theme + "\n"
      "Status: Texniki Dəstək qrupuna prosesi sürətləndirmək üçün xatırlatma göndərilmişdir. \n")
    if lang == 1:
        output_box1.insert(0.0, Subject)
        output_box2.insert(0.0, Service1)
    elif lang == 2:
        output_box1.insert(0.0, Subject)
        output_box2.insert(0.0, Service2)
    elif lang == 3:
        output_box1.insert(0.0, Subject)
        output_box2.insert(0.0, Service3)
    else: messagebox.askretrycancel("Attention!", "Do not forget to select language")
    if len(ID) == 0: messagebox.askretrycancel("Empty field", "Do not forget to enter ticket ID")
    if len(Theme) == 0: messagebox.askretrycancel("Empty field", "Do not forget to enter subject")
    output_box1.config(state='disabled')
    output_box2.config(state='disabled')


def Closed():
    output_box1.config(state='normal')
    output_box2.config(state='normal')
    output_box1.delete(0.0, 'end')
    output_box2.delete(0.0, 'end')
    ID = fill.get()
    Theme = fill2.get()
    lang = var_check.get()
    Subject = Theme + " // AzInTelecom Request [ID :##" + str(ID) + "##] ID" + str(ID)
    Service1 = ("Dear Colleagues, \n\n"
      "Thanks for your information.\n"
      "The ticket is closed.\n\n"
      "Thanks for your co-operation! \n\n"
      "Ticket number: ID" + str(ID) + "\n"  
      "Subject: " + Theme + "\n"
      "Status: Closed \n")
    Service2 = ("Уважаемые Коллеги, \n\n"
      "Спасибо за предоставленную информацию.\n"
      "Тикет был закрыт.\n\n"
      "Спасибо вам за сотрудничество!\n\n"
      "Ticket number: ID" + str(ID) + "\n"  
      "Subject: " + Theme + "\n"
      "Status: Closed\n")
    Service3 = ("Hörmətli Həmkarlar, \n\n"
      "Məlumat üçün təşəkkür edirik.\n"
      "Ticket bağlanmışdır.\n\n"
      "Əməkdaşlığınız üçün təşəkkür edirik!\n\n"
      "Ticket number: ID" + str(ID) + "\n"  
      "Subject: " + Theme + "\n"
      "Status: Closed\n")
    if lang == 1:
        output_box1.insert(0.0, Subject)
        output_box2.insert(0.0, Service1)
    elif lang == 2:
        output_box1.insert(0.0, Subject)
        output_box2.insert(0.0, Service2)
    elif lang == 3:
        output_box1.insert(0.0, Subject)
        output_box2.insert(0.0, Service3)
    else: messagebox.askretrycancel("Attention!", "Do not forget to select language")
    if len(ID) == 0: messagebox.askretrycancel("Empty field", "Do not forget to enter ticket ID")
    if len(Theme) == 0: messagebox.askretrycancel("Empty field", "Do not forget to enter subject")
    output_box1.config(state='disabled')
    output_box2.config(state='disabled')

def Copy1():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(output_box1.get(0.0,'end'))
    clip.destroy()

def Copy2():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(output_box2.get(0.0,'end'))
    clip.destroy()

def Status():
    output_box2.config(state = 'normal')
    output_box2.delete(0.0,'end')
    lang = var_check.get()
    Service1 = ("Dear All, \n\n"
                "Could you please inform us about ticket’s status?\n\n"
                "Thanks in advance.")
    Service2 = ("Уважаемые Коллеги, \n\n"
                "Просим вас сообщить о статусе заявки.\n\n"
                "Спасибо.")
    Service3 = ("Salam Hörmətli Həmkarlar, \n\n"
                "Xahiş edirik ticketin statusu barəsində məlumat verəsiniz.\n\n"
                "Təşəkkürlər.")
    if lang == 1: output_box2.insert(0.0,Service1)
    elif lang == 2: output_box2.insert(0.0,Service2)
    elif lang == 3: output_box2.insert(0.0,Service3)
    else: messagebox.askretrycancel("Attention!", "Do not forget to select language")
    output_box2.config(state = 'disabled')

def Reminder():
    output_box2.config(state='normal')
    output_box2.delete(0.0, 'end')
    lang = var_check.get()
    Service1 = ("Dear Colleagues, \n\n"
                "Kindly Reminder. \n\n"
                "Thanks in advance.")
    Service2 = ("Уважаемые Коллеги, \n\n"
                "Вежливое напоминание.\n\n"
                "Спасибо.")
    Service3 = ("Salam Hörmətli Həmkarlar, \n\n"
                "Xatırlatma məktubu.\n\n"
                "Təşəkkürlər.")
    if lang == 1: output_box2.insert(0.0, Service1)
    elif lang == 2: output_box2.insert(0.0, Service2)
    elif lang == 3: output_box2.insert(0.0, Service3)
    else: messagebox.askretrycancel("Attention!", "Do not forget to select language")
    output_box2.config(state='disabled')

def Updates():
    output_box2.config(state='normal')
    output_box2.delete(0.0, 'end')
    lang = var_check.get()
    Service1 = ("Dear Colleagues, \n\n"
                "Do you have any updates regarding this issue? \n\n"
                "Thanks in advance.")
    Service2 = ("Уважаемые Коллеги, \n\n"
                "Есть ли новости по данной заявке?\n\n"
                "Спасибо.")
    Service3 = ("Salam Hörmətli Həmkarlar, \n\n"
                "Sorğu ilə bağlı hər hansı bir yenilik varmı?\n\n"
                "Təşəkkürlər.")
    if lang == 1: output_box2.insert(0.0, Service1)
    elif lang == 2: output_box2.insert(0.0, Service2)
    elif lang == 3: output_box2.insert(0.0, Service3)
    else: messagebox.askretrycancel("Attention!", "Do not forget to select language")
    output_box2.config(state='disabled')

def Closing():
    output_box2.config(state='normal')
    output_box2.delete(0.0, 'end')
    lang = var_check.get()
    Service1 = ("Dear Colleagues, \n\n"
                "If you do not have additional questions please confirm closing TT.\n\n"
                "Thanks in advance.")
    Service2 = ("Уважаемые Коллеги, \n\n"
                "Если нет дополнительных вопросов, просим подтвердить закрытие тикета.\n\n"
                "Спасибо.")
    Service3 = ("Salam Hörmətli Həmkarlar, \n\n"
                "Qeyd olunan məsələ ilə bağlı əlavə sualınız yoxdursa, xahiş edirik ticketin bağlanmasını təsdiq edəsiniz.\n\n"
                "Təşəkkürlər.")
    if lang == 1: output_box2.insert(0.0, Service1)
    elif lang == 2: output_box2.insert(0.0, Service2)
    elif lang == 3: output_box2.insert(0.0, Service3)
    else: messagebox.askretrycancel("Attention!", "Do not forget to select language")
    output_box2.config(state='disabled')

def Support():
    output_box2.config(state='normal')
    output_box2.delete(0.0, 'end')
    IMS1 = ("Salam Hörmətli Həmkarlar,\n\n"
           "Xahiş edirik fikir bildirəsiniz.")
    IMS2 = ("Salam Hörmətli Həmkarlar,\n\n"
            "Xahiş edirik münasibət bildirəsiniz.")
    IMS3 = ("Salam Hörmətli Həmkarlar,\n\n"
            "Xahiş edirik dəstək göstərəsiniz.")
    IMS = [IMS1,IMS2,IMS3]
    output_box2.insert(0.0, random.choice(IMS))
    output_box2.config(state='disabled')

def Verify():
    output_box2.config(state='normal')
    output_box2.delete(0.0, 'end')
    lang = var_check.get()
    Service1 = ("Dear Colleagues, \n\n"
                "We would like to inform you that your request has been completed.\n"
                "Kindly ask you to check and inform us.\n\n"
                "Thanks in advance.")
    Service2 = ("Уважаемые Коллеги, \n\n"
                "Ваш запрос был выполнен.\n"
                "Просим проверить и сообщить нам.\n\n"
                "Спасибо.")
    Service3 = ("Salam Hörmətli Həmkarlar, \n\n"
                "Sizin sorğunuz icra olunmuşdur.\n"
                "Xahiş edirik yoxlayıb bizə məlumat verəsiniz.\n\n"
                "Təşəkkürlər.")
    if lang == 1: output_box2.insert(0.0, Service1)
    elif lang == 2: output_box2.insert(0.0, Service2)
    elif lang == 3: output_box2.insert(0.0, Service3)
    else: messagebox.askretrycancel("Attention!", "Do not forget to select language")
    output_box2.config(state='disabled')



#----------------------------------------------------------------------------------#
b1 = Button(root, text = "Open", font = 'Tahoma 12',width = 10, command = Opent, activeforeground = '#384D48',activebackground = '#CAFF8A')
b1.place(x = 10, y = 170)

b2 = Button(root, text = "Priority", font = 'Tahoma 12', width = 10, command = Priority, activeforeground = '#384D48',activebackground = '#CAFF8A')
b2.place(x = 110, y = 170)

b3 = Button(root, text = "Closure", font = 'Tahoma 12',width = 10, command = Autoclose, activeforeground = '#384D48',activebackground = '#CAFF8A')
b3.place(x = 210, y = 170)

b4 = Button(root, text = "Update", font = 'Tahoma 12',width = 10, command = Update, activeforeground = '#384D48',activebackground = '#CAFF8A')
b4.place(x = 310, y = 170)

b5 = Button(root, text = "Closed", font = 'Tahoma 12',width = 10, command = Closed, activeforeground = '#384D48',activebackground = '#CAFF8A')
b5.place(x = 410, y = 170)

var_check = IntVar()
b6 = Radiobutton(root, image = flageng, variable = var_check, value = 1,bg = '#70C1B3',activebackground = '#70C1B3' )
b6.place(x = 10, y = 110)

b7 = Radiobutton(root, image = flagrus, variable = var_check, value = 2,bg = '#70C1B3',activebackground = '#70C1B3')
b7.place(x = 110, y = 110)

b8 = Radiobutton(root, image = flagaze, variable = var_check, value = 3,bg = '#70C1B3',activebackground = '#70C1B3')
b8.place(x = 210, y = 110)

b9 = Button(root, text = 'Status', font = 'Tahoma 12', width = 10,activeforeground = '#323031',activebackground = '#e9c46a',command = Status)
b9.place(x = 650 , y = 270)

b10 = Button(root, text = 'Reminder', font = 'Tahoma 12', width = 10,activeforeground = '#323031',activebackground = '#e9c46a',command = Reminder)
b10.place(x = 650 , y = 303)

b11 = Button(root, text = 'Updates', font = 'Tahoma 12', width = 10,activeforeground = '#323031',activebackground = '#e9c46a',command = Updates)
b11.place(x = 650 , y = 336)

b12 = Button(root, text = 'Closing', font = 'Tahoma 12', width = 10,activeforeground = '#323031',activebackground = '#e9c46a',command = Closing)
b12.place(x = 650 , y = 369)

b13 = Button(root, text = 'Support', font = 'Tahoma 12', width = 10,activeforeground = '#323031',activebackground = '#e9c46a',command = Support)
b13.place(x = 650 , y = 402)

b14 = Button(root, text = 'Verify', font = 'Tahoma 12', width = 10,activeforeground = '#323031',activebackground = '#e9c46a',command = Verify)
b14.place(x = 650 , y = 435)

copy_button1 = Button(root,image = img2,command = Copy1,relief = 'flat',bg = '#70C1B3',activebackground = '#be95c4')
copy_button1.place(x = 575, y = 225)

copy_button2 = Button(root,image = img2, command = Copy2,bg = '#70C1B3',relief = 'flat',activebackground = '#be95c4')
copy_button2.place(x = 575, y = 270)
#----------------------------------------------------------------------------------#
#INPUT
n1 = Label(root, text = 'Ticket   :',width = 10,bg = '#70C1B3',font = "Georgia  14",fg = '#022b3a')
n1.place(x = 10 ,y = 10)
input_box1 = Entry(root,width = 60,background = "#CADBC8",textvariable = fill,relief = 'flat')
input_box1.place(x = 120, y = 17)
n2 = Label(root, text = 'Subject :',width = 10,bg = '#70C1B3',font = "Georgia  14",fg = '#022b3a')
n2.place(x = 10 ,y = 40)
input_box2 = Entry(root,width = 60, background = "#CADBC8",textvariable = fill2,relief = 'flat')
input_box2.place(x = 120, y = 47)
n4 = Label(root, text = 'Priority :',width = 10,bg = '#70C1B3',font = "Georgia  14",fg = '#022b3a')
n4.place(x = 10, y = 70 )
input_box3 = Entry(root,width = 60, background = "#CADBC8",textvariable = fill3,relief = 'flat')
input_box3.place(x = 120, y = 77)

#OUTPUT
output_box1 = Text(root, width = 80, height = 1, background = "#AEECEF",font = 'Calibri 11',relief = 'solid')
output_box1.place(x = 10 , y = 225)

output_box2 = Text(root, width = 80,height = 20, background = "#AEECEF",font = 'Calibri 11',relief = 'solid')
output_box2.place(x = 10 , y = 270)


root.mainloop()


