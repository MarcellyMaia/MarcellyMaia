---

## Como o fluxo funciona

O fluxo possui apenas **8 etapas**.

Em cada uma delas, uma informação é preparada para a próxima.

---

## 1. Receber a resposta do Forms

Quando alguém envia o formulário, o Power Automate é iniciado automaticamente.

Em seguida, a ação **Obter detalhes da resposta** recupera todas as respostas preenchidas.

**Entrada**

```text
Nome
CPF
Telefone
Upload de Arquivos
```

**Saída**

```text
Todas as respostas do formulário
```

---

## 2. Organizar os arquivos

<p align="center">
  <img src="images/github/json.png" alt="Organizando os arquivos" width="900">
</p>

Os arquivos enviados pelo Forms **não chegam como anexos**.

Eles chegam como um texto contendo informações sobre cada arquivo.

Por isso, primeiro organizamos todos os documentos em uma única lista.

**Exemplo**

```json
[
  {
    "Tipo": "Documento A",
    "Resposta": "..."
  },
  {
    "Tipo": "Documento B",
    "Resposta": "..."
  }
]
```

**Objetivo**

Criar uma lista única para facilitar o processamento.

---

## 3. Ler o JSON

Agora utilizamos **Analisar JSON**.

Essa ação transforma o texto em informações que o Power Automate consegue utilizar.

Depois dela conseguimos acessar:

- Nome do arquivo
- Identificador
- Caminho do arquivo

---

## 4. Processar cada documento

Como podem existir vários anexos, o Power Automate precisa repetir o mesmo processo para cada um.

Dentro do **Aplicar a cada**, fazemos três etapas:

- Verificar se existe arquivo;
- Obter o identificador;
- Criar o nome do anexo.

Exemplo:

```text
Documento A.pdf
Documento B.png
Documento C.jpg
```

---

## 5. Recuperar o arquivo

Até agora temos apenas as informações do documento.

A ação **Obter conteúdo do arquivo** faz o download do arquivo para dentro do fluxo.

**Entrada**

```text
ID do arquivo
```

**Saída**

```text
Arquivo completo
```

---

## 6. Criar a lista de anexos

Cada arquivo recuperado é adicionado a uma variável.

Essa variável será utilizada no envio do e-mail.

```json
{
  "Name": "Documento.pdf",
  "ContentBytes": "..."
}
```

Ao final, essa variável contém todos os anexos enviados pelo Forms.

---

## 7. Preparar os anexos

Antes de enviar o e-mail, utilizamos novamente **Analisar JSON**.

Isso faz com que o Outlook reconheça corretamente todos os arquivos.

---

## 8. Enviar o e-mail

Por fim, utilize a ação **Enviar um e-mail (V2)**.

No campo **Anexos**, informe a variável criada anteriormente.

O Outlook anexará automaticamente todos os documentos.

<p align="center">
  <img src="images/github/e-maiail.png" alt="Resultado do e-mail" width="900">
</p>

---

## Resultado

O destinatário recebe um único e-mail contendo:

- Todas as respostas do Forms;
- Todos os documentos enviados;
- Arquivos organizados automaticamente.