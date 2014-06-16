from setuptools import setup

setup(
    name='exomondo',
    version='0.1.0',
    description='endomondo.com track downloader and api libraries',
    url='https://github.com/ElvisTheKing/exomondo',
    author='Sergey Konyukhovskiy',
    license='MIT',
    packages=['exomondo'],
    scripts=['bin/exomondo_downloader'],
    install_requires = [
        'click==2.1',
        'requests==2.3.0',
        'splinter==0.6.0'
    ],
)
