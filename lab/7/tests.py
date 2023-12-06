import unittest
from service import UserService
from unittest.mock import patch


class TestGetPersonalProfile(unittest.TestCase):

    @patch('service.requests.get')
    def test_get_personal_profile_success(self, mock_get):
        username = "apple"
        expected_response = {"id": "5821462185"}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response
        result = UserService.get_personal_profile(username)
        self.assertEqual(result, expected_response)

    @patch('service.requests.get')
    def test_get_personal_profile_error_response(self, mock_get):
        username = "mryflotska"
        error_message = "User not found"
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {"message": error_message}
        with self.assertRaises(ValueError) as context:
            UserService.get_personal_profile(username)
        self.assertIn(error_message, str(context.exception))


if __name__ == '__main__':
    unittest.main()
