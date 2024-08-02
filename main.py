from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def sauvegarder():
    n = nom.get()
    p = prenom.get()
    a = adresse.get()
    b = birth.get()
    m = montant.get()
    g = genre.get()
    na = nationalite.get()
    n = n.strip()
    p = p.strip()
    a = a.strip()
    b = b.strip()

    if len(p) == 0:
        messagebox.showwarning(title='Erreur', message='Prénom obligatoire!')
        txtPrenom.focus()

    elif len(n) == 0:
        messagebox.showwarning(title='Erreur', message='Nom obligatoire!')
        txtNom.focus()

    elif len(a) == 0:
        messagebox.showwarning(title='Erreur', message='Adresse obligatoire!')
        txtAdresse.focus()

    elif len(b) == 0:
        messagebox.showwarning(title='Erreur', message='Date_anniverssaire obligatoire!')
        txtBirth.focus()

    elif m == 0 or m == "":
        messagebox.showwarning(title='Erreur', message='montant obligatoire!')
        txtmontant.focus()
    elif g == "":
        messagebox.showwarning(title='Erreur', message='genre obligatoire!')
        btnGenre.focus()
    elif na == "":
        messagebox.showwarning(title='Erreur', message='Nationalite obligatoire!')
        Nationalite.focus()
    else:
        with open('information.txt', 'a') as f:
            f.write(f'{n},{p},{a},{b},{m},{g},{na}\n')
        annuler()



def annuler():
    prenom.set('')
    nom.set('')
    adresse.set('')
    birth.set('')
    montant.set(0)
    nationalite.set('')
    genre.set('')
    txtPrenom.focus()


def lister():
    with open('information.txt', 'r') as f:
        liste_noms = f.readlines()
    listbox_widget.delete(0, END)
    for n in liste_noms:
        listbox_widget.insert(END, n.replace(',', ' '))


def button_radio(liste):
    for i in range(2):
        but_radio = Radiobutton(screen, text=liste[i])
        but_radio.grid(row=2, column=3, padx=5, sticky=E)


screen = Tk()
screen.title("Fiche d'info")
screen.geometry("750x400+50+50")
screen.resizable(width=False, height=False)
screen.config(background="#9DA0A4")




prenom = StringVar()
nom = StringVar()
adresse = StringVar()
birth = StringVar()
montant = DoubleVar()
nationalite = StringVar()
genre = StringVar()

# Last_name
lblPrenom = Label(screen, text="Prénom:", background="#9DA0A4")
lblPrenom.grid(row=0, column=0, pady=5, padx=5)
txtPrenom = Entry(screen, textvariable=prenom)
txtPrenom.grid(row=0, column=1, pady=5, padx=5)

# Name
lblNom = Label(screen, text="Nom:", background="#9DA0A4")
lblNom.grid(row=1, column=0, pady=5, padx=5)
txtNom = Entry(screen, textvariable=nom)
txtNom.grid(row=1, column=1, pady=5, padx=5)

# Birthday
lblBirth = Label(screen, text="Date de naissance:", background="#9DA0A4")
lblBirth.grid(row=2, column=0, pady=5, padx=5)
txtBirth = Entry(screen, textvariable=birth)
txtBirth.grid(row=2, column=1, pady=5, padx=5)

# Adresse
lblAdresse = Label(screen, text="Adresse:", background="#9DA0A4")
lblAdresse.grid(row=3, column=0, pady=5, padx=5)
txtAdresse = Entry(screen, textvariable=adresse)
txtAdresse.grid(row=3, column=1, pady=5, padx=5)

# Genre
btnGenre = Label(screen, text="Choisir votre genre:", background="#9DA0A4")
btnGenre.grid(row=0, column=2, pady=5, padx=5)
bntradio1 = Radiobutton(screen, text="Masculin", value="Masculin", variable=genre)
bntradio1.grid(row=1, column=2, pady=5, padx=5)
bntradio2 = Radiobutton(screen, text="Feminin", value="Feminin", variable=genre)
bntradio2.grid(row=1, column=3, pady=5, padx=5)

# Nationalité
lblNationalite = Label(screen,text="Nationalité:",background="#9DA0A4")
lblNationalite.grid(row=0, column=4,pady=5, padx=5)
Nationalite = ttk.Combobox(screen, values=["Haitien", "Etranger"], textvariable=nationalite)
Nationalite.current(1)
Nationalite.grid(row=0, column=5, pady=5, padx=5)

# Montant
lblmontant = Label(screen, text='Montant: ',background="#9DA0A4")
lblmontant.grid(row=2, column=2, sticky=E)
txtmontant = Entry(screen, textvariable=montant)
txtmontant.grid(row=2, column=3, pady=5, padx=5)

btnSauvegarder =Button(screen, text="Sauvegarder", command=sauvegarder,bg='#9DA0A4',fg='black')
btnSauvegarder.grid(row=5, column=1, pady=5, padx=5)

btnAnnuler = Button(screen, text="Annuler", command=annuler,bg='#9DA0A4',fg='black')
btnAnnuler.grid(row=5, column=2, pady=5, padx=5)

btnLire = Button(screen, text="Lire les données", command=lister,bg='#9DA0A4',fg='black')
btnLire.grid(row=5, column=3, pady=5, padx=5)

listbox_widget = Listbox(screen)
listbox_widget.grid(row=4, column=1, columnspan=5, sticky=EW,pady=5, padx=5)

txtPrenom.focus()


screen.mainloop()
