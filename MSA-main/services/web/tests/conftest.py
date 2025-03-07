import pytest


@pytest.fixture
def mock_producer_send_method(mocker):
    mocker.patch(
        "app.producer.AIOWebProducer.send",
        return_value={"Method 'send'": "Was Called"},
    )
