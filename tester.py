from kitchen_sink_logger import KitchenSinkLogger
from handler.firehose import KinesisFirehoseHandler
from json_formatter.json import SimpleJsonFormatter
from backpack import Backpack
from state_manager import StateManager
import time
import logging

logger = KitchenSinkLogger()
logger.with_level(logging.INFO)
handler = KinesisFirehoseHandler(stream_name='STREAM_NAME')
handler.setFormatter(SimpleJsonFormatter())
logger.with_handler(handler)
logger.with_timer("TestTimer")
time.sleep(2)
logger.with_timer("SecondTimer")
logger2 = logger.clone()
logger.with_item('test', 'value')
j = logger.backpack.to_json()

sm = StateManager(TableName='BackpackState')
sm.upsert(logger.backpack)
logger.backpack = sm.get(logger.backpack.id)
logger.info('starting')
logger.log_metric("Getting data", "ReadsPerSecond", 100)
