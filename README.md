# Fez
Python script to print all translations of a sentence


## Dependencies

* googletrans
* tableprint
* colored

## Installation

### Using pip

`(sudo) pip install fez`

### From Source

```
git clone https://github.com/mubaris/Fez

cd Fez
```

Using pip:

`pip install .`

or

`python setup.py install`


## Usage

Try to use with words rather than sentences for accurate translations and to avoid bad printing.


```sh
fez -t "your beautiful sentence goes here"
```
For English to all other languages

```sh
fez -t "your beautiful sentence goes here" -x 0
```
For All languages to English

## Screenshot

![Fez Screenshot](https://i.imgur.com/v8lxOHI.png)
