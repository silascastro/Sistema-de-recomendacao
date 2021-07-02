from functools import partial
from os import name
from pywebio import start_server
from pywebio.input import NUMBER, input, TEXT, input_group,radio
from pywebio.output import put_code, put_html, put_markdown, put_text, put_buttons,put_table, clear
from bokeh.io import output_notebook,show
from bokeh.io import show,output_file,output_notebook
from bokeh.plotting import figure
from pywebio.session import hold
from correlacaoPearson import recommend, users,artists

list_of_users = []
avaliation_artists_media = []
my_avaliation = []
user_name = ''

def refactor():
    for e in users:
        user = e
        avaliations = []
        for key in artists: #avalia se o artista existe no array de artistas
            if(key not in users[e]):
                #avaliations.append(users[e][key])
                avaliations.append('-')
            else:
                avaliations.append(users[e][key])
        list_of_users.append(list(user.split())+avaliations)
    #print(list_of_users)

def mediaArtistas():
    for artist in artists:
        n = 0
        soma = 0
        for user in users:
            if(artist in users[user]):
                soma+=users[user][artist]
                n+=1
        avaliation_artists_media.append(soma/n)



def checkName(name):
    if(name == ''):
        return 'Digite o seu nome!'

def checkAvaliacaoNumero(value):
    if(float(value) <0 or float(value) > 5):
        return 'Valor inválido!'

def btnclick(name,btn_val):
    if(btn_val == 'sim'):
        clear()
        avaliar_artistas(name)
    elif(btn_val == "não"):
        exit(-1)


def refactor_my_avaliation(avaliacao):
    list_of_valid_avaliations = []
    for e,i in enumerate(avaliacao):
        if(e>0 and not i == '-'):
            list_of_valid_avaliations.append(float(i))

    concat = list(zip(artists,list_of_valid_avaliations))
    dic = dict(concat)
    return (avaliacao[0],dic)


def avaliar_artistas(name):
    array_avaliacao = []
    array_avaliacao.append(name)
    put_text('Iniciando nova avaliação')
    for e in artists:
        avaliacao = input('como você avalia %s'%e)
        if(avaliacao == '' or float(avaliacao) < 0 or float(avaliacao)>5):
            array_avaliacao.append('-')
        else:
            array_avaliacao.append(avaliacao)
    put_text("Deseja confirmar as avaliações")
    put_table([artists]+[array_avaliacao[1:]])
    put_buttons(['sim','não'],onclick=partial(avaliacao_btn, array_avaliacao))


def avaliacao_btn(avaliacao, btn_val):
    if(btn_val == 'sim'):
        clear()
        list_of_users.append(avaliacao)
        my_avaliation = refactor_my_avaliation(avaliacao)
        put_table([['Usuários']+artists]+list_of_users)
        plotar_grafico()
        put_buttons(['ver recomendações'], onclick=partial(mostrar_recomendacao, my_avaliation))
    elif(btn_val == "não"):
        exit(-1)


def put_on_pearson(avaliacao):
    pass

def put_on_similaridade_cosseno(avaliacao):
    pass

def mostrar_recomendacao(avaliacao,btn_val):
    users[avaliacao[0]] = avaliacao[1]
    recomendations =recommend(avaliacao[0],users)
    #clear()
    print(recomendations)
    put_markdown('## %s, Talvez você goste dessas bandas!'%avaliacao[0])
    put_table([[x[0]]  for x in recomendations],['Recomendações de Bandas'])


def plotar_grafico():
    put_markdown("# Média de avaliações de artistas")
    p = figure(x_range=artists, plot_height=250, title="Avaliações dos artistas",
    toolbar_location=None, tools="")
    p.vbar(x=artists, top=avaliation_artists_media, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    show(p)
    put_html('<br>')



def main():
    refactor()
    mediaArtistas()
    output_notebook(notebook_type='pywebio') #
    #start

    name = input("Qual o seu nome?", type=TEXT, validate=checkName)


    if(name != ''):
        put_markdown('## Olá %s, Aqui estão algumas bandas já avaliadas por algumas pessoas!'%name)
        put_table([['Usuários']+artists]+list_of_users)

        plotar_grafico()

        put_text("Deseja avaliar algum artista?")
        put_buttons(['sim','não'],onclick=partial(btnclick, name))

        hold()



if __name__ == '__main__':
    start_server(main, port=8080, debug=True)
