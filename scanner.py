import sys
from datetime import datetime
import socket

if len(sys.argv) == 2:
	host = socket.gethostbyname(sys.argv[1])
else:
	print('Syntax mistake.')

print("*-"*17+"*\nScanning ports 1 to 1000", f"\nOn Time: {datetime.now()}" + f"\nScanning ip {host}\n" + "*-"*17+"*")
try:
	for i in range(1,1000):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((f'{host}',i))
		if result == 0:
			print(f"Successful connection to port {i}")
		s.close()

except KeyboardInterrupt:
	print("\nOK BOSS! Exiting.")
	sys.exit()

except socket.gaierror:
	print("IP cannot be resolved.")
	sys.exit()

except socket.error:
	print("Connection Problem.")	
	sys.exit()	
