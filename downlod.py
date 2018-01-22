import progressbar
import requests

url = input('Enter download Link')
def download_file(url):
    r = requests.get(url, stream=True)
    filename = r.url.split('/')[-1]
    f = open(filename, 'wb')
    file_size = int(r.headers['Content-Length'])
    bar =  progressbar.ProgressBar(max_value=file_size).start()
    i = 0
    for chunk in r.iter_content():
        f.write(chunk)
        bar.update(i)
        i+=1
    f.close()
    return
download_file(url)

#https://yoourl.me/img
#