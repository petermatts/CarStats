# Automatically generated file template

import re

from Correction_Template import Correction_Template

class Hyundai_Corrections(Correction_Template):
	"""
	Helper class for Hyundai corrections
	"""

	def fix(self, data: dict[str, str]) -> dict:
		"""
		Makes corrections to the data entry dict

		To make corrections implement the case setting `result[k]` to the corrected value
		"""
		result = data.copy()

		for k in data.keys():
			match k:
				case "Price":
					pass #Implement this if necessary
				case "Year":
					pass #Implement this if necessary
				case "Brand":
					pass #Implement this if necessary
				case "Model":
					match result[k]:
						case "accent":
							result[k] = "Accent"
						case "azera":
							result[k] = "Azera"
						case "elantra"|"elantra-gt"|"elantra-n"|"elantra-sport"|"elantra-touring":
							result[k] = "Elantra"
						case "entourage":
							result[k] = "Entourage"
						case "equus":
							result[k] = "Equus"
						case "genesis"|"genesis-coupe":
							result[k] = "Genesis"
						case "ioniq"|"ioniq-electric":
							result[k] = "Ioniq"
						case "ioniq-5":
							result[k] = "Ioniq 5"
						case "ioniq-6":
							result[k] = "Ioniq 6"
						case "kona"|"kona-electric"|"kona-n":
							result[k] = "Kona"
						case "nexo":
							result[k] = "Nexo"
						case "palisade":
							result[k] = "Palisade"
						case "santa-cruz":
							result[k] = "Santa Cruz"
						case "santa-fe"|"santa-fe-sport":
							result[k] = "Santa Fe"
						case "sonata":
							result[k] = "Sonata"
						case "tiburon":
							result[k] = "Tiburon"
						case "tucson"|"tucson-hybrid":
							result[k] = "Tucson"
						case "veloster"|"veloster-n":
							result[k] = "Veloster"
						case "venue":
							result[k] = "Venue"
						case "veracruz":
							result[k] = "Veracruz"
				case "Style":
					result[k] = re.sub(r"(P|p)lug-(I|i)n (H|h)ybrid", "PHEV", result[k])
					result[k] = result[k].replace("hybrid", "Hybrid")
					result[k] = result[k].replace("coupe", "Coupe")
					result[k] = result[k].replace("sedan", "Sedan")
					result[k] = result[k].replace("electric", "Electric")

					s = re.search(r"(Sedan|Coupe|Hybrid|PHEV|N|Electric)", result[k])
					if s is not None:
						result[k] = result[k][s.span()[0]:s.span()[1]]
					else:
						result[k] = ""

					if "HB" in result["Trim"] or "Hatchback" in result["Trim"]:
						result[k] = (result[k] + " Hatchback").lstrip()

				case "Trim":
					if "Ltd" in result[k]:
						result[k] = result[k].replace("Ltd", "Limited") #? is this an accurate thing to do

					t = re.search(r"((Limited|Sport|SEL|GS|GT|GLS|Eco|N Line|Night|Turbo|Ultimate|XL|SE|Base|R-Spec|(Grand )?Touring|Premium|Track|GL|Calligraphy|Blue|(Value|Walking Dead) Edition) ?)+", result[k])
					if t is not None:
						trim = result[k][t.span()[0]:t.span()[1]].strip()
						result[k] = trim
					else:
						result[k] = ""
				case "Drivetrain":
					pass #Implement this if necessary
				case "EPA Class":
					pass #Implement this if necessary
				case "Engine":
					pass #Implement this if necessary
				case "Engine Order Code":
					pass #Implement this if necessary
				case "Maximum Engine Speed (rpm)":
					pass #Implement this if necessary
				case "Turbo":
					pass #Implement this if necessary
				case "Displacement (Liters)":
					pass #Implement this if necessary
				case "Max Horsepower":
					pass #Implement this if necessary
				case "Max Horsepower RPM":
					pass #Implement this if necessary
				case "Max Torque":
					pass #Implement this if necessary
				case "Max Torque RPM":
					pass #Implement this if necessary
				case "Fuel System":
					pass #Implement this if necessary
				case "Engine Oil Cooler":
					pass #Implement this if necessary
				case "Cooling System Capacity (quarts)":
					pass #Implement this if necessary
				case "Maximum Alternator Capacity (amps)":
					pass #Implement this if necessary
				case "Cold Cranking Amps @ 0� F":
					pass #Implement this if necessary
				case "Cold Cranking Amps @ 0� F (2nd)":
					pass #Implement this if necessary
				case "Transmission":
					result[k] = re.sub(r" (S|s)hift", "", result[k])
					result[k] = re.sub(r"Continuously (V|v)ariable( (R|r)atio)?", "CVT", result[k])
					result[k] = result[k].replace("automatic", "Automatic")
					result[k] = result[k].replace("manual", "Manual")
					result[k] = re.sub(r"\s+", " ", result[k])
				case "Transmission Type":
					pass #Implement this if necessary
				case "Transmission Speeds":
					pass #Implement this if necessary
				case "Transmission Manufacturer":
					pass #Implement this if necessary
				case "Transmission Order Code":
					pass #Implement this if necessary
				case "First Gear Ratio (:1)":
					pass #Implement this if necessary
				case "Second Gear Ratio (:1)":
					pass #Implement this if necessary
				case "Third Gear Ratio (:1)":
					pass #Implement this if necessary
				case "Fourth Gear Ratio (:1)":
					pass #Implement this if necessary
				case "Fifth Gear Ratio (:1)":
					pass #Implement this if necessary
				case "Sixth Gear Ratio (:1)":
					pass #Implement this if necessary
				case "Seventh Gear Ratio (:1)":
					pass #Implement this if necessary
				case "Eighth Gear Ratio (:1)":
					pass #Implement this if necessary
				case "Ninth Gear Ratio (:1)":
					pass #Implement this if necessary
				case "Tenth Gear Ratio (:1)":
					pass #Implement this if necessary
				case "Reverse Ratio (:1)":
					pass #Implement this if necessary
				case "Fuel":
					pass #Implement this if necessary
				case "MPG (city)":
					pass #Implement this if necessary
				case "MPG (highway)":
					pass #Implement this if necessary
				case "MPG (combined)":
					pass #Implement this if necessary
				case "MPGe (city)":
					pass #Implement this if necessary
				case "MPGe (highway)":
					pass #Implement this if necessary
				case "MPGe (combined)":
					pass #Implement this if necessary
				case "Fuel Capacity (Gallons)":
					if result[k].upper() != "NA":
						result[k] = str(round(float(result[k]), 1))
				case "Range City (Miles)":
					pass #Implement this if necessary
				case "Range Highway (Miles)":
					pass #Implement this if necessary
				case "Aux Fuel Tank Capacity (gallons)":
					pass #Implement this if necessary
				case "EPA Greenhouse Gas Score":
					pass #Implement this if necessary
				case "CO2 Emissions 15K mi/year (tons)":
					pass #Implement this if necessary
				case "Seating Capacity":
					pass #Implement this if necessary
				case "Passenger Space (cubic feet)":
					pass #Implement this if necessary
				case "Front Head Room (inches)":
					pass #Implement this if necessary
				case "Front Leg Room (inches)":
					pass #Implement this if necessary
				case "Front Hip Room (inches)":
					pass #Implement this if necessary
				case "Front Shoulder Room (inches)":
					pass #Implement this if necessary
				case "Second Row Head Room (inches)":
					pass #Implement this if necessary
				case "Second Row Leg Room (inches)":
					pass #Implement this if necessary
				case "Second Row Hip Room (inches)":
					pass #Implement this if necessary
				case "Second Row Shoulder Room (inches)":
					pass #Implement this if necessary
				case "Third Row Head Room (inches)":
					pass #Implement this if necessary
				case "Third Row Leg Room (inches)":
					pass #Implement this if necessary
				case "Third Row Hip Room (inches)":
					pass #Implement this if necessary
				case "Third Row Shoulder Room (inches)":
					pass #Implement this if necessary
				case "Fourth Row Head Room (inches)":
					pass #Implement this if necessary
				case "Fourth Row Leg Room (inches)":
					pass #Implement this if necessary
				case "Fourth Row Hip Room (inches)":
					pass #Implement this if necessary
				case "Fourth Row Shoulder Room (inches)":
					pass #Implement this if necessary
				case "Fifth Row Head Room (inches)":
					pass #Implement this if necessary
				case "Fifth Row Leg Room (inches)":
					pass #Implement this if necessary
				case "Fifth Row Hip Room (inches)":
					pass #Implement this if necessary
				case "Fifth Row Shoulder Room (inches)":
					pass #Implement this if necessary
				case "Length (inches)":
					pass #Implement this if necessary
				case "Body Length":
					pass #Implement this if necessary
				case "Width without mirrors (inches)":
					pass #Implement this if necessary
				case "Wheelbase (inches)":
					pass #Implement this if necessary
				case "Height (inches)":
					pass #Implement this if necessary
				case "Rear Door Opening Width (inches)":
					pass #Implement this if necessary
				case "Rear Door Opening Height (inches)":
					pass #Implement this if necessary
				case "Curb Weight":
					pass #Implement this if necessary
				case "Weight (lbs)":
					pass #Implement this if necessary
				case "Total Weight (pounds)":
					pass #Implement this if necessary
				case "Body Weight":
					pass #Implement this if necessary
				case "Trunk Space (cubic feet)":
					pass #Implement this if necessary
				case "Cargo Space/Area (cubic feet)":
					pass #Implement this if necessary
				case "Cargo Space/Area with Rear Seat Up":
					pass #Implement this if necessary
				case "Cargo Space/Area with Rear Seat Down":
					pass #Implement this if necessary
				case "Cargo Space/Area Length Behind First Row (inches)":
					pass #Implement this if necessary
				case "Cargo Space/Area Behind Second Row (cubic feet)":
					pass #Implement this if necessary
				case "Cargo Space/Area Length Behind Second Row (inches)":
					pass #Implement this if necessary
				case "Cargo Space/Area Behind Third Row (cubic feet)":
					pass #Implement this if necessary
				case "Cargo Space/Area Length Behind Third Row (inches)":
					pass #Implement this if necessary
				case "Cargo Space/Area Width at Beltline (inches)":
					pass #Implement this if necessary
				case "Cargo Space/Area Behind Fourth Row (cubic feet)":
					pass #Implement this if necessary
				case "Cargo Space/Area Behind Front Row (cubic feet)":
					pass #Implement this if necessary
				case "Cargo Bed Height (inches)":
					pass #Implement this if necessary
				case "Cargo Bed Width at Floor (inches)":
					pass #Implement this if necessary
				case "Cargo Bed Width Between Wheelhousings (inches)":
					pass #Implement this if necessary
				case "Cargo Bed Length (inches)":
					pass #Implement this if necessary
				case "Cargo Bed Width @ Top Rear":
					pass #Implement this if necessary
				case "Cargo Space/Area Length @ Floor to Console":
					pass #Implement this if necessary
				case "Ext'd Cab Cargo Space/Size":
					pass #Implement this if necessary
				case "Steering Type":
					pass #Implement this if necessary
				case "Steering Ratio (:1)":
					pass #Implement this if necessary
				case "Turns lock to lock":
					pass #Implement this if necessary
				case "Turning Diameter / Radius curb to curb (feet)":
					pass #Implement this if necessary
				case "Turning Diameter / Radius wall to wall (feet)":
					pass #Implement this if necessary
				case "Turning Diameter /Radius wall to wall (feet)":
					pass #Implement this if necessary
				case "Front Suspension Type":
					pass #Implement this if necessary
				case "Rear Suspension Type":
					pass #Implement this if necessary
				case "Front Shock Absorber Diameter (mm)":
					pass #Implement this if necessary
				case "Rear Shock Absorber Diameter (mm)":
					pass #Implement this if necessary
				case "Front Tire Size":
					pass #Implement this if necessary
				case "Front Wheel Size (inches)":
					pass #Implement this if necessary
				case "Front Track Width (inches)":
					pass #Implement this if necessary
				case "Front Wheel Material":
					pass #Implement this if necessary
				case "Rear Tire Size":
					pass #Implement this if necessary
				case "Rear Wheel Size (inches)":
					pass #Implement this if necessary
				case "Rear Track Width (inches)":
					pass #Implement this if necessary
				case "Rear Wheel Material":
					pass #Implement this if necessary
				case "Spare Tire Size":
					pass #Implement this if necessary
				case "Spare Wheel Size (inches)":
					pass #Implement this if necessary
				case "Spare Wheel Material":
					pass #Implement this if necessary
				case "Brake Type":
					pass #Implement this if necessary
				case "Front Brake Rotors diameter x thickness (inches)":
					pass #Implement this if necessary
				case "Rear Brake Rotors diameter x thickness (inches)":
					pass #Implement this if necessary
				case "Rear Drums diameter x width (inches)":
					pass #Implement this if necessary
				case "Anti-Lock-Braking System":
					pass #Implement this if necessary
				case "Towing Capacity":
					pass #Implement this if necessary
				case "Maximum Payload Capacity (pounds)":
					pass #Implement this if necessary
				case "Maximum Tongue Weight weight distributing hitch (pounds)":
					pass #Implement this if necessary
				case "Maximum Tongue Weight dead weight hitch (pounds)":
					pass #Implement this if necessary
				case "Maximum Trailer Weight weight distributing hitch (pounds)":
					pass #Implement this if necessary
				case "Maximum Trailer Weight dead weight hitch (pounds)":
					pass #Implement this if necessary
				case "Trailer Weight":
					pass #Implement this if necessary
				case "Payload Weight Front":
					pass #Implement this if necessary
				case "As Spec'd Payload Capacity (pounds)":
					pass #Implement this if necessary
				case "Clutch Size":
					pass #Implement this if necessary
				case "Torque Converter":
					pass #Implement this if necessary
				case "Bolt Pattern":
					pass #Implement this if necessary
				case "Liftover Height (inches)":
					pass #Implement this if necessary
				case "Ground Clearance Front":
					pass #Implement this if necessary
				case "Minimum Ground Clearance (inches)":
					pass #Implement this if necessary
				case "Front Anti-Roll Bar Diameter (inches)":
					pass #Implement this if necessary
				case "Rear Anti-Roll Bar Diameter (inches)":
					pass #Implement this if necessary
				case "Total Option Weight (pounds)":
					pass #Implement this if necessary
				case "Gross Vehicle Weight Rating (pounds)":
					pass #Implement this if necessary
				case "Front Gross Axle Weight Rating (pounds)":
					pass #Implement this if necessary
				case "Rear Gross Axle Weight Rating (pounds)":
					pass #Implement this if necessary
				case "Transfer Case Model":
					pass #Implement this if necessary
				case "Transfer Case Gear Ratio low (:1)":
					pass #Implement this if necessary
				case "Transfer Case Gear Ratio high (:1)":
					pass #Implement this if necessary
				case "Axle Ratio - Low Rear (:1)":
					pass #Implement this if necessary
				case "Final Drive Axle Ratio (:1)":
					pass #Implement this if necessary
				case "URL":
					pass #Implement this if necessary
				case _:
					pass # default case

		return result
