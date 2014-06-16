#Exomondo

Exomondo is a small set of tools for endomondo.com. 
And it can download tracks!

inspired and loosely based on [isoteemu's sports-tracker-liberator](https://github.com/isoteemu/sports-tracker-liberator/blob/master/README.md)

##api module

implements couple of methods from endomondo mobile api, currently it can
- request auth token
- get workouts list using this token

##browser module

since it is not possible to download tracks using api there is some site browsing happening using splinter and requests:
- login
- download track from workout page

one of selenium web drivers required for browser module to work (tested with firefox and phantomjs, more information at [splinter homepage](http://splinter.cobrateam.info/docs/))

##exomondo_downloader

script that downloads workout tracks from endomondo.com in gpx format
for usage see 
```exomondo_downloader --help```

##warning

endomondo.com has no public documented apis and site can change any time, so exomondo itself is not that stable
