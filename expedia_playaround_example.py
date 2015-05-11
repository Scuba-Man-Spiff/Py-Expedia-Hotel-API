import urllib.request
import urllib.error
from hashlib import md5
import time

service = 'http://api.ean.com/ean-services/rs/hotel/'
version = 'v3/'
method = 'list/'
hotelId = '201252'
#  Toss his in a dict for easy maintenance


timestamp = str(int(time.time()))

prehash = apiKey + secret + str(timestamp)

sig = md5(prehash.encode('utf-8')).hexdigest()

url = service + version + method+ '?apiKey=' + apiKey + '&sig=' + sig + '&' \
    + otherElementsStr + '&hotelIdList=' + hotelId

hotelXml = urllib.request.urlopen(url).read()

