# Testing the parsedatetime library
This is just a toy project to play with the [parsedatetime](https://github.com/bear/parsedatetime) library.

To setup your environment to see the tests, run the following:
```
./setup.sh
```
This will create a `virtualenv` in your current directory and install the `parsedatetime` library. It will then run the `test.py` file.

The test cases are contained in the `samples.json` file. To test additional phrases just add them to the `samples.json` file and then run:
```
python test.py
```

