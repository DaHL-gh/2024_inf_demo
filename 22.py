import pandas as pd

file = pd.ExcelFile("22.xls")

sheet1:pd.DataFrame = file.parse(0)

in_work = {sheet1['ID процесса B'][i]: sheet1["Время выполнения процесса B (мс)"][i] for i in range(len(sheet1)) if sheet1["ID процессов A"][i] == 0}
tick = 0
while True:
    to_pop = []
    for x in in_work.items():
        if x[1] == tick:
            to_pop.append(x[0])

    for x in to_pop:
        in_work.pop(x)
        for i in range(len(sheet1)):
            if x in list(map(int, str(sheet1.loc[i, "ID процессов A"]).split("; "))):
                in_work[i+1] = tick + sheet1.loc[i, "Время выполнения процесса B (мс)"]

    if len(in_work) == 4:
        print(tick)

    tick += 1
    if len(in_work) == 0:
        break
print(sheet1.head(15))