from datetime import datetime
import time
import os

# Print the arguments passed
print("✅ Starting job with test 3 subfolder")
print("Checking mounted volumes ----")

# Sleep to simulate processing time
time.sleep(5)

# List all directories in the current folder
print("\n📁 Listing directories in the current folder:.........")
current_path = os.getcwd()
directories = [d for d in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, d))]
for dir_name in directories:
    print(f" - {dir_name}")

# Get the current time
current_time = datetime.now()

# Print the current time
print("\n✅ Job successfully ended.")
print("🕒 Current Server Time:", current_time)

