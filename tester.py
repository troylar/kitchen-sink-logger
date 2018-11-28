from kitchen_sink_logger import KitchenSinkLogger
import logging
from handler import KinesisFirehoseHandler
from formatter import SimpleJsonFormatter
from backpack import Backpack
from state_manager import StateManager

logger = KitchenSinkLogger()
logger.with_level(logging.INFO)
handler = KinesisFirehoseHandler(stream_name='pollexy-logging')
handler.setFormatter(SimpleJsonFormatter())
logger.with_handler(handler)
logger.with_timer("TestTimer")
logger2 = logger.clone()
logger.with_item('test', 'value')
j = logger.backpack.to_json()

sm = StateManager(TableName='BackpackState')
sm.upsert(logger.backpack)
b = sm.get(logger.backpack.id)
print('logging info')
logger.info('starting')
logger.log_metric("Getting data", "ReadsPerSecond", 100)
