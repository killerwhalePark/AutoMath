from fpdf import FPDF
from PIL import Image
import random
import json


# 1부터 max 까지의 숫자 중 amount 개 만큼 선택
def randomchoice(max, amout):
    numberlist = []
    reslist = []
    for q in range(max):
        numberlist.append(q+1)

    for k in range (amout):
        index = random.randint(1, max -k)
        p = numberlist.pop(index-1)
        reslist.append(p)

    return reslist


def makepdf(first_choice, second_choice, nanido, proamont):

    current_dir = 'Question/' + str(first_choice) + '/' + str(second_choice) + '/'

    filename = current_dir + 'data.json'
    with open(filename)as fileob:
        datalist = json.load(fileob)

    datalist = datalist[nanido-1]
    datalist = datalist[proamont-1]

    with open(current_dir + 'question_amount.json')as fileob3:
        question_amount_list = json.load(fileob3)

    listlen = len(datalist)
    problemlist = []

    for i in range(listlen):
        leveldatalist = datalist[i]
        for j in range(3):
            list = randomchoice(question_amount_list[i][j], leveldatalist[j])
            try:
                u = list[0]
            except:
                pass
            else:
                for element in list:
                    problem = current_dir + str(i+1) + '/' + str(j+1) + '/' + str(element) + '.PNG'
                    problemlist.append(problem)




    namuzi = (proamont*5) % 4
    na = 4- namuzi
    num11 = (proamont*5) + na
    page = num11 /4
    page = int(page)
    if page == 6:
        page = 5



    WIDTH = 210
    HEIGHT = 297

    pdf = FPDF()

    for count in range(page):
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(280, 20, f'', ln= True)




        design = "design.PNG"



        pdf.image(design, 0, 0, int(Image.open(design).size[0]*0.25), int(Image.open(design).size[1])*0.25)

        pdf.set_font('Arial', '', 14)
        pdf.cell(100, 10, f'       '+ str(4*count +1))
        pdf.cell(80, 10, f'' +str(4*count +3), ln=True)
        pdf.cell(100, 230, f'       '+str(4*count +2))
        pdf.cell(80, 230, f''+ str(4*count +4))

        for i in range(4):
            a = int(4*count + i)

            try:
                image = problemlist[a]

            except:
                break
            if a%4 == 0:
                pdf.image(image, 20, 40, int(Image.open(image).size[0] * 0.18), int(Image.open(image).size[1] * 0.18))
            elif a%4 == 1:
                pdf.image(image, 20, 160, int(Image.open(image).size[0] * 0.18), int(Image.open(image).size[1] * 0.18))
            elif a % 4 == 2:
                pdf.image(image, 110, 40, int(Image.open(image).size[0] * 0.18), int(Image.open(image).size[1] * 0.18))
            elif a % 4 == 3:
                pdf.image(image, 110, 160, int(Image.open(image).size[0] * 0.18), int(Image.open(image).size[1] * 0.18))



    pdf.output('result.pdf', 'F')
    return


if __name__ =="__main__":
    makepdf()