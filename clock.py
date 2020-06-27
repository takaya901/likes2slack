from apscheduler.schedulers.blocking import BlockingScheduler
import likes2slack_heroku

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=5)
def timed_job():
    likes2slack_heroku.post()

if __name__ == "__main__":
    twische.start()