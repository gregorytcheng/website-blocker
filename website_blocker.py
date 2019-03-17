import time
from datetime import datetime as dt

hosts_temp = "hosts"
host_path = "/etc/hosts"
redirect_ip_address = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    current_year = dt.now().year
    current_month = dt.now().month
    current_day = dt.now().day
    # Between hour 8 (8am) and hour 16 (4pm)
    # If our current time falls between these times, we must assure that the appropriate websites are the in host file.
    if dt(current_year, current_month, current_day, 8) < dt.now() < dt(current_year, current_month, current_day, 16):
        print("Working hours...")
        # Open file
        with open(hosts_temp, 'r+') as hosts_file:
            file_content = hosts_file.read()
            # Loop through all websites in blocked list and check if they are in the file.
            for website in website_list:
                if website in file_content:
                    pass
                else:
                    hosts_file.write(redirect_ip_address + " " + website + '\n')

    # If our current time does not fall within these times, we must assure that the appropriate website are NOT in
    # the host file.
    else:
        print("Not working hours...")
        with open(hosts_temp, 'r+') as hosts_file:
            host_file_lines = hosts_file.readlines()
            # Place the file pointer at position 0 (the start of the file)
            hosts_file.seek(0)
            for hosts_file_line in host_file_lines:
                if not any(website in hosts_file_line for website in website_list):
                    hosts_file.write(hosts_file_line)
            # Truncate file (delete everything downward from the cursor)
            hosts_file.truncate()
    time.sleep(60)