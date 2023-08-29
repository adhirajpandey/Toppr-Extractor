# create csv file from final merged file

import csv
import json

def cleanText(text):
    text = text.replace('\n', '')
    text = text.replace('<br/>', '')
    text = text.replace('<div>', '')
    text = text.replace('</div>', '')
    text = text.replace('<span>', '')
    text = text.replace('</span>', '')
    text = text.replace('<li>', '')
    text = text.replace('</li>', '')
    text = text.replace('<br>', '')
    text = text.replace('<b>', '')
    text = text.replace('</b>', '')
    text = text.replace('<p>', '')
    text = text.replace('</p>', '')
    text = text.replace('$', '')
    text = text.replace('&', '')
    text = text.replace('class="MsoNormal"', '')
    text = text.replace('&', '')
    text = text.replace('<span lang="EN-US">', '')
    text = text.replace('class="_wysihtml5-temp"', '')

    return text

def getAnswer(data):
    try:
        for i in range(0, 4):
            if data['choices'][i]['is_right'] == True:
                return i+1
    except:
        return -1

def create_csv(merged_json, output_csv):
    with open(merged_json, encoding='utf8') as f:
        datas = json.load(f)

    clean_questions_list = []
    qno = 1

    for page in datas:
        try:
            questions = page['questions']
        except:
            pass
        for questiondata in questions:
            try:
                tempq = {}
                # print(cleanText(questiondata['question']))
                tempq['question_number'] = qno 
                tempq['question'] = cleanText(questiondata['question'].replace('\n', ' '))
                tempq['question_style'] = cleanText(questiondata['question_style'])
                tempq['question_image'] = cleanText(questiondata['question_image'])
                tempq['hint'] = cleanText(questiondata['hint'])
                tempq['solution'] = cleanText(questiondata['solution'])
                tempq['solution_image'] = cleanText(questiondata['solution_image'])
                tempq['correct_option'] = getAnswer(questiondata['with_katex'])
                tempq['choice1'] = cleanText(questiondata['with_katex']['choices'][0]['choice'])
                tempq['choice1_image'] = cleanText(questiondata['with_katex']['choices'][0]['image'])
                tempq['choice2'] = cleanText(questiondata['with_katex']['choices'][1]['choice'])
                tempq['choice2_image'] = cleanText(questiondata['with_katex']['choices'][1]['image'])
                tempq['choice3'] = cleanText(questiondata['with_katex']['choices'][2]['choice'])
                tempq['choice3_image'] = cleanText(questiondata['with_katex']['choices'][2]['image'])
                tempq['choice4'] = cleanText(questiondata['with_katex']['choices'][3]['choice'])
                tempq['choice4_image'] = cleanText(questiondata['with_katex']['choices'][3]['image'])
                tempq['meta_solution'] = cleanText(questiondata['with_katex']['meta_solution'])

                clean_questions_list.append(tempq)

                qno += 1
            except:
                qno += 1
                pass
    
    # print(len(clean_questions_list))
    # print(clean_questions_list[24])

    # open a file for writing
    sorted_data_file = open(output_csv, 'w')
    csvwriter = csv.writer(sorted_data_file)

    count = 0
    for questions in clean_questions_list:
        if count == 0:  
            header = questions.keys()
            csvwriter.writerow(header)
            count += 1
        
        csvwriter.writerow(questions.values())

    print("Successfully created csv file", sorted_data_file)

    sorted_data_file.close()


if __name__ == "__main__":
    merged_json = 'Final/merged_data.json'
    output_csv = 'Final/scriptout.csv'
    create_csv(merged_json, output_csv)