import csv
from collections import Counter

def Mode():
    with open('height-weight.csv', newline = '') as f :
        reader = csv.reader(f)
        file_data = list(reader)


    file_data.pop(0)
    new_data = []
    for i in range(len(file_data)):
        n_num = file_data[i][1]
        new_data.append(float(n_num))

    data = Counter(new_data)
    mode_data_for_range = {"50-60":0,
                           "60-70":0,
                           "70-80":0}

    for height, occurence in data.items():
        if 50<float(height)<60:
            mode_data_for_range["50-60"] += occurence
        elif 60<float(height)<70:
            mode_data_for_range["60-70"] += occurence
        elif 70<float(height)<80:
            mode_data_for_range["70-80"] += occurence

    mode_range,mode_occurence = 0,0
    for range, occurence in mode_data_for_range.items():
        if occurence>mode_occurence:
            mode_range,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

    mode=float((mode_range[0]+ mode_range[1])/2)
    print(f"mode is {mode:2f}")

    
def Median():
    with open('height-weight.csv', newline = '') as f :
        reader = csv.reader(f)
        file_data = list(reader)


    file_data.pop(0)
    new_data = []
    for i in range(len(file_data)):
        n_num = file_data[i][1]
        new_data.append(float(n_num))

    n = len(new_data)
    new_data.sort()

    if n % 2 == 0 :
        median1 = float(new_data[n//2])
        median2 = float(new_data[n//2-1])
        median = (median1 + median2)/2
    else:
        median = new_data[n//2]
        print(n)

    print("Median is " + str(median))

def Mean():
    with open('height-weight.csv', newline = '') as f :
        reader = csv.reader(f)
        file_data = list(reader)


    file_data.pop(0)
    new_data = []
    for i in range(len(file_data)):
        n_num = file_data[i][1]
        new_data.append(float(n_num))

    n = len(new_data)
    total = 0
    for x in new_data:
        total = total+x

    mean = total/n
    print("mean/average = " + str(mean))

    
def Main():
    method = input("Pick Which Method You Would Like to use  --> ")
    string = method

    if "Mean" in string :
        Mean()
    elif "Median" in string:
        Mode()
    elif "Mode" in string:
        Median()
    else:
        print("Methods are: Mean, Median and Mode")

Main()

    
    
    
    
