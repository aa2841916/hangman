import urllib
import os
import lxml.html,requests
url = "https://www.python.org/dev/peps/pep-0020/"
xpath = '//*[@id="the-zen-of-python"]/pre/text()'
res = requests.get(url)
ht = lxml.html.fromstring(res.text)
text = ht.xpath(xpath)
yami = ('Hello,\n'+''.join(text))
with open('st.txt','w') as f:
    f.write(yami)