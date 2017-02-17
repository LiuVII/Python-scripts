from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive   
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


file_list = drive.ListFile({'q': "'0B1vi4ZYngkYQMzBWamRmemZOXzg' in parents and trashed=false"}).GetList()
for file1 in file_list:
	if file1['title'] == 'user_data.json':
		file1.SetContentFile('user_data.json')
		file1.Upload()
		print('File updated')
		break
