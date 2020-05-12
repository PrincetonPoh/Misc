# Not complete

bin_list = db.child('log').get()
days_cleaned = []
time_cleaned = []
interval_list = []
for bin in bin_list.each(): # access bin in log
    data_string = db.child('log').child(bin).get()
    data_string = data_string.split()  # string gives [dayofweek, hour, day, 1/0 (binstate)]
    days_cleaned.app
    end(data_string[0]) # comprehensive list of days cleaned

    for i in range(1,3):
        time_cleaned.append(data_string[i]) # consolidated list of time cleaned

for i in range(0, len(time_cleaned) - 3, 2):
    hour_interval = (int(time_cleaned[i+2]) - int(time_cleaned[i])) * 60 # access first digit of each pair
    minute_interval = int(time_cleaned[i+3]) - int(time_cleaned[i+1]) # access second digit of each pair
    time_interval = hour_interval + minute_interval
    interval_list.append(time_interval)

number_of_cleanings = len(interval_list)
sum = 0
for i in interval_list:
    sum += i
average_interval = sum / number_of_cleanings
    # repeat after interval of 1 minute

floor_dictionary = {'Floor1': {'Bin1' : v, 'Bin2' : v, 'Bin3' : v},
                    'Floor2': {'Bin4' : v, 'Bin5' : v, 'Bin6' : v},
                    'Floor3': {'Bin7' : v, 'Bin8' : v, 'Bin9' : v},
                    'Floor4': {'Bin10' : v, 'Bin11' : v, 'Bin12' : v},
                    'Floor5': {'Bin13' : v, 'Bin14' : v, 'Bin15' : v},
                    'Floor6': {'Bin16' : v, 'Bin17' : v, 'Bin18' : v},
                    'Floor7': {'Bin19' : v, 'Bin20' : v, 'Bin21' : v}}
bin_names = db.child('current_bin_states').get()
for k,v in floor_dictionary.items():
    for bin in bin_names:
        if floor_dictionary[k].get[bin] != None:
            floor_dictionary[k][bin] = db.child('current_bin_states').child(bin)


# map floor to bin
# output : if any floor has trigger
# {'Floor1': 0/1, 'Floor2': ... until 'Floor7': 0,1}

# 7 Lists:
# for 1 floor:
#for one bin:
#[full(0/1), wet(0/1), smell(0/1), averagetime], [bin2 same] ... [for all bins]...

# list of all bins across all 7 floors
#[sort by average time (shortest up)]
#[same output as before but sorted].....................