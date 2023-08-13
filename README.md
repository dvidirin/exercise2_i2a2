# Projeto em Grupo CHALLENGE 2 - Redes Generativas - I2A2 Academy

<b>Este projeto foi elaborado por:</b>

<ul>
<li>Robson da Costa - robsondacosta@gmail.com</li>
<li>Sidnei Agostini - jsribeiro123@gmail.com</li>
<li>Daniel Vidiri Neto - dvn.face@gmail.com</li>
<li>Vinícius Reis - viniciusreis@gmail.com</li>
<li>José Neto - jose.fe.neto@gmx.com</li>
</ul>

---

## Descrição do desafio

#### Desenvolver um chatbot de uso terapêutico, semelhante ao Eliza Bot (só que uma versão melhorada) com a ajuda das LLMs disponíveis.

---

## Ferramentas utilizadas

:heavy_check_mark: <b>Python</b><br>
Linguagem de programação utilizada para programar.<br>

:heavy_check_mark: <b>Gradio</b><br>
Biblioteca Python para gerar a interface do ChatBot.<br>

:heavy_check_mark: <b>OpenAI</b><br>
Biblioteca Python para fazer a integração com o ChatGPT (necessário uma API paga).<br>

:heavy_check_mark: <b>decouple</b><br>
Biblioteca Python para fazer a separação de parãmetros de ambiente de configuração.<br>

:heavy_check_mark: <b>Hugging Face</b><br>
Ambiente para fazer o deploy da aplicação, no momento está como privado.<br>

---

## Como utilizar

### 1-Pré-requisitos

O projeto foi desenvolvido dentro do VSCode<br>

- Instalar a biblioteca Python dentro do VSCode.

- O arquivo "requirements.txt" deve ser colocado no mesmo diretório do arquivo python principal.<br>
  Comando para instalar as bibliotecas do requirements.txt:<br>

  ```shell
  $ pip install -r requirements.txt
  ```

- A biblioteca decouple é utilizada para esconder a API Key.<br>
  Para isso ele necessita de um arquivo ".env".<br>
  Baixar o arquivo ".env.example", renomear para somente ".env".<br>
  Dentro do arquivo, colocar uma API Key da OpenAI válida na variável OPENAI_API_KEY (sem aspas).<br>

### 2-Baixar a tarefa do GitHub

- Estando no repositório do projeto, clicar no botão "Code" (botão verde) e selecionar "Download ZIP".

- O arquivo virá compactado, descompactar o arquivo.<br>

### 3-Para executar o projeto no VSCode

- Clique no ícone de play "Run Python file", no canto superior direito.

- O terminal começará a exibir um log.

- O gradio irá gerar uma URL local.

- Segurar a tecla Ctrl do teclado e clicar com o mouse em cima da URL que ele gerou para abrir a aplicação no navegador.

- O aplicativo executará com sucesso.

---

<p>
  <img src="src/assets/to_readme/Autopin.gif">
</p>
