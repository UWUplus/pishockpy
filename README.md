# pishockpy

Comfortably use the [PiShock](https://PiShock.com) API in Python.  
This requires at least `Python 3.8`

## Usage
Import the package:
```python
from pishockpy import PishockAPI
```
Declare a new shocker instance:
```python
pishock = PishockAPI("YOUR_API_KEY", "YOUR_USERNAME", "SHARECODE", "YOUR_APP_NAME")
```
Run actions on a shocker:
```python
# Send a shock - intensity (float between 0 and 1) and duration in seconds (integer between 1 and 15)
pishock.shock(INTENSITY, DURATION)

# Send a mini shock - intensity (float between 0 and 1)
pishock.minishock(INTENSITY)

# Send a vibration - intensity (float between 0 and 1) and duration in seconds (integer between 1 and 15)
pishock.vibrate(INTENSITY, DURATION)

# Send a sound - duration in seconds
pishock.beep(DURATION)

```

Check if an action was successful:
```python
if(pishock.shock(INTENSITY, DURATION)):
    print("Shock was successful")
else:
    print("Shock was not successful")
```

### Disclaimer
I'm not affiliated with PiShock in any way. I am also not responsible for any damage caused by this library.