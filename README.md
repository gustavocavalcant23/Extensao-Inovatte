# Inovatte Consultoria — Site Institucional (Projeto de Extensão)

Projeto desenvolvido como atividade de extensão utilizando **Django** para construção de um site institucional moderno, funcional e focado na **captação de leads** e comunicação com clientes.

Site disponível em: https://inovatte-consultoria.onrender.com/

---

## 🚀 Sobre o Projeto

O site oficial da **Inovatte Consultoria**, empresa especializada em:

* Gestão do agronegócio
* Gestão empresarial
* SST (Segurança e Saúde no Trabalho)

O sistema foi desenvolvido com foco em:

* Gerar credibilidade institucional
* Facilitar o contato com potenciais clientes
* Criar um canal direto para envio de newsletters
* Oferecer um ambiente administrativo completo e seguro

---

## 🧩 Principais Funcionalidades

### 🌐 Área Pública

#### **Landing Page Institucional**

* Apresentação da empresa
* Seções sobre as áreas de atuação (agronegócio, empresarial, SST)
* Formulário de contato integrado ao banco de dados
* Captação e armazenamento de leads

#### **📬 Inscrição na Newsletter**

* Página dedicada para inscrição via e-mail
* Validação dos dados
* Registro seguro no painel administrativo
* Canal para comunicação recorrente

---

### 🔐 Área Administrativa

Ambiente administrativo modernizado com **Django Jazzmin**, oferecendo uma interface intuitiva e responsiva.

#### **📑 Gestão de Contatos**

* Listagem de mensagens recebidas
* Marcação de mensagens como lidas
* Organização e controle de leads

#### **👥 Gestão da Newsletter**

* Listagem de e-mails cadastrados
* Edição/remoção de inscrições
* Envio manual de newsletters diretamente pelo admin

#### **⚙️ Configurações Gerais**

* Controle de usuários e permissões
* Personalização via Jazzmin
* Gerenciamento de todos os modelos do projeto

---

## 🛠️ Tecnologias Utilizadas

* Python 3.11.3
* Django 5.2.8
* Django Jazzmin
* HTML5 / CSS3 / JavaScript
* SQLite / PostgreSQL
* Django Forms & ModelForms
* Brevo / API para envio de Emails

---

## ▶️ Como clonar e executar localmente

Siga este passo a passo para rodar o projeto na sua máquina local (assumindo que você tenha Git e Python 3.11+ instalados):

1. **Clonar o repositório**

```bash
git clone https://github.com/gustavocavalcant23/Extensao-Inovatte/tree/main
cd SEU_REPOSITORIO
```

2. **Criar e ativar um ambiente virtual** (recomendado)

No Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. **Instalar dependências**

```bash
pip install -r requirements.txt
```

4. **Configurar variáveis de ambiente**

Altere o arquivo `.env` (ou configure conforme sua preferência) com chaves mínimas:

5. **Aplicar migrações**

```bash
python manage.py migrate
```

6. **Criar superusuário**

```bash
python manage.py createsuperuser
```

7. **Coletar arquivos estáticos (quando aplicável)**

```bash
python manage.py collectstatic --noinput
```

8. **Rodar o servidor de desenvolvimento**

```bash
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000/` para a área pública e `http://127.0.0.1:8000/admin/` para o painel administrativo.

---

## Mais Informações

* Esse projeto foi desenvolvido para fins educacionais como um projeto de extensão universitário.
* As funções de envio de Email foram alteradas para manter a privacidade e segurança da empresa.
* O projeto já está deployado em produção utilizando a plataforma Render, garantindo alta disponibilidade e fácil manutenção.
* O site em produção pode ser acessado pelo link `https://inovatte-consultoria.onrender.com`
