"""
parser a prirazovac vysledku
"""
import re, json
from html.parser import HTMLParser

def loadDB(res):

    """
    spoji vysledky s databazi a zahodi nepotrebne
    :param res: pole vysledku stafet
    :return: slovnik vysledku
    """
    import json
    with open('competitors.json', encoding="utf8") as data_file:
        data = json.load(data_file)
        results = parse_results(res)
        ret_data = []
        for result in results:
            for i in range(2,7, 2):
                for competitor in data:
                    if (competitor["firstname"] == result[i] and competitor["lastname"] == result[i+1]):

                        ret_data.append({"id": competitor["id"], "result": int(result[0]), "time": result[1]})
                        break
        return ret_data


def parse_results(res):
    """
    parsuje string vysledku
    :param res: radek vysledku stafet
    :return: pole vysledku
    """
    return re.findall(r'([0-9]+)\) [\w]+ ([0-9A-Z:]+) \(([^ ]+) ([^,]+), ([^ ]+) ([^,]+), ([^ ]+) ([^)]+)\)', res, re.UNICODE)

def handle_file():
    """
    najde ve vysledcich vysledky stafet a ulozi je v json
    """
    file_results = open('result.html', encoding="utf8")
    results_page = file_results.read()
    results_list = re.findall(r'<p>([^<]{20,})', results_page,re.UNICODE)
    list = []
    for results in results_list:
        list += loadDB(results)
    file_out = open('result.json', 'w')
    json.dump(list, file_out, indent=0, separators=(',',':'))

if __name__ == '__main__':
    handle_file()