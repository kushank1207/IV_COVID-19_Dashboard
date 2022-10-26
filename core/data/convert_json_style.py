import json

def func():
    with open ("healthcare.json", "r") as file:
        dict_data = json.load(file)
        return dict_data
    # print(dict_data)

if __name__ == "__main__":
    data_old = func()   
    json_struct = {
        "state" : [],
        "lat" : [],
        "lng" : [],
        "ICU_bed" :[],
        "PSYCHIATRIC_bed" :[],
        "ACUTE_bed" :[],
        "Other_bed\r" :[],
    }

    for state_data in data_old:
        for key, value in state_data.items():
            if key == "state" or key == "Other_bed\r":
                json_struct[key].append(value)
            else:
                json_struct[key].append(float(value))
            
    
    json_struct["Other_bed"] = [float(value.split("\r")[0]) for value in json_struct["Other_bed\r"]]
    json_struct.pop("Other_bed\r")

    with open("healthcare_cleaned.json", "w") as outfile:
        json.dump(json_struct, outfile)