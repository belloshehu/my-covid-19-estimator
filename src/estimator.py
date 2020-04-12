import  json
from data import data

output_data = {
    "data":data,
    "impact":{},
    "severeImpact":{}
}

#returns duration for estimation
def get_duration(data):

    if data['periodType'] == 'months':
        duration = data['timeToElapse']*30
    elif data['periodType'] == 'weeks':
        duration = data['timeToElapse']*7
    else:
        duration = data['timeToElapse']*1
    return duration
  
  #challenge 1 function 
def challenge1_soluton(data):
    #estimating the currently Infected people for both impact and severeImpact 
    impact_currently_infected = data["reportedCases"]*10
    severe_Impact_currently_infected = data["reportedCases"]*50
    output_data["impact"]["currentlyInfected"] = impact_currently_infected
    output_data["severeImpact"]["currentlyInfected"] = severe_Impact_currently_infected

    #estimating the imfected people for duration based on timeToElapse for both impact and severeImpact
    impact_infections_by_requested_time = impact_currently_infected*(2**(get_duration(data)//3))
    severe_Impact_infections_by_requested_time = severe_Impact_currently_infected*(2**(get_duration(data)//3))
    output_data["impact"]["infectionsByRequestedTime"] = impact_infections_by_requested_time
    output_data["severeImpact"]["infectionsByRequestedTime"] = severe_Impact_infections_by_requested_time
    return output_data
def challenge2_soluton(data):
    # determing the 15% of InfectionsByRequestedTime for impact and severeImpact
    output_data_after_challenge1 = challenge1_soluton(data)
    impact_severe_cases_requested_time = output_data_after_challenge1["impact"]["infectionsByRequestedTime"]*0.15
    severe_Impact_severe_cases_requested_time = output_data_after_challenge1["severeImpact"]["infectionsByRequestedTime"]*0.15
    output_data_after_challenge1["impact"]["severeCasesByRequestedTime"] = int(impact_severe_cases_requested_time)
    output_data_after_challenge1["severeImpact"]["severeCasesByRequestedTime"] = int(severe_Impact_severe_cases_requested_time)
    
    #Determining the number of available beds
    impact_hospital_beds_by_requested_time = data["totalHospitalBeds"]*0.35 - impact_severe_cases_requested_time
    severe_Impact_hospital_beds_by_requested_time = data["totalHospitalBeds"]*0.35 - severe_Impact_severe_cases_requested_time
    output_data_after_challenge1["impact"]["hospitalBedsByRequestedTime"] = int(impact_hospital_beds_by_requested_time)
    output_data_after_challenge1["severeImpact"]["hospitalBedsByRequestedTime"] = int(severe_Impact_hospital_beds_by_requested_time)
    output_data = output_data_after_challenge1
    return output_data

def challenge3_soluton(data):
    output_data_after_challenge2 = challenge2_soluton(data)
    #Determining casesForICURequestedByTime
    impact_cases_for_icu_by_requested_time = output_data_after_challenge2["impact"]["infectionsByRequestedTime"]*0.05
    severe_Impact_cases_for_icu_by_requested_time = output_data_after_challenge2["severeImpact"]["infectionsByRequestedTime"]*0.05
    output_data_after_challenge2["impact"]["casesForICUByRequestedTime"] = impact_cases_for_icu_by_requested_time
    output_data_after_challenge2["severe"]["casesForICUByRequestedTime"] = severe_Impact_cases_for_icu_by_requested_time

    #Determining casesForVentilatorsByRequestedTime
    impact_cases_for_ventilators_by_requested_time = output_data_after_challenge2["impact"]["infectionsByRequestedTime"]*0.02
    severe_Impact_cases_for_ventilators_by_requested_time = output_data_after_challenge2["severeImpact"]["infectionsByRequestedTime"]*0.02
    output_data_after_challenge2["impact"]["casesForVentilatorsByRequestedTime"] = impact_cases_for_ventilators_by_requested_time
    output_data_after_challenge2["severeImpact"]["casesForVentilatorsByRequestedTime"] = severeImpact_cases_for_ventilators_by_requested_time

    #Determining dollarsInFlight
    impact_dollars_in_flight = output_data_after_challenge2["impact"]["infectionsByRequestedTime"]*data["region"]["avgDailyIncomeInUSD"]*data["timeToElapse"]
    severe_Impact_dollars_in_flight = output_data_after_challenge2["severeImpact"]["infectionsByRequestedTime"]*data["region"]["avgDailyIncomeInUSD"]*data["timeToElapse"]
    output_data_after_challenge2["impact"]["dollarsInFlight"] = round(impact_dollars_in_flight,2)
    output_data_after_challenge2["severeImpact"]["dollarsInFlight"] = round(severe_Impact_dollars_in_flight)

def estimator(data):

  #challenge 1
  challenge1_soluton(data)
  
  #challenge 2
  result =challenge2_soluton(data)

  return json.dumps(result, indent=2)


print(estimator(data))

print(round(2.339, 2))