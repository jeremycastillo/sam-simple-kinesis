from http import HTTPStatus
import pytest

from simple_kinesis import app

# disable sleep
app.CONTEXT_SLEEP_TEST_SECONDS = 0


@pytest.fixture()
def lambda_event_valid():
    return {
        'Records': [
          {
            'kinesis': {'data': 'eW8gbW9tbWE='}
          }
        ]
    }

@pytest.fixture()
def lambda_event_invalid():
    return {
        'Records': [
          {
            'kinesis': {'data': 'ZGVybw=='}
          }
        ]
    }


@pytest.fixture()
def lambda_context():
    return MockContext()


class MockContext:
    def __init__(self):
        self.log_stream_name = '2019/1/15/[$LATEST]b684e04267f11ba5'
        self.log_group_name = '/aws/lambda/test'
        self.aws_request_id = '1'
        self.memory_limit_in_mb = 128

    def get_remaining_time_in_millis(self):
        return 30000


def test_handler_valid(lambda_event_valid, lambda_context):
    response = app.lambda_handler(lambda_event_valid, lambda_context)
    assert response['valid'] == True

def test_handler_invalid(lambda_event_invalid, lambda_context):
    response = app.lambda_handler(lambda_event_invalid, lambda_context)
    assert response['valid'] == False