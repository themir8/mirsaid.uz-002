
push:
	git add \.
	git commit -m 'initial project version'
	git push

run: manage.py
	python manage.py runserver