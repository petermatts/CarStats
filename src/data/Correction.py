# Automatically generated file - DO NOT EDIT


#from Corrections import *
from Corrections.Acura import Acura_Corrections
from Corrections.AlfaRomeo import AlfaRomeo_Corrections
from Corrections.AstonMartin import AstonMartin_Corrections
from Corrections.Audi import Audi_Corrections
from Corrections.Bentley import Bentley_Corrections
from Corrections.BMW import BMW_Corrections
from Corrections.Buick import Buick_Corrections
from Corrections.Cadillac import Cadillac_Corrections
from Corrections.Chevrolet import Chevrolet_Corrections
from Corrections.Chrysler import Chrysler_Corrections
from Corrections.Dodge import Dodge_Corrections
from Corrections.Ferrari import Ferrari_Corrections
from Corrections.Fiat import Fiat_Corrections
from Corrections.Fisker import Fisker_Corrections
from Corrections.Ford import Ford_Corrections
from Corrections.Genesis import Genesis_Corrections
from Corrections.GMC import GMC_Corrections
from Corrections.Honda import Honda_Corrections
from Corrections.Hummer import Hummer_Corrections
from Corrections.Hyundai import Hyundai_Corrections
from Corrections.Infiniti import Infiniti_Corrections
from Corrections.Jaguar import Jaguar_Corrections
from Corrections.Jeep import Jeep_Corrections
from Corrections.Karma import Karma_Corrections
from Corrections.Kia import Kia_Corrections
from Corrections.Lamborghini import Lamborghini_Corrections
from Corrections.LandRover import LandRover_Corrections
from Corrections.Lexus import Lexus_Corrections
from Corrections.Lincoln import Lincoln_Corrections
from Corrections.Lordstown import Lordstown_Corrections
from Corrections.Lotus import Lotus_Corrections
from Corrections.Maserati import Maserati_Corrections
from Corrections.Mazda import Mazda_Corrections
from Corrections.McLaren import McLaren_Corrections
from Corrections.MercedesAMG import MercedesAMG_Corrections
from Corrections.MercedesBenz import MercedesBenz_Corrections
from Corrections.MercedesMaybach import MercedesMaybach_Corrections
from Corrections.Mercury import Mercury_Corrections
from Corrections.Mini import Mini_Corrections
from Corrections.Mitsubishi import Mitsubishi_Corrections
from Corrections.Nissan import Nissan_Corrections
from Corrections.Polestar import Polestar_Corrections
from Corrections.Pontiac import Pontiac_Corrections
from Corrections.Porsche import Porsche_Corrections
from Corrections.Ram import Ram_Corrections
from Corrections.Rivian import Rivian_Corrections
from Corrections.RollsRoyce import RollsRoyce_Corrections
from Corrections.Saab import Saab_Corrections
from Corrections.Saturn import Saturn_Corrections
from Corrections.Scion import Scion_Corrections
from Corrections.Smart import Smart_Corrections
from Corrections.Subaru import Subaru_Corrections
from Corrections.Suzuki import Suzuki_Corrections
from Corrections.Tesla import Tesla_Corrections
from Corrections.Toyota import Toyota_Corrections
from Corrections.VinFast import VinFast_Corrections
from Corrections.Volkswagen import Volkswagen_Corrections
from Corrections.Volvo import Volvo_Corrections


