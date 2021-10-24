def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# we return a list of strings

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit
# We modify the function

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))
'''print the function'''
name_the_benefits_of_functions()