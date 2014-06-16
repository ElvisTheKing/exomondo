import os
import time
import click
import logging
import endomondo

logging.basicConfig(level=logging.INFO)

@click.command()
@click.argument('email')
@click.argument('password')
@click.option('--out', help = 'directory to download files into', default = '.' )
@click.option('--webdriver', help = 'web_driver to use for browser interactions', default = 'phantomjs')
@click.option('--limit', help = 'maximum tracks to download', default = 10)

def download(email,password, out, webdriver, limit):
    out = os.path.abspath(out)

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"
    
    api = endomondo.Api(email, password, user_agent = user_agent)
    browser = endomondo.Browser(email = email, password = password, user_agent = user_agent, webdriver = webdriver)  

    workouts = api.get_workouts(limit)
    logging.info('will get %d workouts' % len(workouts))
    
    for workout in workouts:
        track = browser.download_track(workout['id'])
        if not track:
            continue

        start_time = time.strptime(workout['start_time'], '%Y-%m-%d %H:%M:%S %Z')
        start_time_str = time.strftime('%Y-%m-%d_%H-%M-%S',start_time) 
        if 'name' in workout:
            name = '(%s)'%workout['name']
        else: 
            name = ''
        
        filename = os.path.join(out,"%s%s.gpx" %(start_time_str,name))
        logging.info('writing track to %s' % filename)
        with open(filename,'w') as f:
            f.write(track)


if __name__ == '__main__':
    download()
