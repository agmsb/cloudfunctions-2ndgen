import functions_framework

@functions_framework.cloud_event
def hello_auditlog(cloud_event):

  event_data = cloud_event.data
  protoPayload = event_data['protoPayload']
  job = protoPayload['serviceData']['jobCompletedEvent']['job']
  jobStatistics = job['jobStatistics']
  createTime = jobStatistics['createTime']
  principalEmail = protoPayload['authenticationInfo']['principalEmail']
  totalBilledBytes = 0
  totalBilledGB = 0
  if 'totalBilledBytes' in jobStatistics and 'totalBIlledBytes' != 0:
        totalBilledBytes = float(jobStatistics['totalBilledBytes'])
        totalBilledGB = totalBilledBytes/(1024.0**3)
  log = 'A query was run by {} at {}, querying {} billed GB of data.'.format(principalEmail, createTime, totalBilledGB)
  print(log)
