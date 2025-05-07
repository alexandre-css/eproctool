import PySimpleGUI as sg
import requests

def alterar_lembrete(num_processo, descricao, cookies):
    url = "https://eproc2g.tjsc.jus.br/eproc/controlador.php?acao=processo_lembrete_destino_cadastrar"
    payload = {
        'acao': 'processo_lembrete_destino_cadastrar',
        'acao_origem': 'processo_lembrete_destino_cadastrar',
        'txtNumProcesso': num_processo,
        'pagina': 'processo_selecionar',
        'sin_abrir_link_janela': 'S',
        'hdnMostrarSoRelevantes': 'false',
        'hash': '3f97cc2005be6381340860c0d12ee888',
        'mostrarDesativados': 'S',
        'hdnInfraTipoPagina': '2',
        'sbmSalvar': 'Salvar',
        'txaDescricao': descricao,
        'hdnCaracteres': '2995',
        'rdInternoExterno': 'interno',
        'selOrgaoDestino': '1202303',
        'selUsuariosDestino': 'null',
        'selUsuariosDestinoSelecionados': 'null',
        'selExternoProcuradoresProcesso': '311742493878064028683726079378',
        'selExternoProcuradoresProcessoSelecionados': '',
        'selCorLembrete': '000000000000000000000000000001',
        'hdnUsuariosExternoProcuradoresProcesso': ',311742493878064028683726079378'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'
    }
    response = requests.post(url, data=payload, cookies=cookies, headers=headers)
    return response.status_code, response.text

layout = [
    [sg.Text('Número do Processo')],
    [sg.InputText(key='num_processo')],
    [sg.Text('Descrição do Lembrete')],
    [sg.Multiline(key='descricao', size=(40, 5))],
    [sg.Button('Alterar Lembrete'), sg.Button('Sair')],
    [sg.Text('', key='output')]
]

window = sg.Window('Alterar Lembrete eproc', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Alterar Lembrete':
        # Substitua pelos cookies reais da sua sessão autenticada
        cookies = {'PHPSESSID': '772kd1fvh2nje4clap7imfspe8'}
        num_processo = values['num_processo']
        descricao = values['descricao']
        status_code, response_text = alterar_lembrete(num_processo, descricao, cookies)
        if status_code == 200:
            window['output'].update('Lembrete alterado com sucesso!')
        else:
            window['output'].update('Erro ao alterar lembrete.')

window.close()