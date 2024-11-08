
# Classificação de Frames de Vídeo com ViT (Visual Transformer)

Este projeto utiliza o modelo ViT para fazer predições em frames extraídos de um vídeo, salvando os resultados em um arquivo JSON.

## Requisitos

- Python 3.7 ou superior

## Passo a Passo para Configuração

### 1. Instalar Dependências

Primeiro, instale as dependências listadas no arquivo `requirements.txt`. Para isso, execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

### 2. Criar um Ambiente Virtual

Recomenda-se criar um ambiente virtual para isolar as dependências do projeto. Siga as instruções abaixo conforme seu sistema operacional.

#### Windows

1. Abra o terminal (Prompt de Comando ou PowerShell).
2. Navegue até o diretório do projeto.
3. Crie o ambiente virtual com o comando:
   ```bash
   python -m venv venv
   ```
4. Ative o ambiente virtual:
   ```bash
   .\venv\Scripts\activate
   ```
5. Instale as dependências no ambiente virtual:
   ```bash
   pip install -r requirements.txt
   ```

#### Linux

1. Abra o terminal.
2. Navegue até o diretório do projeto.
3. Crie o ambiente virtual com o comando:
   ```bash
   python3 -m venv venv
   ```
4. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```
5. Instale as dependências no ambiente virtual:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Executar o Script

Para rodar o script, utilize o seguinte comando:

```bash
python script.py <caminho_do_video> <caminho_do_output_json>
```

- `<caminho_do_video>`: Caminho para o arquivo de vídeo de entrada.
- `<caminho_do_output_json>`: Caminho para salvar o arquivo JSON com os resultados.

#### Exemplo de Execução

```bash
python main.py "meu_video.mp4" "predicoes.json"
```

Após a execução, as predições para cada frame do vídeo serão salvas no arquivo `predicoes.json`.

## Estrutura do Arquivo JSON de Saída

O arquivo JSON gerado conterá as seguintes informações:

```json
{
    "framerate": <taxa_de_quadros>,
    "frames": [
        {
            "frame_number": <número_do_frame>,
            "prediction": {
                "probabilities": [
                    ["label_1", <probabilidade>],
                    ["label_2", <probabilidade>],
                    ...
                ]
            }
        },
        ...
    ]
}
```

## Notas

- O modelo usado é o ViT para reconhecimento de expressões faciais (`motheecreator/vit-Facial-Expression-Recognition`).
- Certifique-se de que o vídeo de entrada está no formato compatível com o OpenCV.
