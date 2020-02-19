# GENow
GENow _deve_ ser uma ferramenta capaz de gerar código fonte à partir de especificações de modelo.

![Fluxo](https://raw.githubusercontent.com/qzar02/genow/master/docs/flow.png)

```
graph TD
A[<center>ESPECIFICAÇÃO<br/>DO MODELO DE DOMINIO</center>] --> B[REST API]
B[REST API] --> C[INSTÂNCIA DO MODELO]
C[INSTÂNCIA DO MODELO] --> E[CÓDIGO FONTE GERADO] 
D[TEMPLATES DE CÓDIGO] --> E[CÓDIGO FONTE GERADO]
E[CÓDIGO FONTE GERADO] --> F[PACOTES DE SOFTWARE]
```


O código fonte gerado pode ser para um framework especifico, uma API, ou uma configuração de instalação de software. Tudo depende dos `templates de código` que contém a _lógica_ de geração do código.

## 1. Especificação do modelo de dominio
Essa especificação é um modelo descrevendo as abstrações que definem um dominio de negócio.
Por exemplo, um `Data Warehouse` é um dominio com lógica e conceitos especificos; um `WebSite` também. Todos possuem conceitos que podem ser especificados através de estruturas de dados ou modelos.
Para que esses modelos de dominios se tornem concretos e consumíveis é necessário a criação de uma API 
que concretize os conceitos do dominio em projetos especificos. Essa especificação é feita usando o EVE - REST API framework (https://docs.python-eve.org/).

## 2. REST API
A REST API permite a criação da instância do modelo e o consumo direto pelas ferramentas de geração de código e outros softwares. 

## 3. Instância do modelo
A Instância do modelo é o modelo de dominio em um alto nível de abstração, pronto para ser consumido através da REST API.

## 4. Templates de código
Os templates de código são formas de estruturar modelos lógicos que podem ser usados juntamente com a instância do modelo para gerar código fonte parametrizável.
Podem existir templates na forma de pacotes para frameworks, softwares, ou APIs especificas. Podem ser consumidos através da API REST.

## 5. Código fonte gerado
Quando um template de código é renderizado usando uma instância de modelo, o código fonte é gerado e pode ser armazenado em repositorio de código.

## 6. Pacote de software
O pacote de software é o software pronto para instalação e uso. A configuração e parametrização do software provém do código fonte gerado.


## Aplicando os conceitos

Pra demonstrar o uso da ferramenta, será criado uma plataforma de Data Pipeline usando software open source.

Software utilizado: 
Airflow, Apache Spark, Flask e Plotly.

