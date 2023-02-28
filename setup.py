'''
Este archivo configura este proyecto para que se pueda convertir en un paquete de python
y así poder instalarlo en tu sistema
la dirección que tienes que poner dentro de entry_points=["console_scripts":{paquete.modulo:funcion}]
Una vez que hayas terminado escribe en consola python setup.py develop
ahora lo puedes ejecuta escribiendo text2mp3 y lo puedes importar en otro proyecto
para desistalar el paquete: pip uninstall nombrepaquete 
'''

from setuptools import setup, find_packages


setup(
    name='text2mp3',
    version='0.1',
    author='benrutter',
    description='Text to speed tipolisto',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/kikemadrigal/text2mp3',
    entry_points={
        'console_scripts': [
            'text2mp3 = text2mp3.text2mp3:convert',
        ],
    },
    install_requires=[
        'pyttsx3',
    ],
    keywords="text, speed,mp3 ",
    packages=find_packages(where="src"),
    package_dir={"":"src", "text2mp3":"src/text2mp3"},
)
