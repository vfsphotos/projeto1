# Meu primeiro projeto Django
Este é o meu primeiro projeto Django, que aborda as bases do framework.

## Instrução para baixar, editar e executar local
1. Clone do projeto
```bash
git clone https://github.com/vfsphotos/projeto1.git
```
2. Entre na pasta do projeto e crie um ambiente virtual python
```bash
cd projeto1
```
```bash
python -m venv .venv
```
Caso somente "python" não funcione, faça usando o "python3"

3. Ative o ambiente virtual
no windows:
```bash
.venv\Scripts\activate
```
no linux:
```bash
source .venv/bin/activate
```
4. Instale as dependências
```bash
pip install -r requirements-dev.txt
```
5. Execute as migrações
```bash
python manage.py migrate
```
6. Execute o servidor
```bash
python manage.py runserver
```
7. Acesse o projeto no navegador
```bash
http://127.0.0.1:8000/