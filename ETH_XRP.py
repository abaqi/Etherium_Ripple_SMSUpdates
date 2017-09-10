from lxml import html
import requests
import smtplib

#Scrapping Etherium price
eth = requests.get('https://ethereumprice.org/')

tree = html.fromstring(eth.content)

eth_p = tree.xpath('//span[@class="rp"]/text()')
print (eth_p[0])

#Scrapping Ripple price
xrp = requests.get('https://ethereumprice.org/xrp')

tree = html.fromstring(xrp.content)

xrp_p = tree.xpath('//span[@class="rp"]/text()')
print (xrp_p[0])

#Establishing server to send number
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.ehlo()
server.starttls()

#Send the message
server.login( '****@gmail.com', 'gmail password' )
server.sendmail('****@gmail.com', '<Tmobile#>@tmomail.net','{} {}'.format(eth_p[0] , xrp_p[0]))
