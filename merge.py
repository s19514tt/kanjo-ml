import pandas as pd

phase = 0

if phase  == 0:
    label = pd.read_csv(filepath_or_buffer="./data/label.csv", encoding="ms932", sep=",")
    acc = pd.read_csv(filepath_or_buffer="./data/_accelerometer_ALL.csv", encoding="ms932", sep=",")
    two = pd.read_csv(filepath_or_buffer="./data/_barometer_ALL.csv", encoding="ms932", sep=",")
    three = pd.read_csv(filepath_or_buffer="./data/_battery_ALL.csv", encoding="ms932", sep=",")
    four = pd.read_csv(filepath_or_buffer="./data/_battery_charges_ALL.csv", encoding="ms932", sep=",")
    five = pd.read_csv(filepath_or_buffer="./data/_gyroscope_ALL.csv", encoding="ms932", sep=",")
    six = pd.read_csv(filepath_or_buffer="./data/_location_ALL.csv", encoding="ms932", sep=",")
    seven = pd.read_csv(filepath_or_buffer="./data/_screen_ALL.csv", encoding="ms932", sep=",")
    tmp = label
    for item in [acc,two,three,four,five,six,seven]:
        tmp = pd.merge(tmp, item, on='datetime_EST', how='outer')
    tmp.to_csv('./final.csv')

