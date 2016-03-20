import requests,bs4,os

question_number = 0

def get_all_url(strName):
    res = requests.get(strName) #('http://www.geekinterview.com/question_details/35086')
    res.raise_for_status()
    global question_number
    question_number = question_number + 1
    content = bs4.BeautifulSoup(res.text,"html.parser")
    if not os.path.exists('C:\\geekinterview'):
        os.makedirs('C:\\geekinterview')
    ele = content.find_all('h1')
    for e in ele:
        names = e.contents[0]
        print(names)
        with open("C:\\geekinterview\\QandA.txt", "a") as myfile:
            myfile.write(strName)
            myfile.write('\n')
            myfile.write(str(question_number)+ ' ')
            myfile.write(names)
    links = content.find_all('a')
    nextlink = content.find(class_ = 'qd_nav')

    answers = content.find_all(class_ = 'commentText' ) #'list_answer')
    for aa in answers:
        testOfNone = aa.p.string  
        print(aa.p.string)
        if testOfNone != None:
            with open("C:\\geekinterview\\QandA.txt", "a") as myfile:
                myfile.write(aa.p.string)
    count = 0
    for a in nextlink.find_all('a',href=True):
        count = count + 1
        while count == 3:
            print(a['href'])
           # get_all_url(a['href'])
            break
    

get_all_url('http://www.geekinterview.com/question_details/35086')
