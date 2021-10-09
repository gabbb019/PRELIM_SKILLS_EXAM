import json
import csv

records = ["dateRep", "countriesAndTerritories", "cases", "deaths"]

with open("/home/devasc/CPE41S1/PRELIM_SKILLS_EXAM/covid_cases.json",'r') as covidCasesJSON:
    data = json.loads(covidCasesJSON.read())

print(data)

with open("/home/devasc/CPE41S1/PRELIM_SKILLS_EXAM/parsed_covid_cases.csv",'w',newline='') as covidCasesParsed:    
    csvFile = csv.writer(covidCasesParsed)
    csvFile.writerow(records)
    for i in data["records"]:
        csvFile.writerow([
            i["dateRep"],
            i["countriesAndTerritories"],
            i["cases"],
            i["deaths"]
        ])