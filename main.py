from utils.image_converter import convert
from utils.menu_reader import read_file
from utils.list_utils import pretty_print

response = convert('images/2022-03-28.jpg')
if (response):
	print("conversione in testo effettuata")
	res_dict = read_file()
	pretty_print(res_dict)
else:
	print("Errore")