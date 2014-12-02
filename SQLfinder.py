import re, urllib2
import sqlcrawler
print """DarkDevilz | Gece Kadar Sessiz, Olum Kadar Ansiz..
,------.                 ,--.    ,------.                  ,--.,--.       
|  .-.  \  ,--,--.,--.--.|  |,-. |  .-.  \  ,---.,--.  ,--.`--'|  |,-----.
|  |  \  :' ,-.  ||  .--'|     / |  |  \  :| .-. :\  `'  / ,--.|  |`-.  / 
|  '--'  /\ '-'  ||  |   |  \  \ |  '--'  /\   --. \    /  |  ||  | /  `-.
`-------'  `--`--'`--'   `--'`--'`-------'  `----'  `--'   `--'`--'`-----'
www.darkdevilz.org                                   Kara Ayaz (karaayaz_)"""
print "ddzCrawler (sql crawler and finder) Beta Versiyon"""
print ""

dork = raw_input("Dork: ")
def finder(dork):
    first = 1
    while first<=91:
        response = urllib2.urlopen("http://www.bing.com/search?q={}&first={}".format(dork, first))
        payload = response.read()
        results = re.findall('<h2><a(.*?)h="', payload)
        for result in results:
            result = result.lstrip(" href=")
            result = result.lstrip('"')
            result = result.rstrip('" ')
            vict = result
            sqlcrawler.scan(vict)
        first = first + 10
finder(dork)
raw_input()
