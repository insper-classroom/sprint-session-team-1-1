[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11138757&assignment_repo_type=AssignmentRepo)
# Sprint Session Projeto para Fundação Telles - Grupo 1

Esse projeto tem como objetivo criar um sistema para automatizar o acompanhamento dos bolsistas Telles Scholars, tanto os atuais quanto os alumni.

## Descrição do sistema

O sistema de acompanhamento dos bolsistas Telles Scholars foi desenvolvido para facilitar o registro e o monitoramento dos bolsistas atuais e alumni. Ele permite acompanhar informações relevantes sobre esses usuários, como seus dados pessoais, histórico acadêmico, histórico profissional e conquistas.

Principais recursos do sistema:
- Cadastro de novos usuários.
- Atualização das informações dos usuários.
- Acompanhamento e vizualização desses perfis.
- Simples interação com os componentes do sistema.

## Como executar

Para executar o servidor local, é necessário ter o Python 3 instalado na máquina. Clone este repositório e execute o comando abaixo para instalar as dependências:

Repositório: 

Comando para instalar todas as dependências:
```
pip install -r requirements.txt
```

Após instalar as dependências, execute o servidor local com:

```
python manage.py runserver
```

Por fim, abra o seu navegador e acesse a seguinte URL para ver a página inicial do sistema.:
```
http://localhost:8000/
```

## Guia do serviço

Ao executar seu sistema, você provavelmente não sera capaz de fazer nada alem de ver a tela de inicio e login.
Para iniciar o processo, utilize o comando "python manage.py cratesuperuser" para criar um usuario de Admin.

Tendo seu usuario de Admin preparado, entre em http://localhost:8000/admin e logue. Agora, você deve criar um novo usuario
e classificar seu "Tipo de Usuario", na aba profile do user, como "Colaborador ou admin". Lembre-se de usar infos validas.
(Isto é uma medida de segurança, contas importantes de funcionarios, moderadores e parceiros só podem ser criadas por contas mestras)

Após isso você ja deve ser capaz de, normalmente, logar e ver o sistema como um funcionario. Para criar usuarios de Bolsistas/ALumnis
(para testes ou para verdadeiros alunos), entre no link http://localhost:8000/generate (ou clique em 'gerar link' no seu profile).

Neste endereço, você ira ver uma key criada que libera o acesso para a criação de contas.
(Caso esteja utilizando outro host que não o localhost, basta substituir, o importante é a key após o /signup/). Isto se trata de
uma função criada a pedido da teles para que cada usuario tenha um link de uso unico para criar sua conta, assim impedindo externos de
entrarem no sistema.

Com esta key, acesse "http://localhost:8000/accounts/signup/* key *" para criar um novo usuario, que sera automaticamente identificado
como bolsista ou Alumni. Após este ponto, basta encher o servidor de usuarios.

## Conta de Admin

Na criação do deploy do app, criamos uma conta de admin no server da AWS, seguem as informações:
Nome: admin
Email: admin@admin.com
senha: admin

Lembrete: Este commit após a data limite (sexta feira) se trata apenas desse guia de serviço adicionado no Readme, nenhuma mudança
técnica. Apenas sentimos que era necessario após fazermos o deploy.

## Modelo inicial do projeto

Link dos primeiros protótipos de design do projeto:
https://www.canva.com/design/DAFi_NcwNwQ/A7esW5kU9ntsACHlWm5NOA/edit?utm_content=DAFi_NcwNwQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Referências

Aqui estão as referências utilizadas para desenvolver e aprimorar o funcionamento do sistema de acompanhamento dos bolsistas Telles Scholars:

