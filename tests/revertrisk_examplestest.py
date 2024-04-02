import unittest
from unittest.mock import patch
from examples.revertrisk_examples import revert_risk_api_request


class RevertRisk_ExamplesTest(unittest.TestCase):
    
    @patch('examples.revertrisk_examples.requests.post')
    def test_revert_risk_example_test_200(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'key': 'value'}
        
        result = revert_risk_api_request("en", 12345)
        
        self.assertEqual(result, {'key': 'value'})

    @patch('examples.revertrisk_examples.requests.post')
    def test_revert_risk_api_request_failure(self, mock_post):
        mock_post.return_value.status_code = 400
        
        with self.assertRaises(ValueError):
            revert_risk_api_request("en", 12345)

    @patch('examples.revertrisk_examples.requests.post')
    def test_revert_risk_api_request_empty_response(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {}

        result = revert_risk_api_request("en", 12345)

        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()
