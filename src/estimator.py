import  json
from data import data

output_data = {
    "data":data,
    "impact":{},
    "severeImpact":{}
}


def get_duration(data):

    if data['periodType'] == 'months':
        duration = data['timeToElapse']*30
    elif data['periodType'] == 'weeks':
        duration = data['timeToElapse']*7
    else:
        duration = data['timeToElapse']*1
    return duration

def estimator(data):

  #challenge 1
  
  

  return json.dumps(output_data, indent=2)
