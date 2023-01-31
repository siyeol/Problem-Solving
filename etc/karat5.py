from os import sep


ad_clicks = [
  #"IP_Address,Time,Ad_Text",
  "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
  "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
  "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
  "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
  "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
  "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

completed_purchase_user_ids = [
   "3123122444","234111110", "8321125440", "99911063"]

all_user_ips = [
  #"User_ID,IP_Address",
   "2339985511,122.121.0.155",
  "234111110,122.121.0.1",
  "3123122444,92.130.6.145",
  "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
  "8321125440,82.1.106.8",
  "99911063,92.130.6.144"
]

click = dict()

for ad in ad_clicks:
    ip, time, name = ad.split(sep=",")
    if name not in click:
        click[name] = [ip]
    else:
        click[name].append(ip)

purchase=list()

for id in completed_purchase_user_ids:
    for aui in all_user_ips:
        user_id, ip_address = aui.split(sep=",")
        if user_id == id:
            purchase.append(ip_address)

for key, value in click.items():
    total = len(value)
    cnt = 0
    for ip in value:
        if ip in purchase:
            cnt+=1
    click[key] = str(cnt) + " of " + str(total)

print(click)