from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(' ', '_')

print(date)