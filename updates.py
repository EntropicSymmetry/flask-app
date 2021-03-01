def regexForDates(st):
  import datefinder, import re
  regexChecks = ["|/A_z?1_10/|"]
  return list(datefinder.find_dates(st))

dateListRecord = regexForDates(str(resp_metadata.json()['latest_message']))

if bool(dateListRecord) == True:
  
