from mechanize import Browser
from bs4 import *
from time import *
import re
import datetime

mech = Browser()

mech.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

mech.set_handle_robots(False)

f = open('sarpy-prop-vals.txt','wb')

f.write("parcel|address|valuation|tax13\n")

assurl = "http://www.sarpy.com/sarpyproperty/pdisplay3.aspx?locid="
taxurl = "http://www.sarpy.com/sarpyproperty/TrStatement.aspx?StatementLookup=2013-"

parcels = ['010748792', '010537449', '010537023', '010537481', '011591964', '010765174', '010944656', '010944648', '011100389', '010549781', '010537341', '010562028', '011181583', '011254750', '011254769', '011234237', '011234245', '011254734', '011254742', '011181656', '011181648', '011181621', '011181605', '011181613', '011181591', '011288353', '011288345', '011288337', '011122536', '011288388', '011288361', '011175656', '011045507', '010974458', '011047305', '011047313', '010974482', '010974466', '011047321', '010581111', '011082828', '011046414', '010580999', '010485651', '010973257', '010581170', '010504737', '010580468', '010580549', '010580727', '010580646', '010973737', '010584390', '010561811', '010561994', '010562087', '010560769', '010571175', '010571256', '010571264', '010561900', '010584226']

test = '010748792'

page = mech.open(taxurl + test)
html = page.read()
soup = BeautifulSoup(html)

texts = soup.findAll('input', {'type':'text'})

for thing in texts:
    print thing['value']

f.flush()
f.close()
