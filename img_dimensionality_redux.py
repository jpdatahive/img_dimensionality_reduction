import marimo

__generated_with = "0.6.26"
app = marimo.App(width="medium", app_title="Image Dimensionality Redux")


@app.cell(hide_code=True)
def __():
    import marimo as mo

    mo.md("""# Redução de dimensionalidade de imagens 🖼️
            ## Uma abordagem para utilização em *Redes Neurais* 🧠""")
    return mo,


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
    Redução de dimensionalidade se refere a técnicas que são utilizadas para a redução do número de variáveis a serem consideradas em um determinado conjunto de dados, isso simplifica os dados enquanto retém o máximo possível da informação relevante.


        """
    ).callout()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        No projeto a seguir, vamos ver como funciona a redução de dimensionalidade em imagens para a utilização em redes neurais, este é um exemplo simples, com a finalidade apenas de reforçar a minha compreensão de como a redução de dimensionalidade pode ser utilizada em um determinado contexto.

        Mas antes vamos entender como funciona uma imagem.

        Uma imagem digital pode ser entendida como uma matriz, onde cada elemento dessa matriz representa um pixel. Aqui está uma explicação simples da estrutura de uma imagem em matriz:

        - Pixel: Um pixel é a menor unidade de uma imagem digital. Ele contém informações sobre a cor e, em imagens em tons de cinza, também sobre a intensidade.

        - Coordenadas: Cada pixel em uma imagem tem coordenadas associadas que indicam sua posição na matriz. Essas coordenadas geralmente são representadas por pares ordenados, como (linha, coluna).

        - Canais de Cor: Para imagens coloridas, cada pixel pode ter vários canais de cor, como vermelho, verde e azul (RGB), ou matiz, saturação e luminosidade (HSL), dependendo do modelo de cor. Cada canal possui um valor que determina a intensidade daquela cor específica no pixel.

        - Formato da Matriz: A imagem é representada como uma matriz bidimensional para imagens em tons de cinza ou uma matriz tridimensional para imagens coloridas.

        Para imagens em tons de cinza, cada elemento da matriz é um número que representa a intensidade do pixel (geralmente variando de 0 a 255).
        Para imagens coloridas, cada elemento da matriz é um vetor que contém os valores dos canais de cor para aquele pixel.
        Resolução: A resolução de uma imagem (por exemplo, 800x600 pixels) indica o número de linhas e colunas da matriz, determinando assim a quantidade de detalhes que a imagem pode conter.

        ### Exemplo Simples:
        Imagine uma imagem em tons de cinza com resolução de 3x3 pixels:

        ```
         img = [[120, 150, 200],
               [100, 130, 180],
               [80, 110, 160]]
        ```

        ### Neste exemplo:

        A matriz é 3x3, ou seja, tem 3 linhas e 3 colunas.
        Cada número representa a intensidade do pixel naquela posição. Por exemplo, o pixel na primeira linha e segunda coluna tem intensidade 150.
        Para imagens coloridas, a matriz seria tridimensional, onde cada elemento é um vetor com três valores (R, G, B) ou equivalentes, dependendo do modelo de cor utilizado.

        Em resumo, a estrutura em matriz proporciona uma forma organizada e sistemática de representar e manipular dados de imagens digitais, facilitando operações como processamento de imagem, análise de conteúdo e reconhecimento de padrões.
        """
    )
    return


@app.cell
def __():
    # Carregamento das bibliotecas necessárias
    from PIL import Image
    from urllib.request import urlopen
    import matplotlib.pyplot as plt
    import seaborn as sns
    from io import BytesIO
    import base64
    return BytesIO, Image, base64, plt, sns, urlopen


