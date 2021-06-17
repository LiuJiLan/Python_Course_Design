pack:
	pyinstaller -F ./src/School_Books_Management_System.py -w -i ./src/assets/images/icon.ico

clean:
	rm -rf ./build
	rm -rf ./dist/School_Books_Management_System
	rm -rf ./School_Books_Management_System.spec

run:pack clean
