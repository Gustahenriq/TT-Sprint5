# Análise de Mercado de Câmeras

Este projeto foi desenvolvido como parte da Sprint 5 da TripleTen.

O objetivo é construir uma aplicação web interativa utilizando Streamlit para explorar um conjunto de dados sobre câmeras digitais, permitindo visualizar informações por meio de gráficos e estatísticas descritivas.

> **Observação:** Nesta Sprint foi utilizado o dataset `camera_dataset.csv` em substituição ao dataset padrão (`vehicles_us.csv`), conforme permitido pelas instruções do projeto.

## Tecnologias utilizadas

- Python
- Pandas
- Streamlit
- Plotly Express

## Dataset

O conjunto de dados contém informações sobre mais de 1.000 modelos de câmeras digitais, incluindo:

- Modelo
- Ano de lançamento
- Resolução máxima
- Pixels efetivos
- Peso
- Preço
- Outras especificações técnicas

## Funcionalidades

A aplicação permite:

- Visualizar a distribuição dos preços das câmeras;
- Explorar a relação entre resolução máxima e preço;
- Explorar a relação entre peso e preço;
- Consultar métricas resumidas do conjunto de dados;
- Visualizar a tabela completa de dados.

## Como executar

1. Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
streamlit run app.py
```

## Aplicação online

Após o deploy, o link da aplicação será disponibilizado aqui.

