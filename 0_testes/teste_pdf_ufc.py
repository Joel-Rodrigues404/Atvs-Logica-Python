from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def criar_pdf(output_file, imagens):
    # Configurando o tamanho da página
    largura, altura = A4

    # Criando o canvas para o PDF
    c = canvas.Canvas(output_file, pagesize=A4)

    # Título
    c.setFont("Times-Bold", 14)
    c.drawString(200, altura - 50, "UNIVERSIDADE FEDERAL DO CEARÁ")
    c.drawString(200, altura - 70, "DIRETORIA DO CAMPUS DE SOBRAL")

    # Declaração
    c.setFont("Times-Bold", 12)
    c.drawString(270, altura - 120, "DECLARAÇÃO")

    # Corpo do texto
    texto = (
        "A diretoria do Campus de Sobral, declara que, conforme o calendário "
        "aprovado pelo Conselho de Ensino, Pesquisa e Extensão – CEPE, a retomada do semestre "
        "letivo 2024.2 após o recesso de final de ano, ocorrerá no dia 06 de janeiro de 2025. "
        "Desse modo, solicitamos a colaboração das gestões municipais da região quanto à "
        "viabilização do transporte para traslado de universitários à cidade de Sobral, garantindo "
        "o acesso dos discentes da Universidade Federal do Ceará às atividades letivas."
    )

    # Escrevendo o texto em múltiplas linhas
    c.setFont("Times-Roman", 12)
    linhas = texto.split(" ")
    texto_formatado = ""
    largura_linha = 0
    espaco_linha = 20
    y = altura - 160

    for palavra in linhas:
        largura_palavra = c.stringWidth(palavra + " ", "Times-Roman", 12)
        if largura_linha + largura_palavra > 500:
            c.drawString(72, y, texto_formatado)
            texto_formatado = palavra + " "
            largura_linha = largura_palavra
            y -= espaco_linha
        else:
            texto_formatado += palavra + " "
            largura_linha += largura_palavra

    c.drawString(72, y, texto_formatado)

    # Assinatura
    c.drawString(72, y - 60, "Sobral, 13 de dezembro de 2024.")
    c.drawString(72, y - 100, "Profa. Rita Helena Sousa Ferreira Gomes")
    c.drawString(72, y - 120, "Vice-Diretora do Campus de Sobral")

    # Endereço
    c.setFont("Times-Italic", 10)
    c.drawString(
        72, y - 180, "DIRETORIA DO CAMPUS DE SOBRAL"
    )
    c.drawString(
        72, y - 200, "Rua Coronel Estanislau Frota, 563. Bloco I - 1º Andar. Centro,"
    )
    c.drawString(72, y - 220, "CEP 62.010-560. Sobral/CE.")

    # Inserir imagens
    for i, imagem_path in enumerate(imagens):
        # Reduzir o tamanho da imagem para caber na página
        c.drawImage(imagem_path, 72, y - 300 -
                    (i * 150), width=400, height=150)

    # Salvando o PDF
    c.save()


# Lista de imagens extraídas manualmente ou via script anterior
# Adicione as imagens extraídas
imagens = ["imagem_pagina1_1.png"]

# Criar o PDF com as imagens
criar_pdf("Retomada_semestre_2024.2_com_imagens.pdf", imagens)
