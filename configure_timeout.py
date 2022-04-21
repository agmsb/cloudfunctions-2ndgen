import functions_framework
import logging
from time import sleep, time

@functions_framework.http
def run_to_timeout(request):

 # Run for the maximum timeout in Cloud Functions 2nd Generation
 max_timeout = time() + 3600
 time_remaining = 3600
 countdown = 'Minutes remaining for this function to process: '
 message = 'Function done processing.'

 while time() < max_timeout:
     sleep(60)
     time_remaining -= 60
     logging.warning(countdown + str(round(time_remaining/float(60), 2)))

 return message