1. Título: "Django Celery, Celery Beat, Redis | Base Setup | Everything about using celery with Django"
   Link: [https://www.youtube.com/watch?v=EfWa6KH8nVI&t=454s](https://www.youtube.com/watch?v=EfWa6KH8nVI&t=454s)

2. Título: "Sending Emails in Django using Celery | Django SMTP Settings | Send emails from an endpoint"
   Link: [https://www.youtube.com/watch?v=JYQG7zlLJrE](https://www.youtube.com/watch?v=JYQG7zlLJrE)

3. Título: "Django Celery Beat | Periodic Tasks | Celery Dynamic Tasks | Crontab | Email Scheduler"
   Link: [https://www.youtube.com/watch?v=vplXie0uOz8](https://www.youtube.com/watch?v=vplXie0uOz8)

4. Título: "GOOGLE LOGIN | DJANGO ALLAUTH"
   Link: [https://www.youtube.com/watch?v=qdOX-6Zhugs&t=40s](https://www.youtube.com/watch?v=qdOX-6Zhugs&t=40s)

5. Título: "AUTENTICAÇÃO PROFISSIONAL COM DJANGO | ALLAUTH"
   Link: [https://www.youtube.com/watch?v=Q4Q3S7HLp4w&t=200s](https://www.youtube.com/watch?v=Q4Q3S7HLp4w&t=200s)

6. Título: "#30 Python e Django - Criar um perfil de usuário com CPF, RG, telefone, endereço, etc"
   Link: [https://www.youtube.com/watch?v=4m8bhZTAGvI](https://www.youtube.com/watch?v=4m8bhZTAGvI)

7. Título: "#31 Python e Django - Editar os dados do perfil do usuário e exibir seus dados em qualquer template"
   Link: [https://www.youtube.com/watch?v=IgNhQPJ0FY8](https://www.youtube.com/watch?v=IgNhQPJ0FY8)

8. Título: "Add A Favicon to A Website in HTML | Learn HTML and CSS | HTML Tutorial | HTML for Beginners"
   Link: [https://www.youtube.com/watch?v=kEf1xSwX5D8](https://www.youtube.com/watch?v=kEf1xSwX5D8)

9. Título: "Formulários com PYTHON e DJANGO | Aula retirada da PYTHON FULL | Aula semanal #8"
   Link: [https://www.youtube.com/watch?v=yVlGqV9kkas&t=26s](https://www.youtube.com/watch?v=yVlGqV9kkas&t=26s)

10. Título: "Multi Step Form With Progress bar Using HTML, CSS & JavaScript [Project 32/100]"
   Link: [https://www.youtube.com/watch?v=JFfVilQSius&t=236s](https://www.youtube.com/watch?v=JFfVilQSius&t=236s)

11. Título: "DJANGO CUSTOM ADMIN | Learn how to make a custom admin panel in django | Admin Theme Series #01"
   Link: [https://www.youtube.com/watch?v=a9F_fN6pGyo](https://www.youtube.com/watch?v=a9F_fN6pGyo)

12. Título: "How to make User History in Django | Advance Django Tutorials - #8"
   Link: [https://www.youtube.com/watch?v=latCmyZyuiE&t=654s](https://www.youtube.com/watch?v=latCmyZyuiE&t=654s)

13. Título: "How To Write a USEFUL README On Github"
   Link: [https://www.youtube.com/watch?v=E6NO0rgFub4&t=63s](https://www.youtube.com/watch?v=E6NO0rgFub4&t=63s)

14. Título: "AUTENTICAÇÃO PROFISSIONAL COM DJANGO | ALLAUTH"
   Link: [https://www.youtube.com/watch?v=Q4Q3S7HLp4w](https://www.youtube.com/watch?v=Q4Q3S7HLp4w)

15. Título: "GOOGLE LOGIN | DJANGO ALLAUTH"
   link: [https://www.youtube.com/watch?v=qdOX-6Zhugs] (https://www.youtube.com/watch?v=qdOX-6Zhugs)

16. Título: "How To Make A Website With Login And Register | HTML CSS & Javascript"
   link: [https://www.youtube.com/watch?v=p1GmFCGuVjw] (https://www.youtube.com/watch?v=p1GmFCGuVjw)
   
Esses vídeos foram referências importantes no desenvolvimento do projeto.

Aqui estão os sites que foram úteis para obter mais informações e recursos relacionados ao nosso sistema de acompanhamento para a Fundação Telles:

1. Título: "Django Documentation"
   Link: [https://docs.djangoproject.com/en/3.2/](https://docs.djangoproject.com/en/3.2/)

2. Título: "Django Allauth Documentation"
    Link: [https://django-allauth.readthedocs.io/en/latest/](https://django-allauth.readthedocs.io/en/latest/)

3. Título: "Jazzmin Documentation"
    Link: [https://django-jazzmin.readthedocs.io/](https://django-jazzmin.readthedocs.io/)

## Autores

- Diego Henrique Yamashitafuji. E-mail para contato: <diegohy@al.insper.edu.br>

- Gustavo Colombi Ribolla. E-mail para contato: <gustavocr2@al.insper.edu.br>

- Henrique Turco Gera. E-mail para contato: <henriquetg1@al.insper.edu.br>

- Joao Pedro Gardenal Sarti. E-mail para contato: <joaopgs4@al.insper.edu.br>

- Luigi Orlandi Quinze. E-mail para contato: <luigioq@al.insper.edu.br>

- Thiago de Miranda e Silva. E-mail para contato: <thiagoms9@al.insper.edu.br>