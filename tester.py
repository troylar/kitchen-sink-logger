from kitchen_sink_logger import KitchenSinkLogger
import logging
from handler import KinesisFirehoseHandler
from formatter import SimpleJsonFormatter
from backpack import Backpack
from state_manager import StateManager

logger = FluentLogger()
handler = KinesisFirehoseHandler(stream_name='pollexy-logging')
handler.setFormatter(SimpleJsonFormatter())
logger.with_handler(handler)
logger.with_timer("TestTimer")
logger2 = logger.clone()
print(logger2.backpack.to_json())
quit()
logger.with_item('test', 'value')
j = logger.backpack.to_json()
print(j)
print(logger.backpack.from_json(j))

sm = StateManager(TableName='BackpackState')
sm.upsert(logger.backpack)
b = sm.get(logger.backpack.id)
print(b.id)
print(b.perm_items)
print(b.timers)
#logger.log_metric("Getting data", "ReadsPerSecond", 100)
