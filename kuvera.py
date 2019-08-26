r = {'King Shan': {'Gender':'Male',
                    'Mother' : None,
                    'spouse':'Queen Anga',
                    'children':['Chit', 'Ish', 'Vich', 'Aras','Satya'],
                    },
    'Queen Anga': {'Gender':'Female',
                        'Mother' : None,
                        'spouse':'King Shan',
                        'children':['Chit', 'Ish', 'Vich', 'Aras','Satya'],
                        },
    'Chit': {'Gender':'Male',
                        'Mother' : 'Queen Anga',
                        'spouse':'Amba',
                        'children':['Dritha', 'Tritha', 'Vritha'],
                        },
    'Amba': {'Gender':'Female',
                        'Mother' : None,
                        'spouse':'Chit',
                        'children':['Dritha', 'Tritha', 'Vritha'],
                        },
    'Ish': {'Gender':'Male',
                        'Mother' : 'Queen Anga',
                        'spouse':None,
                        'children':[],
                        },
    'Vich': {'Gender':'Male',
                        'Mother' : 'Queen Anga',
                        'spouse':'Lika',
                        'children':['Vila','Chika'],
                        },
    'Lika': {'Gender':'Female',
                        'Mother' : None,
                        'spouse':'Vich',
                        'children':['Vila','Chika'],
                        },
    'Aras': {'Gender':'Male',
                        'Mother' : 'Queen Anga',
                        'spouse':'Chitra',
                        'children':['Jinki','Ahit'],
                        },
    'Chitra': {'Gender':'Female',
                        'Mother' : None,
                        'spouse':'Aras',
                        'children':['Jinki','Ahit'],
                        },
    'Satya': {'Gender':'Female',
                        'Mother' : 'Queen Anga',
                        'spouse':'Vyam',
                        'children':['Asva','vyas', 'Atya'],
                        },
    'Vyam': {'Gender':'Male',
                        'Mother' : None,
                        'spouse':'Satya',
                        'children':['Asva','vyas', 'Atya'],
                        },
    'Dritha': {'Gender':'Female',
                        'Mother' : 'Amba',
                        'spouse':'Jaya',
                        'children':['Yodhan'],
                        },
    'Jaya': {'Gender':'Male',
                        'Mother' : None,
                        'spouse':'Dritha',
                        'children':['Yodhan'],
                        },
    'Tritha': {'Gender':'Female',
                        'Mother' : 'Amba',
                        'spouse':None,
                        'children':[],
                        },
    'Vritha': {'Gender':'Male',
                        'Mother' : 'Amba',
                        'spouse':None,
                        'children':[],
                        },
    'Vila': {'Gender':'Female',
                        'Mother' : 'Lika',
                        'spouse':None,
                        'children':[],
                        },
    'Chika': {'Gender':'Female',
                        'Mother' : 'Lika',
                        'spouse':None,
                        'children':[],
                        },
    'Arit': {'Gender':'Male',
                        'Mother' : None,
                        'spouse':'Jinki',
                        'children':['Laki', 'Lavanya'],
                        },
    'Jinki': {'Gender':'Female',
                        'Mother' : 'Chitra',
                        'spouse':'Arit',
                        'children':['Laki', 'Lavanya'],
                        },
    'Ahit': {'Gender':'Male',
                        'Mother' : 'Chitra',
                        'spouse':None,
                        'children':[],
                        },
    'Satvy': {'Gender':'Female',
                        'Mother' : None,
                        'spouse': 'Asva',
                        'children':['Vasa'],
                        },
    'Asva': {'Gender':'Male',
                        'Mother' : 'Satya',
                        'spouse': 'Satvy',
                        'children':['Vasa'],
                        },
    'Krpi': {'Gender':'Female',
                        'Mother' : None,
                        'spouse': 'Vyas',
                        'children':['Kriya', 'Krithi'],
                        },
    'Vyas': {'Gender':'Male',
                        'Mother' : 'Satya',
                        'spouse': 'Krpi',
                        'children':['Kriya', 'Krithi'],
                        },
    'Atya': {'Gender':'Female',
                        'Mother' : 'Satya',
                        'spouse': None,
                        'children':[],
                        },
    'Yodhan': {'Gender':'Male',
                        'Mother' : 'Dritha',
                        'spouse': None,
                        'children':[],
                        },
    'Laki': {'Gender':'Male',
                        'Mother' : 'Jinki',
                        'spouse': None,
                        'children':[],
                        },
    'Lavanya': {'Gender':'Female',
                        'Mother' : 'Jinki',
                        'spouse': None,
                        'children':[],
                        },
    'Vasa': {'Gender':'Male',
                        'Mother' : 'Satvy',
                        'spouse': None,
                        'children':[],
                        },
    'Kriya': {'Gender':'Male',
                        'Mother' : 'Krpi',
                        'spouse': None,
                        'children':[],
                        },
    'Krithi': {'Gender':'Female',
                        'Mother' : 'Krpi',
                        'spouse': None,
                        'children':[],
                        },
    }

