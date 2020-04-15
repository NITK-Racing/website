# NITK RACING WEBSITE

##instructions
* install latest version of django
* install latest version of python 3
* install pycharm professional (get student licence)
* clone repo

##to start server
1. open pycharm and file>open>[filepath]/nitk_racing
2. at the bottom there is terminal option type the following
    * python3 manage.py runserver
    * server is now running at local host port :8000

## work for shende
* learn about django template language its v easy google it
* all html files are located in nitk_racing/mysite/templates
* index has been somewhat modified and is nearly complete
    use it as reference
* multiple arrays of objects are made available to each html page
    * 'banners_list':
    * 'sponsors_list': 
    * 'sig_head_list': 
    * 'image_gallery_full':
    * 'image_gallery_short':
    * 'full_member_list': 
* the above can be accessed via for loop in html file like
    * {% for x in sponsors_list%}
        
        {%end for%}    
    * look at index html for reference
* back end for 4 pages are ready
    * index located at href= '  '
    * team located at href= './team'
    * contact located at href= './contact'
    * about located at href= './about'
* you will have to import all css and js files using static tag
(see index.html for refernece) all image url should be replaced with either static tag or 
refernced via an object of the feild (see index html for refernece)
* store all non changin(static files in ) mysite/static directory

* admin dash board can be accessed using localhost:8000/admin
    username is admin and password is in description of wa group
* photos and member details can be added via gui from admin dashboard
 