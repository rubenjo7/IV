from fabric.api import *
import os

def info_servidor():
    run ('uname -s')

def descargar():
    run ('sudo rm -rf IV/')
    run ('git clone https://github.com/rubenjo7/IV.git')

def actualizar():
    run ('cd IV/')
    run ('sudo git pull')

def borrar():
    run ('sudo rm -rf IV/')

def testear():
    with shell_env(token_bot=os.environ['token_bot'], usuario_db=os.environ['usuario_db'], password_db=os.environ['password_db'], database_db=os.environ['database_db'], host_db=os.environ['host_db']):
        run ('cd IV/ &&  python p_deportivas_bot/test_p_deportivas_bot.py')

def instalar():
    run ('cd IV/ && pip install -r requirements.txt')

def consultar_contenido():
    run ('cd IV/ && ls -la')

def iniciar():
    with shell_env(token_bot=os.environ['token_bot'], usuario_db=os.environ['usuario_db'], password_db=os.environ['password_db'], database_db=os.environ['database_db'], host_db=os.environ['host_db']):
        run ('sudo supervisorctl start p_deportivas_bot')

def stop():
    run("sudo supervisorctl stop p_deportivas_bot")

def status():
    run("sudo supervisorctl status p_deportivas_bot")

def recargar():
    run("sudo supervisorctl reload")

def logs():
    run("cat IV/log/logs.txt")
