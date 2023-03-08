import requests


def get_JSON_Subjects(year, semester):
    year = year[-2:]
    if semester == "Spring":
        semester = "2"
    if semester == "Fall":
        semester = "8"
    subjects = []

    url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearchOptions?institution=UVA01&term=1"
    url += year
    url += semester

    r = requests.get(url)
    data = r.json()

    temp = data.get("subjects")

    for sub in temp:
        subjects.append(sub['subject'])


    return subjects

def get_classes(subject_name, year, semester):
    classes = []
    data = 1
    page_num = 1
    year = year[-2:]
    if semester == "Spring":
        semester = "2"
    if semester == "Fall":
        semester = "8"

    while data != []:
        page_num_str = str(page_num)

        url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1"
        year_sem_num = year + semester + "&subject="
        url += year_sem_num

        add = subject_name + "&page="
        url += add

        url += page_num_str
        r = requests.get(url)
        data = r.json()

        for cur_class in data:
            val = cur_class.get('descr')
            if val not in classes:
                classes.append(val)
        page_num += 1
    return classes



def get_classes(subject_name, year, semester):
    classes = []
    data = 1
    page_num = 1
    year = year[-2:]
    if semester == "Spring":
        semester = "2"
    if semester == "Fall":
        semester = "8"

    while data != []:
        page_num_str = str(page_num)

        url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1"
        year_sem_num = year + semester + "&subject="
        url += year_sem_num

        add = subject_name + "&page="
        url += add

        url += page_num_str
        r = requests.get(url)
        data = r.json()

        for cur_class in data:
            val = cur_class.get('descr')
            if val not in classes:
                classes.append(val)
        page_num += 1
    return classes


#print(get_JSON_Subjects("2023", "Spring"))

#print(get_classes("CS", "2023", "Spring"))
