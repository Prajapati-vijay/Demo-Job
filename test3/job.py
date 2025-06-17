from datetime import datetime
import time
import sys

# Print the arguments passed
print("✅ Starting job with test 3 subfolder")
print("Agrs are : ----")
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
time.sleep(80)
# Get the current time
current_time = datetime.now()

# Print the current time
print(" Job successfully ended and Current Server Time:", current_time)   