@app.cell(hide_code=True)
def __(mo):
    mo.accordion({
        "## Exemplo Prático":
        """Em um conjunto de dados, você tem dezenas de colunas com milhares de linhas contendo características de carros usados. Imagine que, para o seu projeto em questão, essa quantidade de colunas e linhas seja demais para o seu poder de processamento. Podemos então usar duas colunas, como a de **ano de fabricação** e **km rodados** do carro, para criar um valor que consiga representar ambas as informações de alguma forma. Reduzimos então essas duas colunas a uma só com um *score* que consiga uma combinação dessas duas informações, já que carros mais antigos geralmente possuem uma quilometragem maior (isso pode ser aplicado a quaisquer variáveis que estejam de alguma forma relacionadas). Chamamos isso de redução de dimensionalidade e ainda *feature engineering*, pois criamos uma característica nova através de outras."""
    })
    return


@app.cell
def __(mo):
    mo.accordion({
        "## Redução de Dimensionalidade em Imagens":
        """Em imagens, essa redução é especialmente importante devido à alta dimensionalidade junta aos dados visuais. Uma imagem nada mais é que uma matriz de informações divididas basicamente em altura, largura e 3 faixas de cores diferentes.

        Vejamos então uma imagem colorida com um tamanho de 1024x1024 pixels. Ela possui 3.145.728 dimensões (1024 * 1024 * 3 canais de cor (RGB ou Red, Green e Blue)).

        O desempenho computacional para processar diretamente essas imagens de alta resolução é extremamente caro e ineficiente. Essas imagens também possuem uma quantidade de ruído que é indesejada, nos deixando mais distantes das características mais significativas para nossas análises.

        Podemos, no entanto, usar a redução de dimensionalidade para reduzir todas as informações que não são necessariamente desejadas (de acordo com nossa necessidade) para o desenvolvimento de análises. Verifiquemos os exemplos a seguir."""
    })
    return


@app.cell
def __(Image, urlopen):
    # Função para a conversão para a escala de cinza
    def escala_cinza(url_img_colorida):
        # Carrega a imagem original (colorida)
        im = Image.open(urlopen(url_img_colorida))
        # Converte a imagem para cinza
        img_cinza = im.convert("L")

        return img_cinza


    # Função para a conversão numa escala binária
    def escala_binaria(img_cinza, limiar=128):

        # Aplica a conversão para a escala binária
        img_binaria = img_cinza.point(lambda p: p > limiar and 255)

        return img_binaria
    return escala_binaria, escala_cinza


@app.cell
def __(Image, escala_binaria, escala_cinza, urlopen):
    # Imagem da cachorra Laika - mártir canina, vítima de nossa ambição
    laika_dir = "https://upload.wikimedia.org/wikipedia/pt/b/be/Laika_%28cadela%29.jpg"

    # Carregando a imagem da Laika diretamente do link (colorida)
    laika_cor = Image.open(urlopen(laika_dir))

    # Convertendo a Laika para uma escala de cinza
    laika_cinza = escala_cinza(laika_dir)

    # Convertendo a Laika em escala cinza para uma escala binária
    laika_binaria = escala_binaria(laika_cinza, limiar=128)
    return laika_binaria, laika_cinza, laika_cor, laika_dir


@app.cell(hide_code=True)
def __(mo):
    mo.md("## Considere as imagens da Laika a seguir:")
    return


