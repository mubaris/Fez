#!/usr/bin/python3

import sys
import argparse

from googletrans import Translator
from colored import stylize
import colored
import tableprint as tp
from prettytable import PrettyTable

from .constants import LANGUAGES


def translate():
    parser = argparse.ArgumentParser(description="Welcome to Fez")

    parser.add_argument("-t", action="store", required=True, help="Your Beautiful Sentence")
    parser.add_argument("-x", help="1 for English to all and 0 for all to English", default=1)

    args = parser.parse_args()

    sentence = args.t
    en_to_all = bool(int(args.x))

    x = PrettyTable()

    headers = [stylize("Text", colored.fg("blue")),
                stylize("Pronounciation", colored.fg("blue")),
                stylize("Language", colored.fg("blue"))]

    x.field_names = headers

    cell_width = max(20, int(2.5 * len(sentence)))
    #print(tp.header(headers, width=cell_width))
    translator = Translator()
    for code, lang in LANGUAGES.items():
        if en_to_all:
            translation = translator.translate(sentence, dest=code)
        else:
            translation = translator.translate(sentence, src=code, dest='en')
        output_text = translation.text
        output_pron = translation.pronunciation
        if not output_pron:
            output_pron = output_text
        line_list = [output_text, stylize(output_pron, colored.fg("yellow")), stylize(lang, colored.fg("green"))]
        #print(tp.row(line_list, width=cell_width), flush=True)
        x.add_row(line_list)

    #print(tp.bottom(3, width=cell_width))
    x.padding_width = int(cell_width / 5)
    print(x)
