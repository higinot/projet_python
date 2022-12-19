# Projeto de Higienização de Tabelas

Este projeto visa limpar e organizar os dados em uma tabela de clientes para garantir a precisão e a confiabilidade dos dados. Isso inclui a remoção de linhas duplicadas, a correção de erros de digitação e a formatação consistente dos dados.

A higienização de tabelas é importante para qualquer empresa que dependa de dados precisos para tomar decisões importantes. Além disso, manter os dados limpos e organizados pode ajudar a proteger a privacidade dos clientes e evitar problemas de segurança de dados.

Depois de completar a higienização, os dados serão utilizados para criar relatórios e realizar análises de mercado.

## Estrutura do projeto
O projeto possui a seguinte estrutura:

src: contém os arquivos fonte do projeto.
public: contém os arquivos estáticos do projeto.

## Sobre o projeto

Este projeto é uma ferramenta para higienizar tabelas de dados. A higienização de tabelas consiste em remover ou corrigir dados incorretos, inconsistentes ou incompletos de uma tabela. Isso é importante porque os dados incorretos podem levar a análises ou resultados imprecisos e prejudicar a qualidade do trabalho.

## O que o projeto faz

O projeto recebe uma planilha não higienizada (planilha_input) com valores não padronizados e cruza com uma planilha base, para padronizar os valores da planilha input e transformar em um novo Excel higienizado e padronizado.

 - Planilha "base.xlsx":  Tem os valores higienizados e organizados
 - Planilha "planilha_input.xlsx": Tem os valaores não higienizados e não organizados.
 - Planilha "planilha_output.xlsx": Cruza os dados da "base.xlxs" com "planilha_input" e traz os valores de:
    - Registro - "base.xlsx"
    - Referencia - "base.xlsx"
    - Referencia_texto - "base.xlsx"
    - Produto - "base.xlsx"
    - Nome Técnico - "base.xlsx"
    - Fabricante Legal - "base.xlsx"
    - Classificação de Risco - "base.xlsx"
    - Vencimento do Registro - "base.xlsx"
    - Preço Referencia - "planilha_input.xlsx"
    - Planilha Referencia - "planilha_input.xlsx"



