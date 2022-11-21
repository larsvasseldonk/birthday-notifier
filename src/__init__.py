import logging
import datetime

import azure.functions as func

from birthday_notifier.src.main import run_daily_trigger

def main(dayTrigger: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

    run_daily_trigger.main()

    if dayTrigger.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    