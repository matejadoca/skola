from tkinter import *
from tkinter.filedialog import *
import re
root = Tk()
lista=[]

    
def dodavanje():
    global lista
    lista.append(ime.get())
    lista.append(prezime.get())
    

    if select.get('active')=='Matematika':
        lista.append('Matematika,')
    elif select.get('active')=='Srpski':
        lista.append('Srpski, ')
    elif select.get('active')=='Programiranje':
        lista.append('Programiranje,')

    if var1.get()==1:
        lista.append('Onlajn')
    elif var1.get()==0:
        lista.append('Skola')
        
    Label(root, text='Ime '+lista[0]+", Prezime "+lista[1]+ " , Izborni Predmet " + lista[2]+ ", " + lista[3]).grid(row=7)
    
 

def open_callback():
    file = askopenfile(mode ='r', filetypes =[('Text Documents', '*.txt')]) 
    if file is not None: 
        content = file.read()
        wordList = re.sub("[^\w]", " ",  content).split()
    d='Ime '+wordList[0]+", Prezime "+wordList[1]+ " , Izborni Predmet " + wordList[2]+", "+wordList[3]

    Label(root, text=d).grid(row=7)
        



def saveas_callback(event=None):
    files = [   
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files) 
    if file is None:
        return
    text= ' '.join(lista)
    file.write(text)
    file.close()

        
ime=StringVar()
prezime=StringVar()

root.title('Forma')

Label(root, text='Ime', width=10).grid(row=1)
Label(root, text='Prezime', width=10).grid(row=2)

Entry(root, width=25,bg='lightgray',textvariable=str(ime)).grid(row=1, column=1 )
Entry(root, width=25,bg='lightgray',textvariable=str(prezime)).grid(row=2, column=1)


Label(root, text='Izaberite izborni predmet: ').grid(row=3, column=0)
select=Listbox(root, height=3)
select.insert(END, 'Matematika')
select.insert(END, 'Srpski')
select.insert(END, 'Programiranje')

select.grid(row=4, column=0)

var1 = IntVar()
Checkbutton(root, text="Stiklirajte ovo polje ako zelite da pratite onlajn nastavu: ", variable=var1).grid(row=5)


Button(root, width=10,command=dodavanje, text='Izaberi').grid(row=5, column=1)




menu = Menu()
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=open_callback)
file_menu.add_command(label='Save as', command=saveas_callback)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)



mainloop()
