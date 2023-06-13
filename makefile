




# 	[auth]
#     changepassword
#     createsuperuser

# [contenttypes]
#     remove_stale_contenttypes

# [django]
#     check
#     compilemessages
#     createcachetable
#     dbshell
#     diffsettings
#     dumpdata
#     flush
#     inspectdb
#     loaddata
#     makemessages
makemigrations :
	python server/manage.py makemigrations
migrate :makemigrations
	python server/manage.py migrate
#     optimizemigration
#     sendtestemail
#     shell
#     showmigrations
#     sqlflush
#     sqlmigrate
#     sqlsequencereset
#     squashmigrations
#     startapp
#     startproject
#     test
#     testserver

# [sessions]
#     clearsessions

# [staticfiles]
#     collectstatic
#     findstatic
full-run :migrate
	python server/manage.py runserver 4906
run :
	python server/manage.py runserver 4906²