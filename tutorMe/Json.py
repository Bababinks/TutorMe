import requests


def get_JSON_Subjects():

    subjects = []
    url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearchOptions?institution=UVA01&term=12312"
    r = requests.get(url)
    data = r.json()

    temp = data.get("subjects")

    for sub in temp:
        subjects.append(sub['subject'])


    return subjects
print(get_JSON_Subjects())

