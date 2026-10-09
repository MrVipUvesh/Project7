import datetime as dt
import time

date_format = "%d/%m/%y - %I:%M:%S %p"
class DtOperations:
    def current_dt(self):
        datetime = dt.datetime.now().strftime(date_format)
        return f"Current Date and Time: {datetime}"

    def difference(self, date1, date2):
        d1 = dt.datetime.strptime(date1, "%Y/%m/%d")
        d2 = dt.datetime.strptime(date2, "%Y/%m/%d")

        difference = d1 - d2
        return f"Difference: {abs(difference)}"

    def change_format(self, format):
        global date_format
        if(format.lower() == "y/d/m"):
            date_format = "%y/%d/%m - %I:%M:%S %p"
            print(f"Date format set to: {date_format}")
        elif(format.lower() == "m/d/y"):
            date_format = "%m/%d/%y - %I:%M:%S %p"
            print(f"Date format set to: {date_format}")
        elif(format.lower() == "y/m/d"):
            date_format = "%y/%m/%d - %I:%M:%S %p"
            print(f"Date format set to: {date_format}")
        elif(format.lower() == "m/y/d"):
            date_format = "%m/%y/%d - %I:%M:%S %p"
            print(f"Date format set to: {date_format}")
        elif(format.lower() == "d/y/m"):
            date_format = "%d/%y/%m - %I:%M:%S %p"
            print(f"Date format set to: {date_format}")
        elif(format.lower() == "d/m/y"):
            date_format = "%d/%m/%y - %I:%M:%S %p"
            print(f"Date format set to: {date_format}")
        else:
            print("Date format not set correctly.")

    def stopwatch(self):
        input("Press ENTER to start")
        start = time.perf_counter()
        input("Press ENTER to stop")
        stop = time.perf_counter()
        total_time = stop - start
        return f"\nTime: {total_time:.2f} seconds"

    def countdown(self, limit):
        for i in range(limit, 0, -1):
            if(i < 0):
                break
            print(f"{i} second(s) left")
            time.sleep(1)
            i -= 1
            if(i == 0):
                print("Time's Up!")