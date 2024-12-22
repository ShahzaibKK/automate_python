import uuid
import hashlib

# Get the machine's MAC address (stable identifier)
mac_address = str(uuid.getnode())
secret = "M_AMIR"

# Hash the MAC address
hashed_mac = hashlib.sha256((mac_address + secret).encode()).hexdigest()

# Save the hashed MAC to a license file
with open("Office_license.key", "w") as license_file:
    license_file.write(hashed_mac)

print("License key generated and saved.")
