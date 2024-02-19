from src.econ_server_sdk_briandidthat.api import FredApi, FredOperation
from httpx import Response

url = "http://locahost:8080"
username = "tester"
api_key = "abcdefg"
headers = {"caller": username, "apiKey": api_key}

fred_api = FredApi(username, url, api_key)


def test_get_most_recent_observation(observation_mock, respx_mock):
    respx_mock.get(
        f"{url}/fred/observations/current/{FredOperation.AVERAGE_MORTGAGE_RATE}",
        params={"file_type": "json"},
        headers=headers,
    ).mock(return_value=Response(200, content=observation_mock.model_dump_json()))
    response = fred_api.get_most_recent_observation(
        FredOperation.AVERAGE_MORTGAGE_RATE, {"file_type": "json"}
    )

    assert response == observation_mock


def test_get_observations(fred_response_mock, respx_mock):
    respx_mock.get(
        f"{url}/fred/observations/{FredOperation.AVERAGE_MORTGAGE_RATE}",
        params={"file_type": "json"},
        headers=headers,
    ).mock(return_value=Response(200, content=fred_response_mock.model_dump_json()))
    response = fred_api.get_observations(
        FredOperation.AVERAGE_MORTGAGE_RATE, {"file_type": "json"}
    )

    assert len(response) == len(fred_response_mock.observations)
