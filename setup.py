from setuptools import setup, find_packages


setup(
    name='fez',
    version='0.1',
    packages=find_packages(),
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
