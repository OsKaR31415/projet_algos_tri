
all: tests

run:
	python3 algorithms.py

tests:
	python3 -m doctest node.py
	python3 -m doctest linked_list.py
	python3 -m doctest utils.py
	python3 -m doctest algorithms.py


