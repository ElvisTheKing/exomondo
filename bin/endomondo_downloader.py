from splinter import Browser
import requests
import click
import re
import logging
logging.basicConfig(level=logging.DEBUG)


@click.command()
@click.argument('username')
@click.argument('password')
def download(username,password):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"
    b = Browser('phantomjs',user_agent=user_agent)
    try:
        b.visit('http://www.endomondo.com')
        b.find_link_by_href('login').first.click()

        b.fill('email',username)
        b.fill('password',password)
        b.find_by_css('div.signInButton').first.click()

        b.visit('http://www.endomondo.com/workouts/list')

        b.find_by_css('tbody.compareShadow td.title').first.click()
        b.find_by_css('span.more').first.mouse_over()
        b.find_by_css('a.export').first.click()

        # b.find_by_css('div.wizard a').last.click()

        m = re.search('<a href="\.\./(.+?exportGpxLink.+?)">',b.html)
        url = 'http://www.endomondo.com/'+m.group(1)

        cookies = dict(map(lambda cookie: (cookie['name'],cookie['value']), b.cookies.all()))
        headers = {'User-Agent': user_agent}        
        r = requests.get(url, cookies = cookies, headers = headers)
        
        print(r.url)
        print(r.headers)
        print(r.status_code)
        print(r.text)

    finally:
        b.screenshot('/Users/zz/Dropbox/Workspace/python/endomondo_track_downloader/bin/scr/')

if __name__ == '__main__':
    download()
