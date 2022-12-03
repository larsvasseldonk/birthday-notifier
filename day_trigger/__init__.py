import logging
import datetime

import azure.functions as func
from opencensus.ext.azure.log_exporter import AzureLogHandler

from src.daily_check import run_daily_trigger

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(
    connection_string="InstrumentationKey=cb0b5774-f68f-4abc-a255-c87b830fd0be"
    )
)


def main(dayTrigger: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

    run_daily_trigger()

    if dayTrigger.past_due:
        logger.info('The timer is past due!')

    logger.info('Python timer trigger function ran at %s', utc_timestamp)
    