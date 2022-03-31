from config import file_result_path
from utils.list_utils import remove_void


def read_file():
	'''Legge il contenuto del file e ritorna un dizionario con i vari piatti'''
	with open(file_result_path,"r") as file:
		file_content = file.read().replace(",\n",",").replace(" \n"," ").replace(" di\n"," di").replace("&\n","&")
		res_dict = {}
		res_dict['primi'] 		= []#read_primi_piatti(file_content)
		res_dict['secondi'] 	= read_secondi_piatti(file_content)
		res_dict['contorni'] 	= read_contorni_piatti(file_content)
		res_dict['insalatone'] 	= read_insalatone(file_content)
		return res_dict



def read_primi_piatti(file_content:str):
	return remove_void(file_content.split('PRIMEPIATTI')[1].split('SECONDI PIATTI')[0].split("\n"))



def read_secondi_piatti(file_content:str):
	return remove_void(file_content.split('SECONDI PIATTI')[1].split('CONTORNI')[0].split("\n"))



def read_contorni_piatti(file_content:str):
	return remove_void(file_content.split('CONTORNI')[1].split('INSALATONE')[0].split("\n"))



def read_insalatone(file_content:str):
	return remove_void(file_content.split('INSALATONE')[1].split('DESSERT')[0].split("\n"))


if __name__ == '__main__':
	print(read_file())