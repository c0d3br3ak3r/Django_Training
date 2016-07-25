import urllib.parse
import urllib.request

def sendOTP(code):
    OTP = code
    authkey = "118913AH5kKDctH7BZ578155bf" # Your authentication key.
    mobiles = "919700566714" # Multiple mobiles numbers separated by comma.
    message = "Your OTP verification code is :  " + OTP  # Your message to send.
    sender = "SOCITY" # Sender ID,While using route4 sender id should be 6 characters long.
    route = "default" # Define route

    # Prepare you post parameters
    values = {
              'authkey' : authkey,
              'mobiles' : mobiles,
              'message' : message,
              'sender' : sender,
              'route' : route
              }

    url = "https://control.msg91.com/api/sendhttp.php" # API URL
    postdata = urllib.parse.urlencode(values) # URL encoding the data here.
    postdata = postdata.encode('utf-8')
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req,postdata)
    output = response.read().decode('utf-8') # Get Response
    print(output) # Print Response

if __name__=="__main__":
    sendOTP("DX12354")
