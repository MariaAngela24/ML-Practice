import csv
lookup_dict = {}
with open('/Users/mariamendiburo/Downloads/nri-backend-takehome/questions.csv', 'rb') as csvfile:
    questions = csv.DictReader(csvfile, delimiter=",")
    for row in questions:
        print row["question_id"]

