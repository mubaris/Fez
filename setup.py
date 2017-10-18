from setuptools import setup, find_packages


setup(
    name='fez',
    version='0.1',
    packages=find_packages(),
    author='Mubaris NK',
    author_email = 'mubarishassannk@gmail.com',
    url='https://github.com/mubaris/Fez',
    keywords = ['translate', 'google'],
    download_url='https://github.com/mubaris/Fez/archive/0.1.tar.gz',
    install_requires=[
        'googletrans==2.2.0',
        'tableprint==0.7.0',
        'colored==1.3.5',
    ],
    entry_points='''
        [console_scripts]
        fez=fez.Fez:translate
    '''
)
