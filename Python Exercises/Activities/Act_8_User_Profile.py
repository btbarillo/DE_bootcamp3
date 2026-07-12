sensor = {"id": "T800", "temp": 24.5}
# 1. Add "battery": 85

sensor["battery"] = 85 # Alternative way is sensor.update({"battery":85})
print(sensor)

# 2. Print: "Device T800 is at 24.5"
device = sensor["id"]
temperature = sensor["temp"]

print(f"Device {device} is at {temperature}")
