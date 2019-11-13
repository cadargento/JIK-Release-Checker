import spotipy
import spotipy.util as util
from config import *
import smtplib, ssl
import time

def send_email(a):
    '''
    s = smtplib.SMTP(host='your_host_address_here', port=465)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    '''
    port = 465
    sender_email = MY_ADDRESS
    receiver_email = 'giucecrew@gmail.com'
    message = f'The album {a} is released on spotify!'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(MY_ADDRESS, PASSWORD)
        server.sendmail(sender_email, receiver_email, message)
        #server.sendmail(sender_email, 'jned2000@yahoo.com', message)

def album_parse(where_is_JIK):
    keywords = ['KIDS', 'ye', 'Pablo', 'Yeezus', 'Presents', 'Beautiful', '808', 'Graduation', 'Late']
    for a in where_is_JIK:
        if (keywords[0] not in a and keywords[1] not in a and
                keywords[2] not in a and keywords[3] not in a and
                keywords[4] not in a and keywords[5] not in a and
                keywords[6] not in a and keywords[7] not in a and
                keywords[8] not in a):
            #send_email(a)
            #print(a)
            return True, a
    return False, None

def analyzer():
    token = util.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    cache_token = token.get_access_token()
    sp = spotipy.Spotify(cache_token)
    where_is_JIK = []
    while(1):
        yeezy_search = sp.search(q='Kanye West', type='artist',limit='1')
        kanye_id = yeezy_search['artists']['items'][0]['id']
        albums = sp.artist_albums(kanye_id)

        for i,a in enumerate(albums['items']):
            #print(i,a['name'])
            if a['name'] not in where_is_JIK:
                where_is_JIK.append(a['name'])

        (email, album_name) = album_parse(where_is_JIK)
        if email:
            #send_email(album_name)
            break
        time.sleep(1800)
    print('Kanye west has released the album {}!'.format(album_name))
    return
if __name__ == '__main__':
    while(1):
        analyzer()
        time.sleep(60 * 30)

