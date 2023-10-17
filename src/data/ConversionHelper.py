import re


def DataCorrection():
    pass


def KeyMap(webspecs: dict[str, str]) -> dict[str, str]:
    """Map specs dict for YAML -> JSON datafile conversion"""

    specs = {}

    if 'Engine Type and Required Fuel' not in webspecs.keys():
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        print(webspecs['URL'])
        return webspecs

    isElectric = webspecs['Engine Type and Required Fuel'] == 'Electric'

    def EngineAndGas(k: str = '', v: str = ''):
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
                if "Twin Turbo" in v:
                    specs['Turbo'] = 'Twin Turbo'
                elif "Intercooled Turbo" in v:
                    specs['Turbo'] = 'Intercooled Turbo'
                elif "Intercooled Supercharger" in v:
                    specs['Turbo'] = 'Intercooled Supercharger'
                elif "Turbo" in v:
                    specs['Turbo'] = 'Turbo'

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

    def Horsepower(k: str = '', v: str = ''):
        hp = v.split(' @ ')
        if len(hp) > 1 and not isElectric:
            return {'Max Horsepower': hp[0], 'Max Horsepower RPM': hp[1]}
        else:
            return {'Max Horsepower': hp[0]}

    def Torque(k: str = '', v: str = ''):
        hp = v.split(' @ ')
        if len(hp) > 1 and not isElectric:
            return {'Max Torque': hp[0], 'Max Torque RPM': hp[1]}
        else:
            return {'Max Torque': hp[0]}

    def MPG(k: str = '', v: str = ''):
        fe = v.replace('N/A', '').split('/')
        comb = fe[0].strip().split(' ')[0]
        hwy = None
        city = None

        if len(fe) > 1:
            city = fe[1].strip().split(' ')[0]
            hwy = fe[2].strip().split(' ')[0]

        if k == 'EPA Fuel Economy combined/city/highway (mpg)':
            return {'MPG (combined)': comb, 'MPG (highway)': hwy, 'MPG (city)': city}
        elif k == 'EPA Fuel Economy Equivalent (for hybrid and electric vehicles) combined/city/highway (MPGe)':
                return {'MPGe (combined)': comb, 'MPGe (highway)': hwy, 'MPGe (city)': city}
        else:
            return {}

    def TurnRad(k: str = '', v: str = ''):
        try:
            return {'Turn Radius (feet)': str(round(float(v)/2, 2))}
        except:
            return {}
        
    def default(k: str = '', v: str = ''):
        return {k: v}

    switch = {
        'EPA Classification': lambda k, v: {'EPA Class': v},
        'Drivetrain': lambda k, v: {'Drivetrain': ''.join(list(filter(lambda c: c.isupper() or c.isdigit(), v)))},
        'Engine Type and Required Fuel': EngineAndGas,
        'Displacement (liters/cubic inches)': lambda k, v: {'Displacement (Liters)': v.split('/')[0].replace('L', '').strip()},
        'Maximum Horsepower @ RPM': Horsepower,
        'Maximum Torque @ RPM': Torque,
        'Transmission Description': lambda k, v: {'Transmission': v.split(' ')[0]}, #? change
        'Number of Transmission Speeds': lambda k, v: {'Transmission Speeds': v},
        'EPA Fuel Economy combined/city/highway (mpg)': MPG,
        'EPA Fuel Economy Equivalent (for hybrid and electric vehicles) combined/city/highway (MPGe)': MPG,
        'Fuel Capacity / Gas Tank Size': lambda k, v: {'Fuel Capacity (Gallons)': v},
        # 'Length (inches)': lambda v: {'Length (inches)': v},
        'Width, without mirrors (inches)': lambda k, v: {'Width (inches)': v},
        # 'Height (inches)': lambda v: {'Height (inches)': v},
        # 'Wheelbase (inches)': lambda v: {'Wheelbase (inches)': v},
        'Passenger / Seating Capacity': lambda k, v: {'Seating Capacity': v},
        'Total Passenger Volume (cubic feet)': lambda k, v: {'Passenger Space (cubic feet)': v},
        # 'Trunk Space (cubic feet)': lambda v: {'Truck Space (cubic feet)': v},
        'Turning Diameter / Radius, curb to curb (feet)': TurnRad,
        'Base Curb Weight (pounds)': lambda k, v: {'Weight (lbs)': v},
        'Maximum Towing Capacity (pounds)': lambda k, v: {'Towing Capacity': v},
        # Add as necessary
    }

    for key in webspecs.keys():
        addition = switch.get(key, default)
        specs.update(addition(k = key, v = webspecs[key]))

    return specs

