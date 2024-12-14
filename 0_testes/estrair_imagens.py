# from PyPDF2 import PdfReader
# from PIL import Image
# # import io
#
#
# def extrair_imagens(pdf_path):
#     reader = PdfReader(pdf_path)
#     count = 0
#
#     for page in reader.pages:
#         if "/XObject" in page["/Resources"]:
#             xObject = page["/Resources"]["/XObject"].get_object()
#             for obj in xObject:
#                 if xObject[obj]["/Subtype"] == "/Image":
#                     tamanho = (xObject[obj]["/Width"], xObject[obj]["/Height"])
#                     data = xObject[obj].get_data()
#                     mode = "RGB" if xObject[obj]["/ColorSpace"] == "/DeviceRGB" else "P"
#
#                     imagem = Image.frombytes(mode, tamanho, data)
#                     imagem_path = f"imagem_extraida_{count + 1}.png"
#                     imagem.save(imagem_path)
#                     print(f"Imagem extraída e salva como {imagem_path}")
#                     count += 1
#
#
# extrair_imagens("Retomada_semestre_2024.2_para_as_prefeituras.pdf")


import fitz  # PyMuPDF


def extrair_imagens_alta_qualidade(pdf_path):
    # Abrir o PDF
    documento = fitz.open(pdf_path)
    imagens_extraidas = []

    for numero_pagina in range(len(documento)):
        pagina = documento[numero_pagina]
        for img_index, img in enumerate(pagina.get_images(full=True)):
            xref = img[0]
            base_image = documento.extract_image(xref)
            imagem_bytes = base_image["image"]
            # Formato da imagem (ex: 'png', 'jpeg')
            imagem_extensao = base_image["ext"]
            imagem_nome = f"imagem_pagina{
                numero_pagina + 1}_{img_index + 1}.{imagem_extensao}"

            # Salvar imagem em disco
            with open(imagem_nome, "wb") as img_file:
                img_file.write(imagem_bytes)
                imagens_extraidas.append(imagem_nome)
                print(f"Imagem salva: {imagem_nome}")

    print(f"Total de imagens extraídas: {len(imagens_extraidas)}")
    return imagens_extraidas


# Executar a função no PDF
extrair_imagens_alta_qualidade(
    "Retomada_semestre_2024.2_para_as_prefeituras.pdf")