@app.cell(hide_code=True)
def __(BytesIO, laika_binaria, laika_cinza, laika_cor, mo, plt, sns):
    # Configurações de estilo do Seaborn
    sns.set(style="whitegrid", palette="pastel")

    # Criar a figura e os subplots
    _fig, _axs = plt.subplots(1, 3, figsize=(15, 5))

    # Plotar no primeiro subplot
    _axs[0].imshow(laika_cor)
    _axs[0].set_title("Imagem da Laika colorida", fontsize=14)
    _axs[0].axis("off")

    # Plotar no segundo subplot
    _axs[1].imshow(laika_cinza, cmap="gray")
    _axs[1].set_title("Laika em escala de cinza", fontsize=14)
    _axs[1].axis("off")

    # Plotar no terceiro subplot
    _axs[2].imshow(laika_binaria, cmap="gray")
    _axs[2].set_title("Laika em escala binária", fontsize=14)
    _axs[2].axis("off")

    # Ajustar automaticamente o espaçamento entre os subplots
    plt.tight_layout()

    # Salvar a figura em BytesIO
    _buffer = BytesIO()
    plt.savefig(_buffer, format='png')
    _buffer.seek(0)

    _img_bytes = _buffer.getvalue()

    mo.image(_img_bytes)
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        """
        Se quisermos identificar qual animal está presente na imagem, podemos dizer com clareza que não precisamos da cor pra identificar que se trata de um cachorro, como dito anteriormente, o computador teria então uma "percepção" da imagem com um número muito grande de dimensões, as quais não são necessárias para a identificação do animal da foto, portanto, nesse caso, podemos reduzir as dimensões da imagem para que o volume de informações que o computador precise analisar seja muito menor, poupando muito poder de processamento e ao mesmo tempo, "apontando" para as características que mais importam nesse caso.


        Em outros casos, como os de identificação de espécie de flores, por exemplo, as cores têm uma importância significativa, pois fazem parte das características que as definem, portanto, é necessário entender quais características são essenciais para isso.

        Vamos testar agora com uma imagem de sua escolha.
        """
    )
    return


@app.cell
def __(mo):
    img_url = mo.ui.text(kind="text",
                        label="Insira o link de uma imagem jpeg")

    img_url.callout()
    return img_url,


@app.cell
def __(Image, escala_binaria, escala_cinza, img_url, urlopen):
    try:
        # Abrir a imagem a partir da URL fornecida pelo usuário
        with urlopen(img_url.value) as response:
            img_input_cor = Image.open(response)

            img_input_cinza = escala_cinza(img_url.value)

            img_input_binaria = escala_binaria(img_input_cinza)
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
    return img_input_binaria, img_input_cinza, img_input_cor, response


@app.cell
def __(
    BytesIO,
    img_input_binaria,
    img_input_cinza,
    img_input_cor,
    mo,
    plt,
    sns,
):
    # Configurações de estilo do Seaborn
    sns.set(style="whitegrid", palette="pastel")

    # Criar a figura e os subplots
    _fig, _axs = plt.subplots(1, 3, figsize=(15, 5))

    # Plotar no primeiro subplot
    _axs[0].imshow(img_input_cor)
    _axs[0].set_title("Imagem colorida", fontsize=14)
    _axs[0].axis("off")

    # Plotar no segundo subplot
    _axs[1].imshow(img_input_cinza, cmap="gray")
    _axs[1].set_title("Imagem em escala de cinza", fontsize=14)
    _axs[1].axis("off")

    # Plotar no terceiro subplot
    _axs[2].imshow(img_input_binaria, cmap="gray")
    _axs[2].set_title("Imagem em escala binária", fontsize=14)
    _axs[2].axis("off")

    # Ajustar automaticamente o espaçamento entre os subplots
    plt.tight_layout()

    # Salvar a figura em BytesIO
    _buffer = BytesIO()
    plt.savefig(_buffer, format='png')
    _buffer.seek(0)

    _img_bytes = _buffer.getvalue()

    mo.image(_img_bytes)
    return


@app.cell
def __(mo):
    mo.md(""""Aqui, utilizamos a biblioteca Pillow para a redução de dimensionalidade de imagens para o usuo em *redes neurais*.

    Este é um exemplo extremamente simples, apenas para o exercício do entendimento do conceito, visto que não utilizaremos bibliotecas que já são amplamente utilizadas para o pré-processamento de imagens - como OpenCV e outras. 

    Neste exemplo prático, utilizamos a biblioteca Pillow para reduzir uma imagem colorida para uma escala de cinza, e posteriormente, uma escala binária (apenas preto e branco).""")
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
