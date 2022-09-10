import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluido na pasta final
arquivos = ['captcha.png', 'dados.txt']
# Definir a saida de arquivos
configuracao = Executable(
    script='consulta_expediente.py',
    icon='icon.ico'
)
# Configurar o executável
setup(
    name='Consulta Expediente',
    version='1.0',
    description='Aplicación para consulta telemática de expedientes de nacionalidad',
    author='Phernando',
    options={'build_exe':{
        'include_files': arquivos,
        'include_msvcr': True,     # para rodar no Windows sem instalar python

    }},
    executables=[configuracao]
)