class Correction():
	"""
	Correction object containing helper objects and functions to correct data
	during the conversion from JSON to CSV format
	"""

	def __init__(self):
		"""
		Initialize the Correction object and its helpers
		"""

		self._Acura = Acura_Corrections()
		self._AlfaRomeo = AlfaRomeo_Corrections()
		self._AstonMartin = AstonMartin_Corrections()
		self._Audi = Audi_Corrections()
		self._Bentley = Bentley_Corrections()
		self._BMW = BMW_Corrections()
		self._Buick = Buick_Corrections()
		self._Cadillac = Cadillac_Corrections()
		self._Chevrolet = Chevrolet_Corrections()
		self._Chrysler = Chrysler_Corrections()
		self._Dodge = Dodge_Corrections()
		self._Ferrari = Ferrari_Corrections()
		self._Fiat = Fiat_Corrections()
		self._Fisker = Fisker_Corrections()
		self._Ford = Ford_Corrections()
		self._Genesis = Genesis_Corrections()
		self._GMC = GMC_Corrections()
		self._Honda = Honda_Corrections()
		self._Hummer = Hummer_Corrections()
		self._Hyundai = Hyundai_Corrections()
		self._Infiniti = Infiniti_Corrections()
		self._Jaguar = Jaguar_Corrections()
		self._Jeep = Jeep_Corrections()
		self._Karma = Karma_Corrections()
		self._Kia = Kia_Corrections()
		self._Lamborghini = Lamborghini_Corrections()
		self._LandRover = LandRover_Corrections()
		self._Lexus = Lexus_Corrections()
		self._Lincoln = Lincoln_Corrections()
		self._Lordstown = Lordstown_Corrections()
		self._Lotus = Lotus_Corrections()
		self._Maserati = Maserati_Corrections()
		self._Mazda = Mazda_Corrections()
		self._McLaren = McLaren_Corrections()
		self._MercedesAMG = MercedesAMG_Corrections()
		self._MercedesBenz = MercedesBenz_Corrections()
		self._MercedesMaybach = MercedesMaybach_Corrections()
		self._Mercury = Mercury_Corrections()
		self._Mini = Mini_Corrections()
		self._Mitsubishi = Mitsubishi_Corrections()
		self._Nissan = Nissan_Corrections()
		self._Polestar = Polestar_Corrections()
		self._Pontiac = Pontiac_Corrections()
		self._Porsche = Porsche_Corrections()
		self._Ram = Ram_Corrections()
		self._Rivian = Rivian_Corrections()
		self._RollsRoyce = RollsRoyce_Corrections()
		self._Saab = Saab_Corrections()
		self._Saturn = Saturn_Corrections()
		self._Scion = Scion_Corrections()
		self._Smart = Smart_Corrections()
		self._Subaru = Subaru_Corrections()
		self._Suzuki = Suzuki_Corrections()
		self._Tesla = Tesla_Corrections()
		self._Toyota = Toyota_Corrections()
		self._VinFast = VinFast_Corrections()
		self._Volkswagen = Volkswagen_Corrections()
		self._Volvo = Volvo_Corrections()


	def fix(self, data: dict, brand: str) -> dict:
		"""
		Calls helper class fix functions to correct dictionoary of data passed in. Returns corrected data dictionary
		"""

		match brand:
			case "Acura":
				return self._Acura.fix(data)
			case "AlfaRomeo":
				return self._AlfaRomeo.fix(data)
			case "AstonMartin":
				return self._AstonMartin.fix(data)
			case "Audi":
				return self._Audi.fix(data)
			case "Bentley":
				return self._Bentley.fix(data)
			case "BMW":
				return self._BMW.fix(data)
			case "Buick":
				return self._Buick.fix(data)
			case "Cadillac":
				return self._Cadillac.fix(data)
			case "Chevrolet":
				return self._Chevrolet.fix(data)
			case "Chrysler":
				return self._Chrysler.fix(data)
			case "Dodge":
				return self._Dodge.fix(data)
			case "Ferrari":
				return self._Ferrari.fix(data)
			case "Fiat":
				return self._Fiat.fix(data)
			case "Fisker":
				return self._Fisker.fix(data)
			case "Ford":
				return self._Ford.fix(data)
			case "Genesis":
				return self._Genesis.fix(data)
			case "GMC":
				return self._GMC.fix(data)
			case "Honda":
				return self._Honda.fix(data)
			case "Hummer":
				return self._Hummer.fix(data)
			case "Hyundai":
				return self._Hyundai.fix(data)
			case "Infiniti":
				return self._Infiniti.fix(data)
			case "Jaguar":
				return self._Jaguar.fix(data)
			case "Jeep":
				return self._Jeep.fix(data)
			case "Karma":
				return self._Karma.fix(data)
			case "Kia":
				return self._Kia.fix(data)
			case "Lamborghini":
				return self._Lamborghini.fix(data)
			case "LandRover":
				return self._LandRover.fix(data)
			case "Lexus":
				return self._Lexus.fix(data)
			case "Lincoln":
				return self._Lincoln.fix(data)
			case "Lordstown":
				return self._Lordstown.fix(data)
			case "Lotus":
				return self._Lotus.fix(data)
			case "Maserati":
				return self._Maserati.fix(data)
			case "Mazda":
				return self._Mazda.fix(data)
			case "McLaren":
				return self._McLaren.fix(data)
			case "MercedesAMG":
				return self._MercedesAMG.fix(data)
			case "MercedesBenz":
				return self._MercedesBenz.fix(data)
			case "MercedesMaybach":
				return self._MercedesMaybach.fix(data)
			case "Mercury":
				return self._Mercury.fix(data)
			case "Mini":
				return self._Mini.fix(data)
			case "Mitsubishi":
				return self._Mitsubishi.fix(data)
			case "Nissan":
				return self._Nissan.fix(data)
			case "Polestar":
				return self._Polestar.fix(data)
			case "Pontiac":
				return self._Pontiac.fix(data)
			case "Porsche":
				return self._Porsche.fix(data)
			case "Ram":
				return self._Ram.fix(data)
			case "Rivian":
				return self._Rivian.fix(data)
			case "RollsRoyce":
				return self._RollsRoyce.fix(data)
			case "Saab":
				return self._Saab.fix(data)
			case "Saturn":
				return self._Saturn.fix(data)
			case "Scion":
				return self._Scion.fix(data)
			case "Smart":
				return self._Smart.fix(data)
			case "Subaru":
				return self._Subaru.fix(data)
			case "Suzuki":
				return self._Suzuki.fix(data)
			case "Tesla":
				return self._Tesla.fix(data)
			case "Toyota":
				return self._Toyota.fix(data)
			case "VinFast":
				return self._VinFast.fix(data)
			case "Volkswagen":
				return self._Volkswagen.fix(data)
			case "Volvo":
				return self._Volvo.fix(data)
			case _:
				# default case
				raise ValueError("Invalid brand " + brand)
