# Como Recuperar Arquivos do Microsoft Forms e Enviá-los por E-mail com Power Automate

## Fluxo explicado passo a passo

Neste exemplo, vamos construir uma automação capaz de recuperar todos os arquivos enviados pelo **Microsoft Forms** e anexá-los automaticamente em um e-mail utilizando o **Power Automate**.

O objetivo é simples: sempre que uma nova resposta for enviada, todas as informações e documentos chegarão organizados em um único e-mail.

---

## Visão geral do fluxo

```text
Microsoft Forms
        │
        ▼
When a new response is submitted
        │
        ▼
Get response details
        │
        ▼
Organizar documentos
        │
        ▼
Analisar JSON
        │
        ▼
Aplicar a cada
        │
        ▼
Obter conteúdo do arquivo
        │
        ▼
Adicionar anexos à coleção
        │
        ▼
Preparar anexos
        │
        ▼
Enviar e-mail
```

---

### Etapa 1 — Receber a resposta

Tudo começa quando uma nova resposta é enviada pelo Microsoft Forms.

Adicione as ações:

* **When a new response is submitted**
* **Get response details**

A primeira inicia automaticamente o fluxo.

A segunda recupera todas as respostas preenchidas no formulário, incluindo os campos de upload.

---

### Etapa 2 — Criar uma coleção para os anexos

Antes de recuperar qualquer arquivo, precisamos criar um local para armazená-los.

Adicione uma ação **Inicializar variável**.

Configure-a da seguinte forma:

| Configuração | Valor    |
| ------------ | -------- |
| Nome         | `Anexos` |
| Tipo         | `Array`  |

Durante a execução do fluxo, todos os documentos serão adicionados nessa variável.

---

### Etapa 3 — Organizar os documentos

Os campos de upload do Forms chegam separados.

Para facilitar o processamento, vamos agrupá-los em uma única coleção.

Adicione uma ação **Compor** contendo um JSON semelhante ao exemplo abaixo.

```json
[
  {
    "Tipo": "Documento 1",
    "Resposta": "Campo Upload 1"
  },
  {
    "Tipo": "Documento 2",
    "Resposta": "Campo Upload 2"
  }
]
```

Cada objeto representa um campo de upload existente no formulário.

> **Importante**
>
> Os identificadores utilizados são diferentes em cada Microsoft Forms.
> Utilize sempre os campos dinâmicos do seu próprio formulário.

<p align="center">
<img src="../../images/github/json.png" alt="JSON organizado" width="900">
</p>

---

### Etapa 4 — Interpretar o JSON

Até aqui, o Power Automate ainda enxerga essas informações como texto.

Agora precisamos transformá-las em uma estrutura que possa ser utilizada nas próximas etapas.

Adicione a ação **Analisar JSON**.

**Conteúdo**

Utilize a saída da ação **Compor**.

**Schema**

Cole o schema correspondente ao JSON criado anteriormente.

Depois dessa etapa será possível acessar propriedades como:

* Nome do arquivo;
* Identificador (ID);
* Caminho;
* Demais informações do documento.

---

### Etapa 5 — Processar cada documento

Como um formulário pode possuir vários anexos, precisamos repetir o mesmo processo para cada um deles.

Adicione uma ação **Aplicar a cada**.

Como entrada, utilize a saída da ação **Analisar JSON**.

Todas as próximas ações serão criadas dentro desse laço.

<p align="center">
<img src="../../images/github/compor.png" alt="Aplicar a cada" width="900">
</p>

---

### Etapa 6 — Recuperar o identificador

O primeiro passo é descobrir onde o arquivo está armazenado.

Adicione uma ação **Compor**.

Essa expressão verifica se existe um arquivo.

Caso exista, ela retorna seu identificador.

Caso contrário, retorna o texto **ARQUIVO**, evitando erros durante o fluxo.

```text
@if(...)
```

Esse identificador será utilizado para recuperar o arquivo na próxima etapa.

---

### Etapa 7 — Gerar o nome do anexo

Agora adicione outro **Compor**.

Ele será responsável por montar automaticamente o nome do arquivo.

Exemplo:

```text
Documento1.pdf
Documento2.jpg
Documento3.png
```

Isso garante que os anexos sejam enviados com nomes padronizados.

---

### Etapa 8 — Verificar se existe um arquivo

Adicione uma ação **Condição**.

Verifique se o resultado do primeiro **Compor** é diferente de **ARQUIVO**.

* **True** → existe um documento para recuperar.
* **False** → não existe arquivo. O fluxo continua normalmente para o próximo item.

Essa validação evita erros quando algum campo de upload estiver vazio.

---

### Etapa 9 — Recuperar o arquivo

No ramo **True**, adicione a ação:

**Obter conteúdo do arquivo**

Utilize como **Identificador do Arquivo** o valor retornado pelo primeiro **Compor**.

Agora o Power Automate finalmente possui o arquivo completo.

---

### Etapa 10 — Adicionar o arquivo à coleção

Ainda no ramo **True**, adicione a ação:

**Acrescentar à variável de matriz**

Selecione a variável **Anexos**.

No campo **Valor**, informe uma estrutura semelhante a esta:

```json
{
  "Name": "...",
  "ContentBytes": "..."
}
```

Repita esse processo para cada documento encontrado.

Ao final do **Aplicar a cada**, a variável **Anexos** conterá todos os arquivos enviados pelo formulário.

---

### Etapa 11 — Preparar os anexos

Depois que todos os arquivos forem adicionados à coleção, adicione duas ações:

* **Compor**
* **Analisar JSON**

Essas ações convertem a coleção para o formato esperado pelo Outlook.

<p align="center">
<img src="../../images/github/fim.png" alt="Preparação dos anexos" width="900">
</p>

---

### Etapa 12 — Enviar o e-mail

Adicione a ação:

**Enviar um e-mail (V2)**

Configure normalmente:

* Destinatário;
* Assunto;
* Corpo do e-mail.

No campo **Anexos**, utilize a saída do último **Analisar JSON**.

O Outlook anexará automaticamente todos os documentos recuperados durante o fluxo.

<p align="center">
<img src="../../images/github/e-mail.png" alt="Resultado do e-mail" width="900">
</p>

---

## Resultado

Ao final da execução, o destinatário receberá um único e-mail contendo:

* Todas as respostas do Microsoft Forms;
* Todos os arquivos enviados;
* Arquivos organizados automaticamente;
* Anexos prontos para análise.

---

### Próximos passos

Neste artigo expliquei a lógica da automação.

No repositório você encontrará o fluxo completo, as expressões utilizadas e poderá adaptar a solução para qualquer formulário do Microsoft Forms que utilize upload de arquivos.
