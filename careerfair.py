#!/usr/bin/python
from appscript import app
from random import shuffle, randint
import time
from itertools import cycle
import os


items = (56345233, 56344561, 56344511, 56373604, 37216217, 54220776, 55513454, 
         54332142, 30811273, 39601446, 55258812, 
)


shops = ('stellarquilts', 'jasontennant', 'pommesfrites', 'yokoo', 'juliapott', 
         'sevenbc', 'swankarama', 'WalnutStudiolo', 'girlsavage', 
)


office_pics = (
    'http://www.flickr.com/photos/rawfishdesigns/4523753493/',
    'http://www.flickr.com/photos/goobeetsa/4522105458/',
    'http://www.flickr.com/photos/dining-car/4918105142/', 
)

treasuries = (
    '4c90c20e51146d910d7d56cb', '4c903d3fb6b38eefb768809b', 
    '4c8d912de3548eefba237113', 
)


recruiting_video = (13214706, 3.5*60)


videos = [(9682073, 7*60), (375970, 60),]


html = """
<html>
<head>
<title>video</title>
</head>
<body>
<iframe src="http://player.vimeo.com/video/%s?autoplay=1" width="100%%" height="100%%" frameborder="0"></iframe><p><a href="http://vimeo.com/13214706">News Flash: Etsy is hiring!</a> from <a href="http://vimeo.com/etsy">Etsy</a> on <a href="http://vimeo.com">Vimeo</a>.</p>
</body>
</html>
"""


safari = app('Safari')


def show(url):
    safari.document.URL.set(url)
    safari.activate()


def write_vid(l):
    p = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vid.html')
    open(p, 'w').write(html % l)
    return 'file:///' + p


def show_link(l):
    if isinstance(l, tuple):
        l, delay = l
        l = write_vid(l)
    else:
        delay = randint(3, 7)
    show(l)
    time.sleep(delay)


def run():
    links = ['http://www.etsy.com/listing/%s' % x 
             for x in items]
    links.extend(['http://www.etsy.com/shop/%s' % x
                  for x in shops])
    links.extend(['http://www.etsy.com/treasury/%s' % x
                  for x in treasuries])
    links.extend(office_pics)
    links.extend(videos)

    shuffle(links)
    links = cycle(links)
    i = 0
    try:
        for l in links:
            show_link(l)
            i += 1
            if i % 10 == 0:
                show_link(recruiting_video)    
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
