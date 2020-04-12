import  json
from data import data


def estimator(data):

  #challenge 1

  #estimating the currently Infected people for both impact and severeImpact 
  impact_currently_infected = data["reportedCases"]*10
  severe_currently_infected = data["reportedCases"]*50
 
  #estimating the imfected people 28 days from now for both impact and severeImpact
  impact_infections_by_requested_time = impact_currently_infected*((28//3)**2)
  severe_infections_by_requested_time = severe_currently_infected*((28//3)**2)

  #challenge 2
  impact_severe_cases_by_requested_time = impact_infections_by_requested_time*0.15
  severe_severe_cases_by_requested_time = severe_infections_by_requested_time*0.15

  impact_hospitals_beds_by_requested_time = data["totalHospitalBeds"]*0.35-impact_severe_cases_by_requested_time
  severe_hospitals_beds_by_requested_time = data["totalHospitalBeds"]*0.35-severe_severe_cases_by_requested_time

  output_data = {
    "data": data,
    "impact":{
      "currentlyInfected":impact_currently_infected,
      "infectionsByRequestedTime":impact_infections_by_requested_time,
      "severeCasesByRequestedTime":impact_severe_cases_by_requested_time,
      "hospitalBedByRequestedTime":impact_hospitals_beds_by_requested_time
    },
    "severeImpact": {
      "currentlyInfected": severe_currently_infected,
      "infectionsByRequestedTime":severe_infections_by_requested_time,
      
      "severeCasesByRequestedTime":severe_severe_cases_by_requested_time,
      "hospitalBedByRequestedTime":severe_hospitals_beds_by_requested_time
    }
  }

  return json.dumps(output_data, indent=2)
