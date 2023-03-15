import requests
from tutorMe.models import tutorMeUser, Course
def Searcher():
    data = 1
    page_num = 1
    year ="23"

    semester = "2"
    if semester == "Fall":
        semester = "8"
    Classes = []
    class_filter = set()

    relevant_attrs = ['catalog_nbr', 'descr', 'subject']
    while data and page_num<=5:
        page_num_str = str(page_num)

        url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1"
        year_sem_num = year + semester
        url += year_sem_num

        url += "&page="

        url += page_num_str
        r = requests.get(url)
        data = r.json()
        for index in data :
            if not Course.objects.filter(course_name=index["descr"]).exist():
                newCourse=Course()
                newCourse.course_name=index["descr"]
                newCourse.Subject=index["subject"]

                newCourse.referenceLink=url+"&class_nbr="+str(index["class_nbr"])
                class_filter.add(index["descr"])
                index['relevant_attrs'] = [index[attr] for attr in relevant_attrs]
                index['relevant_attrs'].append(url+"&class_nbr="+str(index["class_nbr"]))
                Classes.append(index['relevant_attrs'])

        # filter out items with a low relevance score


        page_num += 1
    return Classes

print(Searcher("AFRICAN"))