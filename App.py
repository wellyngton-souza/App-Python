import customtkinter
from tkinter import *

#aplicação Musica
import Music

#Theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#janela
window = customtkinter.CTk()
window.geometry("700x400")
window.title("App")
window.resizable(False, False)

#imagem
img = PhotoImage(file="./assets/pato.gif")
label_img = customtkinter.CTkLabel(master=window, image=img)
label_img.place(x=0, y=0)

#box
box = customtkinter.CTkFrame(master=window, width=200, height=400)
box.place(x=500, y=0)

#texto
label = customtkinter.CTkLabel(master=box, text="Titulo")
label.place(x=40, y=20)

#textBox
entry1 = customtkinter.CTkEntry(master=box, placeholder_text="TextBox", width=150).place(x=25, y=55)

#botao que referencia a musica
music_label = customtkinter.CTkLabel(master=box, text="music Player")
music_label.place(x=40, y=170)
play_button = Button(window, text="Clique Aqui", command=Music.tocarTudo)
play_button.place(x=550, y=200)

window.mainloop()