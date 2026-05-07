Dashboard de Vendas Global com Python e Power BI
<img width="1416" height="787" alt="Captura de tela 2026-05-07 154335" src="https://github.com/user-attachments/assets/a8187d83-89d6-4b96-b673-8e916d14ede7" />

Sobre o Projeto
Este projeto foi desenvolvido com o objetivo de realizar a análise de vendas internacionais utilizando Python para tratamento dos dados e Power BI para visualização das informações
A proposta do projeto é transformar dados brutos de transações comerciais em indicadores e gráficos que auxiliam no acompanhamento do faturamento e na performance de marcas e produtos

Tecnologias Utilizadas
Python
Pandas
Numpy
Power BI

Estrutura do Projeto
Vendas.xlsx → Base de dados contendo o histórico de vendas
vendas.py → Script Python responsável pelo tratamento e análise dos dados
Dashboard_Vendas.pbix → Dashboard desenvolvido no Power BI

Tratamento de Dados com Python
O tratamento dos dados foi realizado utilizando Pandas e Numpy
O script realiza:
Leitura da base de dados de vendas
Tratamento de valores nulos e limpeza de espaços em branco
Conversão de colunas de data para formato temporal
Cálculo de faturamento total por item (Preço x Quantidade)
Cálculo de margem de contribuição e volume de vendas
Agrupamentos por marca e categoria
Geração dos dados utilizados para alimentação do Power BI

Indicadores Desenvolvidos
O projeto realiza o cálculo dos seguintes indicadores:
Faturamento total global
Quantidade total vendida
Ranking de faturamento por marca
Ticket médio por produto
Identificação do produto líder de vendas
Evolução mensal de faturamento
Distribuição de vendas por localidade geográfica

Dashboard no Power BI
O dashboard foi desenvolvido para apresentar os principais indicadores comerciais de forma visual e interativa
O painel contém:
Cards com faturamento total e quantidade vendida
Gráfico de linha com tendência mensal de vendas
Ranking de faturamento por marca
Mapa de calor por região de vendas
Tabela detalhada de performance de produtos

Filtros Interativos
O dashboard possui filtros por:
Marca
Localidade
Mês e Ano
Ao selecionar uma marca ou região, todos os gráficos e indicadores são atualizados automaticamente, permitindo visualizar o desempenho específico de cada segmento do mercado

Objetivo do Projeto
O projeto foi desenvolvido para prática de:
Análise de dados comerciais
Tratamento de dados estruturados com Python
Desenvolvimento de KPIs de vendas
Visualização de dados geoespaciais
Criação de dashboards dinâmicos no Power BI

Autor
João Gabriel Amaral
