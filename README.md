<p align="center">

  <img src="https://github.com/Trabalhos-Fatec/Calculadora-FrontEnd/blob/main/Repository%20Images/Calculadora-Banner.png" alt="banner do projeto calculadora">
  
</p>

*******

## indice do documento

 1. [Como baixar o projeto?](#build) <br>
 2. [Entregas (Video)](#send1) <br>
 3. [Autoras](#author)
 4. [Orientador](#teacher)

-------------------------------------------------------
<div id='build'/>  

### Como baixar o projeto e dar build

**Máquina Virtual**

- Para instalar a Virtualenv, basta executar:

```
$ pip3 install virtualenv
```

- Para criar a Virtualenv do projeto, execute:

```
$ virtualenv -p python3 venv
```

- Para iniciar a Virtualenv:

**Linux**

```
$ source venv/bin/activate
```

**Windows**

```
$ venv/Scripts/Activate
```


- Instale as dependências do projeto:
```
$ venv/bin/pip3 install -r requirements.txt
```

- Agora rode o projeto:
```
$ python3 main.py
```

-------------------------------------------------------

### Configuração do banco de dados

Criação das tabelas no banco de dados

```
#banco de dados utilizado
use NomeDoBanco;

create table historico (
id_historico int primary key,
dt_registro date not null,
argumentos varchar(20) not null,
resultado decimal(5,2) not null,
id_operacao int not null references operacao (id_operacao)
);

create table operacao (
id_operacao int not null primary key,
tipo_operacao varchar(30) not null,
operacao_especifica varchar(5) not null
);
```
  --------------------------
 
 ## Entregas

 <div id='send1'/>  

|  Entrega  | Video   |      Descrição      |
|:----------:|:----------:|:-------------:|
 Entrega 1 | <a href="https://youtu.be/LmJKxIrqFBw" target="_blank"><img src="https://github.com/Trabalhos-Fatec/Calculadora-FrontEnd/blob/main/Repository%20Images/Capa-video1.png"  width="70%" title="Entrega 1"/></a> |  Neste vídeo eu estarei te passando as etapas para baixar este projeto, buildar e subir a aplicação para um servidor local.|
 Entrega 2| <a href="" target="_blank"><img src="https://github.com/Trabalhos-Fatec/Calculadora-FrontEnd/blob/main/Repository%20Images/Capa-video2.png"  width="70%" title="Entrega 2"/></a> |    Neste vídeo eu estarei te passando as etapas para baixar os serviços nos repositórios do projeto, rodar todos os serviços e demonstrar a interação entre eles com o armazenamento das informações no banco de dados.   |
 Entrega 3| <a href="https://www.youtube.com/watch?v=qsWQxMBulh0" target="_blank">  <img src="https://github.com/Trabalhos-Fatec/Calculadora-FrontEnd/blob/main/Repository%20Images/Capa-video3.png"  width="70%" title="Entrega 3"/></a> |    Neste vídeo eu estarei te passando a demonstração da integração contínua com a falha na instalação das dependências e falha no teste unitário.   |


  --------------------------

<div id='author'/>  
 
  ## Autoras
<table>
  <tr>
    <td align="center"><a href="https://github.com/littlebru"><img src="https://avatars3.githubusercontent.com/u/41810923?s=460&u=c2196ec3a4f76218d7b11bb2a9cf025d2d2e9fdc&v=4" width="70px;" alt="" title="Olha eu ai"/></td>
 </tr>
</table>
 
[Bruna Larissa Clemente Gomes](https://github.com/littlebru)<br>

<table>
  <tr>
    <td align="center"><a href="https://github.com/nayaralorrane"><img src="https://avatars.githubusercontent.com/u/59921213?v=4" width="70px;" alt="" title="Olha eu ai"/></td>
 </tr>
</table>
 
[Nayara Lorrane](https://github.com/nayaralorrane)<br>

 <div id='teacher'/>  

## Orientador
<table>
  <tr>
    <td align="center"><a href="https://github.com/prof-fabriciogmc"><img src="https://avatars.githubusercontent.com/u/31361161?v=4" width="70px;" alt="" title="Mestre Masanori"/></td>
  </tr>
</table>

 [Fabricio Galende Marques de Carvalho](https://github.com/prof-fabriciogmc)

