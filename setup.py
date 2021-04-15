from distutils.core import setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name='isdayoff',
    version='0.1.0',
    author='KlukvaMors',
    author_email='mkv-1724@mail.ru',
    packages=['isdayoff.isdayoff'],
    license='LICENSE.md',
    description='Обёртка на API https://isdayoff.ru/',
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=[
        "certifi >= 2020.4.5.2",
        "chardet >= 3.0.4",
        "idna >= 2.9",
        "requests >= 2.23.0",
        "urllib3 >= 1.25.9"
    ],
)