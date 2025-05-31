# mysitebac
Django Personal Blog
Repositório utilizado para teste da aula da Ebac

Este repositório contém um projeto de blog pessoal desenvolvido com Django. O objetivo é demonstrar a criação de um sistema completo de blog, incluindo cadastro e exibição de posts, sistema de comentários com moderação, uso de templates customizados e integração com formulários Django.

## Estrutura do Projeto

- **blog**: Aplicação principal do projeto, contendo os modelos (`Post`, `Comment`), views, formulários e templates.
- **models**: Define as entidades do blog, como Postagens e Comentários.
- **views**: Implementa as páginas de listagem de posts, detalhes de cada post e processamento de comentários.
- **templates**: Contém os arquivos HTML para as páginas do blog, incluindo listagem, detalhes dos posts e sidebar.
- **admin**: Configuração para gerenciamento de posts e comentários via painel administrativo do Django.
- **tests**: Testes automatizados para garantir o funcionamento das principais funcionalidades do blog.
- **requirements.txt**: Lista de dependências necessárias para rodar o projeto.

O projeto utiliza o Django 5.1.6, crispy-forms para estilização dos formulários e pytest para testes automatizados.

---

```
Como preparar seu repositório:
1. Pwd
2. Git clone <link do repositorio>
...
```
1. Pwd
2. Git clone <link do repositorio>
3. Python3 —version
4. Python3 -m venv env
5. Source env/bin/activate
6. Git checkout -b “”project-setup”
7. Pip install Django
8. Django-admin startproject <nome do arquivo novo>
9. Cd <nome da pasta criada>
10. Python manage.py startapp <nome do arquivo novo>
11. Cd <nome da pasta que contém o manage.py>
12. Python manage.py runserver
13. python manage.py makemigrations (precisa estar na pasta onde o arquivo manage.py está)
14. Criando o usuário: Python manage.py created superuser
Username (leave blank to use 'larissayuki'): 
Email address: larissa.iuki@picpay.com
15. Python manage.py shell
16. Python manage.py createsuperuser 