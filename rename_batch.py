import os
path='output' #這就是欲進行檔名更改的檔案路徑，路徑的斜線是為/，要留意下！
files=os.listdir(path)
print('files') #印出讀取到的檔名稱，用來確認自己是不是真的有讀到

n=0 #設定初始值
for i in files: #因為資料夾裡面的檔案都要重新更換名稱
	oldname=path+files[n] #指出檔案現在的路徑名稱，[n]表示第n個檔案
	newname=path+'im'+str(n+1)+'.jpg' #在本案例中的命名規則為：年份+ - + 次序，最後一個.wav表示該檔案的型別
	os.rename(oldname,newname)
	print(oldname+'>>>'+newname) #印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應
	n=n+1 #當有不止一個檔案的時候，依次對每一個檔案進行上面的流程，直到更換完畢就會結束