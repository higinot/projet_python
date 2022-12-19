# Projeto de Higienização de Tabela com Python e openpyxl

Este projeto visa limpar e organizar os dados em uma tabela de clientes para garantir a precisão e a confiabilidade dos dados. Isso inclui a remoção de linhas duplicadas, a correção de erros de digitação e a formatação consistente dos dados.

A higienização de tabelas é importante para qualquer empresa que dependa de dados precisos para tomar decisões importantes. Além disso, manter os dados limpos e organizados pode ajudar a proteger a privacidade dos clientes e evitar problemas de segurança de dados.

Depois de completar a higienização, os dados serão utilizados para criar relatórios e realizar análises de mercado.

## Estrutura do projeto
O projeto possui a seguinte estrutura:

src: contém os arquivos fonte do projeto.
public: contém os arquivos estáticos do projeto.

## Sobre o projeto

Este projeto é uma ferramenta para higienizar tabelas de dados. A higienização de tabelas consiste em remover ou corrigir dados incorretos, inconsistentes ou incompletos de uma tabela. Isso é importante porque os dados incorretos podem levar a análises ou resultados imprecisos e prejudicar a qualidade do trabalho.

## O que deve ser desenvolvido
O projeto deve incluir as seguintes funcionalidades:

- Leitura de um arquivo .xlsx de entrada
- Leitura de um arquivo .xlsx de base
- Cruzamento de dados entre as tabelas de entrada e base
- Geração de um novo arquivo .xlsx de saída com a tabela higienizada
- Além disso, o projeto deve ser capaz de lidar com os seguintes casos:
    - Tabelas com múltiplas abas
    - Tabelas com diferentes tipos de dados nas células (números, texto, data, etc.)


### **Cruzamento de dados**

Para realizar o cruzamento de dados, são necessários os seguintes passos:
 1. Ler os dados da planilha "planilha_input.xlsx" no campo "Registro ANVISA" que está na coluna "J"
 2. Verificar se o dado contém na planilha base "base.xlsx", exemplo:
    - Verificar se a célula "J2" com  valor "10341350915" existe na planilha "base.xlsx" no campo "Registro" na coluna "A"
 3. Caso contenha o dado na planilha "base.xlsx", verificar se a referência da  contém na planilha base "base.xlsx", exemplo:
    - Verificar se a célula "K2" com valor "SC-4254" existe na planilha "base.xlxs" no campo "Referencia" na coluna "A".
4. Caso os dados da "planilha_input.xlsx" sejam iguais tanto em ANVISA quanto REFERENCIA, copiar em uma nova planilha "planilha_output.xlsx" os dados da linha, exemplo:
 - Copiar linha 10702 da planilha base "base.xlsx" com os dados: 
    - A10702: 10341350915
    - B10702: M365SC42540
    - C10702: (SC-4254)
    - D10702: Precision Montage™ MRI	
    - E10702: Sistema Neuroestimulador	
    - F10702: BOSTON SCIENTIFIC NEUROMODULATION CORP.
    - G10702: IV - MÁXIMO RISCO
    - H10702: 03/04/2027
5. Colar a linha 10702 em uma nova linha na planilha "planilha_output.xlsx", exemplo:
    - A1: 10341350915
    - B1: M365SC42540
    - C1: (SC-4254)
    - D1: Precision Montage™ MRI	
    - E1: Sistema Neuroestimulador	
    - F1: BOSTON SCIENTIFIC NEUROMODULATION CORP.
    - G1: IV - MÁXIMO RISCO
    - H1: 03/04/2027
5. Copiar os dados do campo "Valor Máximo Intercambio Nacional" na coluna "L" e "Referencia Base" na coluna "AB"  para a planilha de saída "planilha_output.xlsx", exemplo:
    - I1: 324,39
    - J1: TNUMM
6. Realizar esse processo para todos os valores da planilha de entrada "planilha_input.xlsx".

## *Funcionalidade Extra*
 - Trazer um resumo do cruzamento de dados das planilha de entrada e base em outra aba da planilha de saída "planilha_output", exemplo:
  - A1: 80356130025 | B1: 730050013 | C1: ANVISA e REFERENCIA ENCONTRADOS!
  - A2: 80356130025 | B2: 730050017 | C2: ANVISA ENCONTRADO E REFERENCIA NÃO ENCONTRADA!
  - A3: 80356131111 | B3: SC-TESTE | C3: ANVISA E REFERENCIA NÃO ENCONTRADOS!


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

## O que deve ser desenvolvido
O projeto deve incluir as seguintes funcionalidades:

- Leitura de um arquivo .xlsx de entrada
- Leitura de um arquivo .xlsx de base
- Cruzamento de dados entre as tabelas de entrada e base
- Geração de um novo arquivo .xlsx de saída com a tabela higienizada
- Além disso, o projeto deve ser capaz de lidar com os seguintes casos:
    - Tabelas com múltiplas abas
    - Tabelas com diferentes tipos de dados nas células (números, texto, data, etc.)

## Contribuições
Este projeto é aberto a contribuições. Se você tiver sugestões de novas funcionalidades ou encontrar um bug, sinta-se à vontade para abrir uma issue ou enviar um pull request.




