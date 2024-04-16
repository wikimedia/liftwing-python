import unittest
from unittest.mock import patch
from src.liftwing_api.models import revertrisk

@patch('examples.revertrisk_examples.requests.post')
def test_revert_risk_example_test_200(self, mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {'key': 'value'}
    
    expectedResult = ("enwiki", 12345)
    
    self.assertEqual(expectedResult, {'key': 'value'})