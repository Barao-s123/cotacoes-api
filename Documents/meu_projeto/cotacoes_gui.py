try:
    import tkinter as tk
    from tkinter import messagebox
    import requests
    import matplotlib.pyplot as plt
    print("✅ Bibliotecas importadas com sucesso.")
except Exception as e:
    print("❌ Erro ao importar bibliotecas:", e)

cotacoes = {}

def buscar_cotacoes():
    print("🔍 Função buscar_cotacoes chamada")
    try:
        url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
        response = requests.get(url)
        data = response.json()
        print("✅ Dados recebidos:", data)

        dolar = float(data['USDBRL']['bid'])
        euro = float(data['EURBRL']['bid'])
        bitcoin = float(data['BTCBRL']['bid'])

        resultado = f'''
💵 Dólar: R$ {dolar:.2f}
💶 Euro: R$ {euro:.2f}
₿ Bitcoin: R$ {bitcoin:.2f}
        '''
        resultado_label.config(text=resultado)
        cotacoes['Dólar'] = dolar
        cotacoes['Euro'] = euro
        cotacoes['Bitcoin'] = bitcoin

    except Exception as e:
        print("❌ Erro ao buscar cotações:", e)
        messagebox.showerror("Erro", f"Erro ao buscar cotações:\n{e}")

def mostrar_grafico():
    print("📊 Função mostrar_grafico chamada")
    if not cotacoes:
        messagebox.showinfo("Aviso", "Busque as cotações primeiro!")
        return

    try:
        moedas = list(cotacoes.keys())
        valores = list(cotacoes.values())

        plt.figure(figsize=(7, 5))
        bars = plt.bar(moedas, valores, color=["green", "blue", "orange"])
        plt.title("Cotações em Reais")
        plt.ylabel("Valor (R$)")

        # Adiciona os valores em cima das barras
        for bar, valor in zip(bars, valores):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"R$ {valor:.2f}",
                     ha='center', va='bottom', fontsize=10)

        plt.tight_layout()
        plt.savefig("grafico_cotacoes.png")
        plt.show()

    except Exception as e:
        print("❌ Erro ao gerar gráfico:", e)
        messagebox.showerror("Erro", f"Erro ao gerar gráfico:\n{e}")


try:
    print("🚀 Iniciando janela Tkinter...")
    janela = tk.Tk()
    janela.title("💰 Cotações de Moedas")
    janela.geometry("320x300")
    janela.configure(bg="#f0f2f5")
    janela.resizable(False, False)

    tk.Label(janela, text="Cotações de Moedas", font=("Arial", 14, "bold"), bg="#f0f2f5", fg="#333").pack(pady=10)
    tk.Button(janela, text="🔍 Buscar Cotações", command=buscar_cotacoes, bg="#4caf50", fg="white", width=25).pack(pady=5)

    resultado_label = tk.Label(janela, text="Clique acima para buscar os valores", bg="#f0f2f5", fg="#333")
    resultado_label.pack(pady=10)

    tk.Button(janela, text="📊 Mostrar Gráfico", command=mostrar_grafico, bg="#2196f3", fg="white", width=25).pack(pady=5)

    tk.Label(janela, text="By Barao-s123", font=("Arial", 8), bg="#f0f2f5", fg="#777").pack(side="bottom", pady=5)

    print("✅ Interface criada com sucesso. Chamando mainloop()...")

    janela.mainloop()
    print("🧼 Interface encerrada.")

except Exception as e:
    print("❌ Erro ao criar janela:", e)
