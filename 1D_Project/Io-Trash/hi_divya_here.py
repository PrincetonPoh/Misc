import time
bin_list = db.child('log').get()
bin_and_interval = []
for bin in bin_list: # access each bin in log
    days_cleaned = []
    time_cleaned = []
    interval_list = []

    data_dictionary = db.child('log').child(bin).get() # get a dictionary of {random string: neededstring!}
    data_string_list = db.child('log').child(bin).keys()
    for i in data_string_list:  # for a single string '0 22 45 1'
        data_string = i.split()  # string gives [dayofweek, hour, day, 1/0 (binstate)]
        days_cleaned.append(data_string[0]) # comprehensive list of days cleaned
        for i in range(1,3): # access 22 45
            time_cleaned.append(data_stri
            ng[i]) # consolidated list of time cleaned
    # repeat for all strings in data_string_list

    for i in range(0, len(time_cleaned) - 3, 2):
        hour_interval = (int(time_cleaned[i+2]) - int(time_cleaned[i])) * 60 # access first digit of each pair
        minute_interval = int(time_cleaned[i+3]) - int(time_cleaned[i+1]) # access second digit of each pair
        time_interval = hour_interval + minute_interval
        interval_list.append(time_interval) # intervals between cleaning for one bin

    number_of_cleanings = len(interval_list)
    sum = 0
    for i in interval_list:
        sum += i
    average_interval = sum / number_of_cleanings # average interval for one bin
    bin_and_interval.append(average_interval)
    # repeat for multiple bins

# TO DO: repeat entire loop (for all bins) after interval of 1 minute

floor_bin_dictionary = {'Floor1': {'Bin1' : 0, 'Bin2' : 0, 'Bin3' : 0},
                    'Floor2': {'Bin4' : 0, 'Bin5' : 0, 'Bin6' : 0},
                    'Floor3': {'Bin7' : 0, 'Bin8' : 0, 'Bin9' : 0},
                    'Floor4': {'Bin10' : 0, 'Bin11' : 0, 'Bin12' : 0},
                    'Floor5': {'Bin13' : 0, 'Bin14' : 0, 'Bin15' : 0},
                    'Floor6': {'Bin16' : 0, 'Bin17' : 0, 'Bin18' : 0},
                    'Floor7': {'Bin19' : 0, 'Bin20' : 0, 'Bin21' : 0}}
bin_interval_dictionary = {}
for k,v in floor_bin_dictionary.items():
    i = 0
    for bin in bin_list:
        if floor_bin_dictionary[k].get(bin, None) != None:
            floor_bin_dictionary[k][bin] = {'Smell' : 0, 'US' : 1, 'Water' : 0} # update dictionary
            floor_bin_dictionary[k][bin]['timeinterval'] = bin_and_interval[i]
            bin_interval_dictionary[bin] = bin_and_interval[i]
        i += 1
# print(floor_bin_dictionary) gives:
# {'Floor1': {'Bin1': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 1},
#            'Bin2': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 2},
#            'Bin3': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 3}},
# 'Floor2': {'Bin4': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 4},
#            'Bin5': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 5},
#            'Bin6': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 6}},
# 'Floor3': {'Bin7': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 7},
#            'Bin8': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 8},
#            'Bin9': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 9}},
# 'Floor4': {'Bin10': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 10},
#            'Bin11': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 11}
#            'Bin12': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 12}},
# 'Floor5': {'Bin13': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 13},
#            'Bin14': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 14},
#            'Bin15': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 15}},
# 'Floor6': {'Bin16': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 16},
#            'Bin17': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 17},
#            'Bin18': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 18}},
# 'Floor7': {'Bin19': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 19},
#            'Bin20': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 20},
#            'Bin21': {'Smell': 0, 'US': 1, 'Water': 0, 'timeinterval': 21}}}


# map floor to bin
# output : if any floor has trigger
# {'Floor1': 0/1, 'Floor2': ... until 'Floor7': 0,1}
floor_dictionary = {}
for k,v in floor_bin_dictionary.items(): # floor, {}
    floor_dictionary[k] = 0
    for key,val in floor_bin_dictionary[k].items(): # bin, {}
        for KEY,VAL in floor_bin_dictionary[k][key].items(): # 'water', 0, 'us', 0; timeinterval will never be 1
            if floor_bin_dictionary[k][key][KEY] == 1:
                floor_dictionary[k] = 1
                break           #
# print(floor_dictionary) gives:
# {'Floor1': 0, 'Floor2': 0, 'Floor3': 0, 'Floor4': 0, 'Floor5': 0, 'Floor6': 0, 'Floor7': 0}

# 7 Lists:
# for 1 floor:
Floor1 = []
Floor2 = []
Floor3 = []
Floor4 = []
Floor5 = []
Floor6 = []
Floor7 = []
for k,v in floor_bin_dictionary.items(): # floor, {}
    for key,val in floor_bin_dictionary[k].items(): # bin, {}
        for KEY, VAL in floor_bin_dictionary[k][key].items():  # 'water', 0, 'us', 0
            floor_bin_dictionary[k][key][KEY]
            if len(Floor1) < 9:
                Floor1.append(floor_bin_dictionary[k][key][KEY])
            elif len(Floor2) < 9:
                Floor2.append(floor_bin_dictionary[k][key][KEY])
            elif len(Floor3) < 9:
                Floor3.append(floor_bin_dictionary[k][key][KEY])
            elif len(Floor4) < 9:
                Floor4.append(floor_bin_dictionary[k][key][KEY])
            elif len(Floor5) < 9:
                Floor5.append(floor_bin_dictionary[k][key][KEY])
            elif len(Floor6) < 9:
                Floor6.append(floor_bin_dictionary[k][key][KEY])
            else:
                Floor7.append(floor_bin_dictionary[k][key][KEY])
# each floor output:
# [0 1 0 12 0 1 1 13 0 0 0 13]
# TO DO: EACH BIN IS A LIST


# list of all bins across all 7 floors
# for floor_bin_dictionary:
bin_sorted_time = sorted(bin_interval_dictionary.items(), key = lambda x : x[1])
# print(bin_sorted_time):
# [('Bin2', 2), ('Bin3', 3), ('Bin4', 4), ('Bin5', 5), ('Bin6', 6), ('Bin7', 7), ('Bin8', 8), ('Bin9', 9), ('Bin10', 10), ('Bin1', 11), ('Bin11', 11), ('Bin12', 12), ('Bin13', 13), ('Bin14', 14), ('Bin15', 15), ('Bin16', 16), ('Bin17', 17), ('Bin18', 18), ('Bin19', 19), ('Bin20', 20), ('Bin21', 21)]

