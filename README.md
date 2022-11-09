# fundamentos-python

### Linux: Códigos básicos
```
ls: listar
mkdir "nome da pasta": criar pasta
cd "nome da pasta": mudar diretório, vai para a pasta nomeada
cd: ir direto pra raíz do usuário
touch "nomedoarquivo.formato": criar arquivo na pasta
rm "nomedoarquivo.formato": excluir arquivo
pwd: saber onde o terminal está trabalhando
cd .. : voltar para a pasta anterior (dois pontos em sequência indicam pasta anterior)
clear: limpar tela
cd pasta/subpasta: ir direto para a pasta nomeada
nano nome do arquivo.formato: abrir o editor de código "nano" para aquele arquivo mencionado
Ctrl+X S: Salvar alterações feitas
cat nomedoarquivo.formato: ver o que está dentro do arquivo mencionado
history: lista todos os comandos dados até agora (últimos 50)
history | grap "códigodesejado": procurar no history todos os códigos que mencionaram "códigodesejado" 
```

### Git, Github e Gitlab
Git: responsável pelo versionamento. Faz a versão do código.

Github e Gitlab: repositórios de código.

Exemplo de profile no Github: https://github.com/leticiadasilva

Passar repositório do GitHub para pasta do computador local/pessoal:

```
cd "pasta que deseja armazenar"
git clone "URL"
```

Para abrir o editor de código na pasta raíz:
```
code .
```
Dica: abrir vscode pelo terminal, para entrar direto na pasta desejada
```
cd pasta/subpasta
code .
```

Sobre o git: https://ohshitgit.com/

-----
Ambiente de trabalho, site do LabRI UNESP: https://labriunesp.org/docs/projetos/ensino/ambiente

Ambiente virtual: é uma estrutura que isola as bibliotecas do computador, para caso haja algum erro nos programas, o ambiente virtual evita danos ao próprio computador. Também, é possível replicar o ambiente virtual.
Conda: tipo de ambiente virtual

Para criação do ambiente virtual:
1. Logar no seu usuário pessoal do X2Go
2. Pelo terminal, criar pasta "Códigos" a partir da raíz e importar "fundamentos-python" para a pasta Códigos.
3. Abrir o vscode na pasta "fundamentos-python"
4. Rodar os comandos da página [ambiente virtual do labri](https://labriunesp.org/docs/projetos/ensino/ambiente/conda#instru%C3%A7%C3%B5es-para-primeira-utiliza%C3%A7%C3%A3o)

Informações para o ambiente virtual:
```
name: env_artur
channels:
  - conda-forge
  - defaults
dependencies:
  - python
  - beautifulsoup4
  - lxml
  - selenium
  - geckodriver
  - requests
  - tinydb
```
