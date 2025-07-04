import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

log_file = "log_file.txt" 
target_file = "transformed_data.csv" 

def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process) 
    return dataframe 

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines=True)
    return dataframe


def extract_from_xml(file_to_process):
    dataframe = pd.read_xml(file_to_process)
    return dataframe

def extract(): 
    extracted_data = pd.DataFrame(columns=['car_model','year_of_manufacture','price','fuel']) # create an empty data frame to hold extracted data 
     
    # process all csv files, except the target file
    for csvfile in glob.glob("*.csv"): 
        if csvfile != target_file:  # check if the file is not the target file
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 
         
    # process all json files 
    for jsonfile in glob.glob("*.json"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 
     
    # process all xml files 
    for xmlfile in glob.glob("*.xml"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data 

def transform(data): 
    '''Convert inches to meters and round off to two decimals 
    1 inch is 0.0254 meters '''
    data['price'] = round(data.price * 0.0254,2) 
    
    return data 

def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file) 

def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' 
    now = datetime.now()  
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

# Journaliser l'initialisation du processus ETL
log_progress("ETL Job Started")

# Journaliser le début de la phase d'extraction
log_progress("Extract phase Started")
extracted_data = extract()

# Journaliser la fin de la phase d'extraction
log_progress("Extract phase Ended")

# Journaliser le début de la phase de transformation
log_progress("Transform phase Started")
transformed_data = transform(extracted_data)
print("Données transformées")
print(transformed_data)

# Journaliser la fin de la phase de transformation
log_progress("Transform phase Ended")

# Journaliser le début de la phase de chargement
log_progress("Load phase Started")
load_data(target_file, transformed_data)

# Journaliser la fin de la phase de chargement
log_progress("Load phase Ended")

# Journaliser la fin du processus ETL
log_progress("ETL Job Ended")
