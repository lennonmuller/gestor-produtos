## 📊 Gestor de Produtos - Aplicação Desktop

## 📝 Sobre o Projeto
O "Gestor de Produtos" é uma aplicação desktop desenvolvida em Python como projeto de conclusão do curso de programação. A solução simula um sistema de gerenciamento de inventário, permitindo registrar, visualizar, atualizar e deletar produtos de forma intuitiva e persistente, com todos os dados armazenados em um banco de dados relacional SQLite.
Este projeto representa a aplicação prática de conceitos fundamentais de desenvolvimento de software, incluindo programação orientada a objetos, design de interfaces gráficas (GUI) e manipulação de banco de dados.
## ✨ Funcionalidades Principais
Interface Gráfica Intuitiva: Interface limpa e funcional construída com a biblioteca nativa Tkinter, facilitando a interação do usuário.
Operações CRUD Completas:
Criar: Adicionar novos produtos ao catálogo com informações de nome, descrição e preço.
Read: Listar todos os produtos existentes em tempo real em uma visualização em tabela.
Update: Selecionar e editar informações de produtos já cadastrados.
Delete: Selecionar e remover produtos do catálogo de forma permanente.
Persistência de Dados: Utilização do SQLite para garantir que os dados sejam armazenados de forma segura e eficiente, mantendo o estado da aplicação entre as sessões.
Validação de Entradas: Implementação de verificações básicas para garantir a integridade dos dados inseridos, como campos não vazios.
## 🛠️ Tecnologias Utilizadas
Python 3: Linguagem principal para toda a lógica de negócios e estruturação da aplicação.
Tkinter: Biblioteca nativa do Python, utilizada para a construção da interface gráfica do usuário (GUI), garantindo leveza e portabilidade.
SQLite 3: Sistema de gerenciamento de banco de dados relacional leve e serverless, ideal para aplicações desktop, responsável pelo armazenamento dos dados dos produtos.
DB Browser for SQLite: Ferramenta auxiliar utilizada durante o desenvolvimento para a modelagem, criação e verificação da estrutura do banco de dados.


## 🌱 Desafios e Aprendizados
Desenvolver o "Gestor de Produtos" foi uma jornada de aprendizado significativa. Alguns dos principais desafios e lições aprendidas incluem:
Integração do Back-end com o Front-end (Tkinter): O maior desafio foi conectar a lógica de manipulação de dados com os componentes visuais da interface. Aprender a gerenciar o estado da aplicação e a atualizar a visualização da lista de produtos em tempo real após cada operação CRUD foi fundamental.
Estruturação do Código: Inicialmente, o código estava em um único script. A refatoração para separar as responsabilidades (ex: uma classe para a interface, outra para as operações de banco de dados) foi um passo crucial para tornar o projeto mais legível, manutenível e escalável.
Modelagem de Dados: A decisão sobre quais campos incluir na tabela de produtos e como definir a chave primária foi um excelente exercício prático de modelagem de banco de dados relacional.
## 📈 Melhorias Futuras e Visão de Carreira
Este projeto serviu como uma base sólida em desenvolvimento de software. Como um profissional com grande interesse na intersecção entre software e dados, meu objetivo é evoluir este projeto e minhas habilidades na direção de Análise e Engenharia de Dados.
As próximas etapas planejadas são:
Implementação de um Dashboard Simples: Adicionar uma nova aba à aplicação que utilize bibliotecas como Matplotlib e Seaborn para visualizar dados agregados, como:
Gráfico de barras com os 5 produtos mais caros.
Gráfico de pizza mostrando a distribuição de produtos por categoria (exigiria adicionar um campo "categoria").
Funcionalidade de Busca e Filtro: Permitir que o usuário pesquise produtos por nome ou filtre por faixas de preço.
Geração de Relatórios: Adicionar um botão para exportar a lista atual de produtos para um arquivo .csv ou .pdf, uma funcionalidade comum em sistemas de gestão.
Refatoração para uma API REST: Como um desafio maior, planejo desacoplar a lógica de negócios em uma API RESTful usando Flask ou FastAPI. Isso permitiria que os dados fossem consumidos não apenas por esta aplicação desktop, mas também por um futuro front-end web, por exemplo.
## 👨‍💻 Autor
<img src="https://avatars.githubusercontent.com/u/lennonmuller?v=4" width="100px;"/><br /><sub><b>Lennon Muler</b></sub>
Desenvolvedor Python em transição de carreira, com foco em construir soluções de software eficientes e com grande interesse em Análise de Dados.

## 🚀 Como Executar o Projeto
Para executar este projeto localmente, siga os passos abaixo.
1. Clonar o repositório:
```bash
# 1. Clone o repositório para sua máquina local
git clone https://github.com/lennon-souza/gestor-de-produtos.git

# 2. Navegue até o diretório do projeto
cd gestor-de-produtos

# 3. (Opcional, mas recomendado) Crie e ative um ambiente virtual
# Isso isola as dependências do projeto.
python -m venv venv

# No Windows:
venv\Scripts\activate

# No macOS/Linux:
source venv/bin/activate

# 4. Execute a aplicação
# O Python 3 e o Tkinter já vêm instalados na maioria dos sistemas.
# Nenhum pacote adicional é necessário.
python main.py
Use code with caution.
```
