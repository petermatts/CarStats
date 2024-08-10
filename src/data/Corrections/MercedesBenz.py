# Automatically generated file template

import os
import sys
import re

if os.getcwd() + "/../" not in sys.path:
	sys.path.append(os.getcwd() + "/../")

from Correction_Template import Correction_Template

class MercedesBenz_Corrections(Correction_Template):
	"""
	Helper class for MercedesBenz corrections
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
						case "a-class":
							m = re.search(r"A \d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "A Class"
						case "b-class-electric-drive":
							m = re.search(r"B \d{3}e", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "B Class"
						case "c-class":
							m = re.search(r"C ?\d{3}e?", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "C Class"

							if "C 63 AMG" in result['Trim']:
								result[k] = "C63 AMG"
						case "c63-amg":
							result[k] = "C63 AMG"
						case "cl-class":
							m = re.search(r"CL ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "CL Class"
						case "cl63-cl65-amg":
							result[k] = "CL63 AMG" if "CL63 AMG" in result['Style'] else "CL65 AMG"
						case "cla-class":
							m = re.search(r"CLA \d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "CLA Class"
						case "clk-class":
							m = re.search(r"CLK ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "CLK Class"
						case "cls-class":
							m = re.search(r"CLS ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "CLS Class"
						case "e-class":
							m = re.search(r"E ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "E Class"
						case "eqe"|"eqe-suv":
							m = re.search(r"EQE ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "EQE"
						case "eqs"|"eqs-suv":
							m = re.search(r"EQS ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "EQS"
						case "esprinter":
							result[k] = "eSprinter"
						case "g-class":
							m = re.search(r"G ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "G Class"
						case "g63-g65-amg":
							result[k] = "G63 AMG" # todo revise
						case "gla-class":
							m = re.search(r"GLA ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "GLA Class"
						case "glb-class":
							m = re.search(r"GLB ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "GLB Class"
						case "glc-class"|"glc-coupe":
							m = re.search(r"GLC ?\d{3}e?", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "GLC Class"
						case "gle-class":
							m = re.search(r"GLE ?\d{3}(d|e)?", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "GLE Class"
						case "glk-class":
							m = re.search(r"GLK ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "GLK Class"
						case "gls-class":
							m = re.search(r"GLS ?\d{3}d?", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "GLS Class"
						case "m-class":
							m = re.search(r"ML ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "M Class"
						case "metris":
							result[k] = "Metris"
						case "ml63-amg":
							result[k] = "ML63 AMG"
						case "r-class":
							m = re.search(r"R ?\d{2,3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
								if "AMG" in result['Trim']:
									result[k] += " AMG" 
							else:
								result[k] = "R Class"
						case "s-class":
							m = re.search(r"S ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]].replace(" ", "")
							else:
								result[k] = "S Class"
						case "s63-s65-amg":
							m = re.search(r"S6(3|5) AMG", result['Style'])
							if m is not None:
								result[k] = result['Style'][m.span()[0]:m.span()[1]]
							else:
								result[k] = "S Class AMG"
						case "sl-class":
							m = re.search(r"SL ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]]
							else:
								result[k] = "SL Class"
						case "slc-class":
							m = re.search(r"SLC ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]]
							else:
								result[k] = "SLC Class"
						case "slk-class":
							m = re.search(r"SLK ?\d{3}", result['Trim'])
							if m is not None:
								result[k] = result['Trim'][m.span()[0]:m.span()[1]]
							else:
								result[k] = "SLK Class"
						case "slk55-amg":
							result[k] = "SLK55 AMG"
						case "slr-class":
							result[k] = "SLR McLaren"
						case "sls-amg":
							result[k] = "SLS AMG"
						case "sprinter":
							result[k] = "Sprinter"
				case "Style":
					result[k] = re.sub("sedan", "Sedan", result['Style'])
					result[k] = re.sub("coupe", "Coupe", result['Style'])
					result[k] = re.sub("roadster", "Roadster", result['Style'])
					result[k] = re.sub("(P|p)lug-in (H|h)ybrid", "PHEV", result['Style'])
					result[k] = re.sub("hybrid", "Hybrid", result['Style'])

					s = re.search(r"Coupe|Cabriolet|Sedan|Black Series|Roadster|Hybrid|PHEV|SUV", result[k])
					if s is not None:
						result[k] = result[k][s.span()[0]:s.span()[1]]
					else:
						result[k] = ""

				case "Trim":
					result[k] = re.sub("BlueTEC", "BlueTEC", result[k])
					result[k] = re.sub("(4|R)WD ", "", result[k])

					if "SUV" in result[k] and "SUV" not in result['Style']:
						result['Style'] += "SUV"
						result['Style'] = result['Style'].lstrip()

					t = re.search(r"((Luxury|Sport|BlueTec|Squared|Cargo|Passenger|CDI|Crew| S |Reg Cab|Cab Chassis|Vans?|Standard|High|Roof|HO|Final Edition|GT|(1|2|3|4)500(XD)?) ?)+", result[k])
					if t is not None:
						result[k] = result[k][t.span()[0]:t.span()[1]].strip()
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
