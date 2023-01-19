import json

with open('tests.json', 'r', encoding='utf-8') as file:
    tests = json.load(file)

with open('values.json', 'r', encoding='utf-8') as file:
    val_res = list(json.load(file).values())[0]
    res_dict = {d['id']: d['value'] for d in val_res}

    def tests_open(dic):
        if isinstance(dic, dict) and dic.get('tests'):
            tests_open(dic['tests'])
        elif isinstance(dic, list):
            for v in dic:
                v['value'] = res_dict.get(v['id'])
                if v.get('values'):
                    tests_open(v['values'])
                
tests_open(tests)
 
with open('report.json', 'w', encoding='utf-8') as file:
    json.dump(tests, file)
