import logging
import datetime

import azure.functions as func

from src.daily_check import run_daily_trigger

def main(dayTrigger: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

    run_daily_trigger()

    if dayTrigger.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    