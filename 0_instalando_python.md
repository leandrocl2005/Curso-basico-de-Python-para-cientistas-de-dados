# Instalando o Python e preparando o ambiente

- Faça o download: https://www.python.org/downloads/


- Crie o ambiente digitando no terminal: `C:/<PATH_PYTHON>/python -m venv env`
- Ative o ambiente digitando no terminal: `. env/Scripts/activate`
- Caso queira desativar, no terminal, digite: `deactivate`
- Atualize o pip digitando no terminal:
```bash
C:\<PATH_PYTHON>\python.exe -m pip install --upgrade pip
```
- Instale as dependências digitando no terminal:
```bash
pip install notebook
pip install matplotlib
pip install -U scikit-learn
pip install pandas
```
- Para criar o arquivo _requirements.txt_ digite no terminal: `pip freeze > requirements.txt`
- Por fim copie e cole o arquivo _.gitignore_ deste repositório na sua pasta.


