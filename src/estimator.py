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

def estimator(data):

  #challenge 1
  result = challenge1_soluton(data)
  return json.dumps(result, indent=2)


print(estimator(data))
