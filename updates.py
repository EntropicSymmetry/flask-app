def regexForDates(st):
  
  #Import libs required for datefinding
  import datefinder, re, sys
  
  #Define regex base to be used be sys
  regexChecks = """	
^((((0[13578])|([13578])|(1[02]))[\/](([1-9])|([0-2][0-9])|(3[01])))|(((0[469])|([469])|(11))[\/](([1-9])|([0-2][0-9])|(30)))|((2|02)[\/](([1-9])|([0-2][0-9]))))[\/]\d{4}$|^\d{4}$"""
  return list(datefinder.find_dates(st))

def storeReminderDates(metadata, username):
  
  #Get datelist from text
  dateListRecord = regexForDates(str(resp_metadata.json()['latest_message']))

  #Check if any dates were found
  if bool(dateListRecord) == True:

    #Get mongo client
    import pymongo
    client = pymongo.MongoClient("mongodb+srv://dbUser:deUserPassword@Stella@uwc-ca.7fijl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    #Insert each datetime in mongo
    [client.Stella.KeyWords.update_one({"_id":username}, {"$push":{"DateList":FoundDate}}) for FoundDate in dateListRecord]
  
#Create a cron job function to get reminders:
def getReminders():
  
  #Create a reminder list to store usernames with reminders
  reminderList = []
   storeThisUser = False
    
  #Loop thrugh all users and see if any has a reminder to be ste
  allUsers  = list(client.Stella.KeyWords.find({}))
  for oneUser in allUsers:
    
    #Put a try statement in case any errors are encountered while reading data
    try:
      for Storeddate in oneUser['DateList']:
        
        #Check if date is for tomrrow (can change this to anything by altering the delta)
        if StoredDate == datetime.date.today() + datetime.timedelta(days=1):
          storeThisUser = True
   
    #If there is a date, add the user to the reminder list.
    if storeThisUser == True:
      reminderList.append(oneUser)
      
    except Exception as e:
      pass
    
    return reminderList
