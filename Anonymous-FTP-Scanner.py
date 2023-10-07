from ftplib import FTP


def Banner():

	print("""                                         _ ___ _     __                       
  /\  ._   _  ._     ._ _   _       _   |_  | |_)   (_   _  _. ._  ._   _  ._ 
 /--\ | | (_) | | \/ | | | (_) |_| _>   |   | |     __) (_ (_| | | | | (/_ |  
                  /                                                           """)

def anonLogin(hostname):
	try:
		ftp = FTP(hostname)
		ftp.login('anonymous')
		print('[+]'+str(hostname)+ ' FTP Anonymous Login Vulnerable')
		ftp.quit()
		return True
	except Exception:
		print('[-]'+str(hostname)+ ' FTP Anonymous Login NOT Vulnerable')
		return False

if __name__ == '__main__':
	
	Banner()
	host = input("Enter the Host IP :")
	print("\n")
	anonLogin(host)		