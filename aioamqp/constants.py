"""
    Defines our constants
"""

PROTOCOL_DEFAULT_TIMEOUT = 60
PROTOCOL_DEFAULT_PORT = 5672
PROTOCOL_HEADER = b'AMQP\x01\x01\x00\x09'

MAX_CHANNELS = 65535

# protocol
TYPE_METHOD = 1
TYPE_HEADER = 2
TYPE_BODY = 3
TYPE_HEARTBEAT = 8

FRAME_END = b'\xce'

# classes
CLASS_CONNECTION = 10
CLASS_CHANNEL = 20
CLASS_EXCHANGE = 40
CLASS_QUEUE = 50
CLASS_BASIC = 60
CLASS_TX = 90
CLASS_CONFIRM = 85

CONNECTION_START = 10
CONNECTION_START_OK = 11
CONNECTION_SECURE = 20
CONNECTION_SECURE_OK = 21
CONNECTION_TUNE = 30
CONNECTION_TUNE_OK = 31
CONNECTION_OPEN = 40
CONNECTION_OPEN_OK = 41
CONNECTION_CLOSE = 50
CONNECTION_CLOSE_OK = 51

CHANNEL_OPEN = 10
CHANNEL_OPEN_OK = 11
CHANNEL_FLOW = 20
CHANNEL_FLOW_OK = 21
CHANNEL_CLOSE = 40
CHANNEL_CLOSE_OK = 41

EXCHANGE_DECLARE = 10
EXCHANGE_DECLARE_OK = 11
EXCHANGE_DELETE = 20
EXCHANGE_DELETE_OK = 21
EXCHANGE_BIND = 30
EXCHANGE_BIND_OK = 31
EXCHANGE_UNBIND = 40
EXCHANGE_UNBIND_OK = 51

QUEUE_DECLARE = 10
QUEUE_DECLARE_OK = 11
QUEUE_BIND = 20
QUEUE_BIND_OK = 21
QUEUE_UNBIND = 50
QUEUE_UNBIND_OK = 51
QUEUE_PURGE = 30
QUEUE_PURGE_OK = 31
QUEUE_DELETE = 40
QUEUE_DELETE_OK = 41

BASIC_QOS = 10
BASIC_QOS_OK = 11
BASIC_CONSUME = 20
BASIC_CONSUME_OK = 21
BASIC_CANCEL = 30
BASIC_CANCEL_OK = 31
BASIC_PUBLISH = 40
BASIC_RETURN = 50
BASIC_DELIVER = 60
BASIC_GET = 70
BASIC_GET_OK = 71
BASIC_GET_EMPTY = 72
BASIC_ACK = 80
BASIC_REJECT = 90
BASIC_RECOVER_ASYNC = 100
BASIC_RECOVER = 110
BASIC_RECOVER_OK = 111
BASIC_NACK = 120

TX_SELECT = 10
TX_SELECT_OK = 11
TX_COMMIT = 20
TX_COMMIT_OK = 21
TX_ROLLBACK = 30
TX_ROLLBACK_OK = 31

CONFIRM_SELECT = 10
CONFIRM_SELECT_OK = 11

MESSAGE_PROPERTIES = ('content_type', 'content_encoding', 'headers', 'delivery_mode', 'priority', 'correlation_id',
                      'reply_to', 'expiration', 'message_id', 'timestamp', 'type', 'user_id', 'app_id', 'cluster_id')

FLAG_CONTENT_TYPE = (1 << 15)
FLAG_CONTENT_ENCODING = (1 << 14)
FLAG_HEADERS = (1 << 13)
FLAG_DELIVERY_MODE = (1 << 12)
FLAG_PRIORITY = (1 << 11)
FLAG_CORRELATION_ID = (1 << 10)
FLAG_REPLY_TO = (1 << 9)
FLAG_EXPIRATION = (1 << 8)
FLAG_MESSAGE_ID = (1 << 7)
FLAG_TIMESTAMP = (1 << 6)
FLAG_TYPE = (1 << 5)
FLAG_USER_ID = (1 << 4)
FLAG_APP_ID = (1 << 3)
FLAG_CLUSTER_ID = (1 << 2)
