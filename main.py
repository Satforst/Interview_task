import schedule
import time
from datetime import datetime
from download import Download
download = Download()


def time_writer():
    time_dict = download.get_time()
    if isinstance(time_dict, dict):
        try:
            my_timestamp = time_dict['serverTimestamp']
            try:
                # transfer timestamp to datetime
                my_datetime = datetime.fromtimestamp(my_timestamp/1000)
                print(my_datetime)
        # errors for unexpected input
            except ValueError as error:
                print(error)
        except KeyError as error:
            print(error)


if __name__ == '__main__':
    print("Start printing time every 1 minute.")
    time_writer()
    schedule.every(1).minutes.do(time_writer)
    while True:
        schedule.run_pending()
        time.sleep(1)
