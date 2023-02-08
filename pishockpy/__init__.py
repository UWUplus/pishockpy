import requests
import json

pishock_url = "https://do.pishock.com/api/apioperate/"

errors = {
  "This code doesn't exist.": "The specified share code could not be found. Make sure you create and copy an active share code from the PiShock website.",
  "Not Authorized.": "The specified username or apikey is not correct (or your account has not been activated).",
  "Shocker is Paused, unable to send command.": "The shocker is paused (from the PiShock.com web panel).",
  "Device currently not connected.": "The PiShock is offline.",
  "This share code has already been used by somebody else.": "Someone (or something) else is using the specified share code. Generate a new one.",
  "Unknown Op, use 0 for shock, 1 for vibrate and 2 for beep.": "Invalid Op code specified. Must be 0, 1, or 2.",
  "Intensity must be between 0 and 100": "The specified intensity was outside the permitted range.",
  "Duration must be between 0 and 15": "The specified duration was outside the permitted range."
}

# Check if a response from the server is valid
# If the response is not valid, raise an exception
# If the response is valid, return True
def check_response(response):
  if response.status_code != 200:
    raise ValueError("Invalid response from server: {}".format(response.text))
  if response.text == "Operation Succeeded.":
    return True
  if response.text in errors:
    raise ValueError(errors[response.text])

class PishockAPI(object):
  def __init__(self, api_key: str, username: str, sharecode: str, app_name: str):
    self.api_key: str = api_key
    self.username: str = username
    self.app_name: str = app_name
    self.sharecode: str = sharecode
    self.base_url: str = pishock_url
    self.header: Dict[str, str] = {"Content-Type": "application/json", "User-Agent": "PishockPy/0.0.1"}

  def shock(self, intensity: float, duration: int):
    # sanity checks
    """Shock the user with the specified intensity and duration. Intensity must be between 0 and 1, 
    duration must be between 0 and 15 (or 300 for 0.5 seconds)"""
    if intensity < 0 or intensity > 1:
      raise ValueError("Intensity must be between 0 and 1")
    if duration < 0 or duration > 15 and duration != 300:
      raise ValueError("Duration must be between 0 and 15")
    """Convert intensity to a percentage"""
    intensity = (int)(intensity * 100)
    data = {"Username": self.username,"Name": self.app_name,"Code":self.sharecode,"Intensity": intensity,"Duration": duration,"Apikey": self.api_key,"Op":"0"}
    """Send the request"""
    response = requests.post(self.base_url, headers = self.header, data = json.dumps(data))
    return check_response(response)

  def minishock(self, intesity: float):
    """A shortcut for a 0.5 second shock at the specified intensity"""
    return self.shock(intesity, 300)

  def vibrate(self, intensity: float, duration: int):
    # sanity checks
    """Vibrate the user with the specified intensity and duration. Intensity must be between 0 and 1, 
    duration must be between 0 and 15"""
    if intensity < 0 or intensity > 1:
      raise ValueError("Intensity must be between 0 and 1")
    if duration < 0 or duration > 15:
      raise ValueError("Duration must be between 0 and 15")
    """Convert intensity to a percentage"""
    intensity = (int)(intensity * 100)
    data = {"Username": self.username,"Name": self.app_name,"Code":self.sharecode,"Intensity": intensity,"Duration": duration,"Apikey": self.api_key,"Op":"1"}
    """Send the request"""
    response = requests.post(self.base_url, headers = self.header, data = json.dumps(data))
    return check_response(response)

  def beep(self, duration: int):
    if duration < 0 or duration > 15:
      raise ValueError("Duration must be between 0 and 15")
    data = {"Username": self.username,"Name": self.app_name,"Code":self.sharecode,"Duration": duration,"Apikey": self.api_key,"Op":"2"}
    response = requests.post(self.base_url, headers = self.header, data = json.dumps(data))
    return check_response(response)