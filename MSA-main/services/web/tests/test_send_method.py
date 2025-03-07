from typing import Any
from tests import settings
import aiohttp
import pytest
from app import producer


@pytest.mark.asyncio
async def test_send_producer_method(mock_producer_send_method: Any):
    async with aiohttp.ClientSession(base_url=settings.BASE_URL) as session:
        async with session.post(
            "/currency-info",
                json={"currency_char_code": "USD", "telegram_id": "1234"},
        ) as response:
            assert response.status == 200
    assert await producer.AIOWebProducer().send() == {"Method 'send'": "Was Called"}