def getSons(name):
    if getChildren(name):
        return [child for child in getChildren(name) if r.get(child).get('Gender') =='Male']

def getChildren(name):
    person = r.get(name)
    if person and person.get('children'):
        return person.get('children')

def getMother(name):
    person = r.get(name)
    if person and person.get('Mother'):
        return person.get('Mother')

def getSpouse(name):
    person = r.get(name)
    if person and person.get('spouse'):
        return person.get('spouse')

def getFather(name):
    if getMother(name):
        return getSpouse(getMother(name))

def getDaughters(name):
    if getChildren(name):
        return [child for child in getChildren(name) if r.get(child).get('Gender') =='Female']

def getBrothers(name):
    mother = getMother(name)
    if mother and getSons(mother):
        sons = getSons(mother)
        return sons and list(set(sons) - set([name]))

def getSisters(name):
    mother = getMother(name)
    if mother and getDaughters(mother):
        daughters = getDaughters(mother)
        return daughters and list(set(daughters) - set([name]))

def getSiblings(name):
    mother = getMother(name)
    if mother and getChildren(mother):
        return list(set(getChildren(mother)) - set([name]))

def getPaternalUncle(name):
    father = getFather(name)
    if father and getBrothers(father):
        return getBrothers(father)

def getMaternalUncle(name):
    mother = getMother(name)
    if mother and getBrothers(mother):
        return getBrothers(mother)

def getPaternalAunt(name):
    father = getFather(name)
    if father and getSisters(father):
        return getSisters(father)

def getGender(name):
    person = r.get(name)
    return person and person.get('Gender')

def getSisterInLaw(name):
    sist_in_law= []
    spouse = getSpouse(name)
    brothers = getBrothers(name)
    sist_in_law.extend(getSisters(spouse) if spouse and getSisters(spouse) else [])
    if brothers:
        sist_in_law.extend([getSpouse(b) for b in brother if getSpouse(b)])
    return sist_in_law

def getBrotherInLaw(name):
    bro_in_law= []
    spouse = getSpouse(name)
    sisters = getSisters(name)
    bro_in_law.extend(getBrothers(spouse) if spouse and getBrothers(spouse) else [])
    if sisters:
        bro_in_law.extend([getSpouse(s) for s in sisters if getSpouse(s)])
    return bro_in_law


if __name__ == '__main__':
    for name in ['Chitra', 'Amba', 'Queen Anga', 'Ahit', 'Laki', 'Vasa']:
        print('='*40)
        print('Sister of {0}: {1}'.format(name, getSisters(name)))
        print('Sons of {0}: {1}'.format(name, getSons(name)))
        print('Siblings of {0}: {1}'.format(name, getSiblings(name)))
        print('Brothers of {0}: {1}'.format(name, getBrothers(name)))
        print('Paternal-Uncle of {0}: {1}'.format(name, getPaternalUncle(name)))
        print('Maternal-Uncle of {0}: {1}'.format(name, getMaternalUncle(name)))
        print('Paternal-Aunt of {0}: {1}'.format(name, getPaternalAunt(name)))
        print('Brothers-in-law of {0}: {1}'.format(name, getBrotherInLaw(name)))
        print('Sister-in-low of {0}: {1}'.format(name, getSisterInLaw(name)))
        print('Daughters of {0}: {1}'.format(name, getDaughters(name)))
        print('Childern of {0}: {1}'.format(name, getChildren(name)))
