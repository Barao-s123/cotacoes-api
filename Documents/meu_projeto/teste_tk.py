import tkinter as tk

janela = tk.Tk()
janela.title("Teste Tkinter")
janela.geometry("300x150")
tk.Label(janela, text="Funcionou o Tkinter! 😄").pack(pady=40)
janela.mainloop()
