
all: tests

statistics:
	python3 bubble_sort.py >> saved_statistics/data &
	python3 bucket_sort.py >> saved_statistics/data &
	python3 insertion_sort.py >> saved_statistics/data &
	python3 merge_sort.py >> saved_statistics/data &
	python3 quick_sort.py >> saved_statistics/data &

run:
	python3 algorithms.py

tests:
	python3 -m doctest node.py
	python3 -m doctest linked_list.py
	python3 -m doctest utils.py
	# sorting algorithms
	python3 -m doctest bubble_sort.py
	python3 -m doctest bucket_sort.py
	python3 -m doctest insertion_sort.py
	# python3 -m doctest gnome_sort.py
	python3 -m doctest merge_sort.py
	python3 -m doctest quick_sort.py


