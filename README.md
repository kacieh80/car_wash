## Car Wash

This is a simple python program that takes an input file of vehicles and runs them through a car wash. It prints out what was done for each vehicle. The rules for this car wash are as follows:

- The car wash accepts cars and trucks.
- Charge $5 for cars.
- Charge $10 for trucks.
- The car wash charges $2 extra if the truck has mud in the bed.
- The car wash does not accept trucks with the bed let down.
- If the vehicle comes in a second time, they get 50% off.
- If the license plate equals 111111 the car is stolen and you will not wash it

To run this application you'll need python3 and virtualenv, download the code from this repository and run the following commands:

`cd car_wash`

`virtualenv -p python3 app`

`cd app`

`source bin/activate`

`python3 car_wash.py automobile.txt`


For tests

`pip3 install requierments.txt`

`python3 -m unittest`
