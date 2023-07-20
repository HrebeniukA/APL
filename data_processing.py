
def clean_notes(APL):
    APL['Notes'] = APL['Notes'].str.replace(r"^→ (?:UEFA Cup Winners' Cup|European Cup|Relegated, → Europa League via).*", 'UEFA Cup', regex=True)
    APL['Notes'] = APL['Notes'].str.replace(r'^→ (?:Europa League|UEFA Cup).*', 'Europa League', regex=True)
    APL['Notes'] = APL['Notes'].str.replace(r'^→ (?:Champions League).*', 'Champions League', regex=True)
    APL['Notes'] = APL['Notes'].str.replace(r'^→ (?:UEFA Intertoto).*', 'UEFA Intertoto Cup', regex=True)
    APL['Notes'] = APL['Notes'].str.replace(r'^→ (?:Europa Conference League).*', 'Europa Conference League', regex=True)
    APL['Notes'] = APL['Notes'].replace(r'Relegated, → Europa League via cup win(\s\d)?', 'Europa League', regex=True)
    APL['Notes'] = APL['Notes'].replace('Relegated, → UEFA Intertoto Cup', 'UEFA Intertoto Cup', regex=True)
    return APL
