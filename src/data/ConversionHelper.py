import re


def DataCorrection():
    pass


# TODO refactor into switch dict
def KeyMap(webspecs: dict[str, str]) -> dict[str, str]:
    """Map specs dict for YAML -> JSON datafile conversion"""

    specs = {}
    isElectric = webspecs['Engine Type and Required Fuel'] == 'Electric'

    # TODO overhaul into intercooled/turbocharged/twinturbo/turbo/etc...
    def EngineAndGas(v: str):
        if isElectric:
            return {'Engine': 'Electric', 'Fuel': 'Electric'}
        else:
            isHybrid = "Gas/Electric" in v
            engine = re.search('\w-?\d+', v)

            result = {}
            if engine != None:
                engine = v[engine.span()[0]:engine.span()[1]].replace('-', '')
                result.update({'Engine': engine})
                
                # check turbos
                # if "Twin Turbo" in webspecs[i]:
                #     specs['Turbos'] = '2'
                # elif "Turbo" in webspecs[i]:
                #     specs['Turbos'] = '1'
                # else:
                #     specs['Turbos'] = '0'

                # check hybrid
                if not isHybrid:
                    gas = re.search("Regular|Premium|Gas|Diesel", v)
                    try:
                        result.update({'Fuel': v[gas.span()[0]:gas.span()[1]]})
                    except:
                        pass
                else:
                    result.update({'Fuel': 'Hybrid'})
            
            return result

    def Horsepower(v: str):
        hp = v.split(' @ ')
        if len(hp) > 1 and not isElectric:
            return {'Max Horsepower': hp[0], 'Max Horsepower RPM': hp[1]}
        else:
            return {'Max Horsepower': hp[0]}

    def Torque(v: str):
        hp = v.split(' @ ')
        if len(hp) >= 1 and not isElectric:
            return {'Max Horsepower': hp[0], 'Max Horsepower RPM': hp[1]}
        else:
            return {'Max Horsepower': hp[0]}

    def MPG(v: str):
        fe = v.replace('N/A', '').split('/')
        comb = fe[0].strip().split(' ')[0]
        hwy = None
        city = None

        if len(fe) > 1:
            city = fe[1].strip().split(' ')[0]
            hwy = fe[2].strip().split(' ')[0]

        if isElectric:
            return {'MPGe (combined)': comb, 'MPGe (highway)': hwy, 'MPGe (city)': city}
        else:
            return {'MPG (combined)': comb, 'MPG (highway)': hwy, 'MPG (city)': city}

    def TurnRad(v: str):
        try:
            return {'Turn Radius (feet)': str(round(float(v)/2, 2))}
        except:
            return {}
        
    def default(k: str, v: str):
        return {k: v}

    switch = {
        'EPA Classification': lambda v: {'EPA Class': v},
        'Drivetrain': lambda v: {'Drivetrain': ''.join(list(filter(lambda c: c.isupper() or c.isdigit(), v)))},
        'Engine Type and Required Fuel': EngineAndGas,
        'Displacement (liters/cubic inches)': lambda v: {'Displacement (Liters)': v.split('/')[0].replace('L', '').strip()},
        'Maximum Horsepower @ RPM': Horsepower,
        'Maximum Torque @ RPM': Torque,
        'Transmission Description': lambda v: {'Transmission': v.split(' ')[0]}, #? change
        'Number of Transmission Speeds': lambda v: {'Transmission Speeds': v},
        'EPA Fuel Economy, combined/city/highway (mpg)': MPG,
        'EPA Fuel Economy Equivalent (for hybrid and electric vehicles), combined/city/highway (MPGe)': MPG,
        'Fuel Capacity / Gas Tank Size': lambda v: {'Fuel Capacity (Gallons)': v},
        # 'Length (inches)': lambda v: {'Length (inches)': v},
        'Width, without mirrors (inches)': lambda v: {'Width (inches)': v},
        # 'Height (inches)': lambda v: {'Height (inches)': v},
        # 'Wheelbase (inches)': lambda v: {'Wheelbase (inches)': v},
        'Passenger / Seating Capacity': lambda v: {'Seating Capacity': v},
        'Total Passenger Volume (cubic feet)': lambda v: {'Passenger Space (cubic feet)': v},
        # 'Trunk Space (cubic feet)': lambda v: {'Truck Space (cubic feet)': v},
        'Turning Diameter / Radius, curb to curb (feet)': TurnRad,
        'Base Curb Weight (pounds)': lambda v: {'Weight (lbs)': v},
        'Maximum Towing Capacity (pounds)': lambda v: {'Towing Capacity': v}
    }

    for i in list(webspecs.keys()):
        if webspecs[i] != 'NA': # N/A or ? or '-TBD-' or ''
            if i == 'Brand' or i == 'Model' or i == 'Year' or i == 'Price' or i == 'Trim' or i == 'URL':
                specs[i] = webspecs[i]
                # specs[i] = webspecs[i].replace(',', '')
            elif i == 'EPA Classification':
                specs['EPA Class'] = webspecs[i]
            elif i == 'Drivetrain':
                dt = webspecs[i].replace('Four', '4')
                specs[i] = ''.join(list(filter(lambda c: c.isupper() or c.isdigit(), dt)))
            elif i == 'Engine Type and Required Fuel':
                if isElectric:
                    specs['Engine'] = 'Electric'
                    specs['Fuel'] = 'Electric'
                else:
                    isHybrid = "Gas/Electric" in webspecs[i]
                    engine = re.search('\w-?\d+', webspecs[i])
                    if engine != None:
                        engine = webspecs[i][engine.span()[0]:engine.span()[1]].replace('-', '')
                        # specs['Engine'] = engine[:1] + '-' + engine[1:]
                        specs['Engine'] = engine
                        
                        # check turbos
                        if "Twin Turbo" in webspecs[i]:
                            specs['Turbos'] = '2'
                        elif "Turbo" in webspecs[i]:
                            specs['Turbos'] = '1'
                        else:
                            specs['Turbos'] = '0'

                        # check hybrid
                        if isHybrid:
                            specs['Fuel'] = 'Hybrid'
                        else:
                            gas = re.search("Regular|Premium|Gas|Diesel", webspecs[i])
                            try:
                                specs['Fuel'] = webspecs[i][gas.span()[0]:gas.span()[1]]
                            except:
                                pass
            elif i == 'Displacement (liters/cubic inches)':
                specs['Displacement (liters)'] = webspecs[i].split('/')[0].replace('L', '').strip()
            elif i == 'Maximum Horsepower @ RPM':
                hp = webspecs[i].split(' @ ')
                specs['Max Horsepower'] = hp[0]
                if not isElectric and len(hp) > 1: 
                    specs['Max Horsepower RPM'] = hp[1]
            elif i == 'Maximum Torque @ RPM':
                tq = webspecs[i].split(' @ ')
                specs['Max Torque'] = tq[0]
                if not isElectric and len(tq) > 1: 
                    specs['Max Torque RPM'] = tq[1]
            elif i == 'Transmission Description':
                specs['Transmission'] = webspecs[i].split(' ')[0]
                # specs['Transmission'] = webspecs[i].split(' ')[0].replace(',', '')
            elif i == 'Number of Transmission Speeds':
                specs['Transmission Speeds'] = webspecs[i]
            elif not isElectric and i == 'EPA Fuel Economy, combined/city/highway (mpg)':
                fe = webspecs[i].replace('N/A', '').split('/')
                specs['MPG (combined)'] = fe[0].strip().split(' ')[0]
                if len(fe)>1:
                    specs['MPG (city)'] = fe[1].strip().split(' ')[0]
                    specs['MPG (highway)'] = fe[2].strip().split(' ')[0]
            elif isElectric and i == 'EPA Fuel Economy Equivalent (for hybrid and electric vehicles), combined/city/highway (MPGe)':
                fe = webspecs[i].replace('N/A', '').split('/')
                specs['MPGe (combined)'] = fe[0].strip().split(' ')[0]
                specs['MPGe (city)'] = fe[1].strip().split(' ')[0]
                specs['MPGe (highway)'] = fe[2].strip().split(' ')[0]
            elif i == 'Fuel Capacity / Gas Tank Size':
                specs['Fuel Cap. (Gal)'] = webspecs[i]
            elif i == 'Length (inches)':
                specs['Length (in)'] = webspecs[i]
            elif i == 'Width, without mirrors (inches)':
                specs['Width no mirrors (in)'] = webspecs[i]
            elif i == 'Height (inches)':
                specs['Height (in)'] = webspecs[i]
            elif i == 'Wheelbase (inches)':
                specs['Wheelbase (in)'] = webspecs[i]
            elif i == 'Passenger / Seating Capacity':
                specs['Seating Cap'] = webspecs[i]
            elif i == 'Total Passenger Volume (cubic feet)':
                specs['Passenger Space (cu ft)'] = webspecs[i]
            elif i == 'Trunk Space (cubic feet)':
                specs['Trunk Space (cu ft)'] = webspecs[i]
            elif i == 'Turning Diameter / Radius, curb to curb (feet)':
                try:
                    #TODO format to a certain decimal place?
                    specs['Turn Radius (ft)'] = str(float(webspecs[i])/2) # curb to curb
                except:
                    pass
            elif i == 'Base Curb Weight (pounds)':
                specs['Weight (lbs)'] = webspecs[i]
                # specs['Weight (lbs)'] = webspecs[i].replace(",", "")
            elif i == 'Maximum Towing Capacity (pounds)':
                specs['Max Towing (lbs)'] = webspecs[i]
            else:
                pass

    return specs

