import sys

from googletrans import Translator
from colored import stylize
import colored
import tableprint as tp

from constants import LANGUAGES

if len(sys.argv) < 2:
	print("Please specify atleast one word")
	sys.exit()
else:
	args = sys.argv[1:]
	sentence = ' '.join(args)

headers = [stylize("Text", colored.fg("blue")),
			stylize("Pronounciation", colored.fg("blue")),
			stylize("Language", colored.fg("blue"))]

cell_width = int(4 * len(sentence))
print(tp.header(headers, width=cell_width))
output = []
translator = Translator()
for code, lang in LANGUAGES.items():
	translation = translator.translate(sentence, dest=code)
	output_text = translation.text
	output_pron = translation.pronunciation
	if not output_pron:
		output_pron = output_text
	line_list = [output_text, stylize(output_pron, colored.fg("yellow")), stylize(lang, colored.fg("green"))]
	print(tp.row(line_list, width=cell_width), flush=True)

print(tp.bottom(3, width=cell_width))