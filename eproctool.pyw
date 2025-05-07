"""Módulo para alterar lembrete no eproc via interface gráfica Tkinter."""

import tkinter as tk
from tkinter import messagebox
import requests


def alterar_lembrete():
    num_processo = entry_num_processo.get()
    descricao = text_descricao.get("1.0", tk.END).strip()
    # Substitua pelos cookies reais da sua sessão autenticada
    cookies = {"PHPSESSID": "772kd1fvh2nje4clap7imfspe8"}
    url = "https://eproc2g.tjsc.jus.br/eproc/controlador.php?acao=processo_lembrete_destino_cadastrar"
    payload = {
        "acao": "processo_lembrete_destino_cadastrar",
        "acao_origem": "processo_lembrete_destino_cadastrar",
        "txtNumProcesso": num_processo,
        "pagina": "processo_selecionar",
        "sin_abrir_link_janela": "S",
        "hdnMostrarSoRelevantes": "false",
        "hash": "3f97cc2005be6381340860c0d12ee888",
        "mostrarDesativados": "S",
        "hdnInfraTipoPagina": "2",
        "sbmSalvar": "Salvar",
        "txaDescricao": descricao,
        "hdnCaracteres": "2995",
        "rdInternoExterno": "interno",
        "selOrgaoDestino": "1202303",
        "selUsuariosDestino": "null",
        "selUsuariosDestinoSelecionados": "null",
        "selExternoProcuradoresProcesso": "311742493878064028683726079378",
        "selExternoProcuradoresProcessoSelecionados": "",
        "selCorLembrete": "000000000000000000000000000001",
        "hdnUsuariosExternoProcuradoresProcesso": ",311742493878064028683726079378",
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    }
    response = requests.post(
        url, data=payload, cookies=cookies, headers=headers, timeout=10
    )
    if response.status_code == 200:
        messagebox.showinfo("Sucesso", "Lembrete alterado com sucesso!")
    else:
        messagebox.showerror("Erro", "Erro ao alterar lembrete.")


# Interface Tkinter
root = tk.Tk()
root.title("Alterar Lembrete eproc")

tk.Label(root, text="Número do Processo").pack(pady=(10, 0))
entry_num_processo = tk.Entry(root, width=40)
entry_num_processo.pack(pady=2)

tk.Label(root, text="Descrição do Lembrete").pack(pady=(10, 0))
text_descricao = tk.Text(root, width=40, height=5)
text_descricao.pack(pady=2)

tk.Button(root, text="Alterar Lembrete", command=alterar_lembrete).pack(pady=10)
tk.Button(root, text="Sair", command=root.quit).pack(pady=(0, 10))

root.mainloop()
