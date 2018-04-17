Graph.png : graph.py DataEvol.txt
	python graph.py

DataEvol.txt : evolfun
	./evolfun > DataEvol.txt

evolfun :
	c++ evol.cpp -o evolfun
