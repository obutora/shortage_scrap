import pandas as pd

class Medicine:
    def __init__(self, updateAt, type, date, name, sheet, unit, housou):
        self.updateAt = updateAt
        self.type = type
        self.date = date
        self.name = name
        self.sheet = sheet
        self.unit = unit
        self.housou = housou

    # dataListを受け取って、Medicineクラスのインスタンスを返す
    def create(dataList):
        updateAt = list(map(lambda x: x.split('：')[0], dataList)) 
        type = list(map(lambda x: x.split('：')[1][1:], dataList)) 
        date = list(map(lambda x: x.split('：')[2].split(')')[0], dataList))
        name = list(map(lambda x: x.split('：')[2].split(')')[1].split(' ')[0], dataList))
        sheet = list(map(lambda x: x.split('：')[2].split(')')[1].split(' ')[1], dataList))
        unit = list(map(lambda x: x.split('：')[2].split(')')[1].split(' ')[2].split('\u3000')[0], dataList))
        housou = list(map(lambda x: x.split('：')[2].split(')')[1].split(' ')[2].split('\u3000')[1], dataList)) 

        length = len(dataList)

        return list(map(lambda x: Medicine(updateAt[x], type[x], date[x], name[x], sheet[x], unit[x], housou[x]), range(length)))

def convertToDF(dataList):
    return pd.DataFrame(
        data = {
            'updateAt': list(map(lambda x: x.updateAt, dataList)),
            'type': list(map(lambda x: x.type, dataList)),
            'date': list(map(lambda x: x.date, dataList)),
            'name': list(map(lambda x: x.name, dataList)),
            'sheet': list(map(lambda x: x.sheet, dataList)),
            'unit': list(map(lambda x: x.unit, dataList)),
            'housou': list(map(lambda x: x.housou, dataList))
    }
)