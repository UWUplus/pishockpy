import unittest
import requests_mock

class TestPishockAPI(unittest.TestCase):
    def setUp(self):
        self.api_key = "api_key"
        self.username = "username"
        self.app_name = "app_name"
        self.sharecode = "sharecode"
        self.pishock_api = PishockAPI(self.api_key, self.username, self.sharecode, self.app_name)
    
    @requests_mock.mock()
    def test_shock(self, mock):
        mock.post(pishock_url, text="Operation Succeeded.")
        intensity = 0.5
        duration = 5
        result = self.pishock_api.shock(intensity, duration)
        self.assertTrue(result)
        
        mock.post(pishock_url, text="Intensity must be between 0 and 100")
        intensity = 1.5
        with self.assertRaises(ValueError) as context:
            self.pishock_api.shock(intensity, duration)
        self.assertEqual(str(context.exception), "The specified intensity was outside the permitted range.")
        
        mock.post(pishock_url, text="Duration must be between 0 and 15")
        intensity = 0.5
        duration = 20
        with self.assertRaises(ValueError) as context:
            self.pishock_api.shock(intensity, duration)
        self.assertEqual(str(context.exception), "The specified duration was outside the permitted range.")
    
    @requests_mock.mock()
    def test_minishock(self, mock):
        mock.post(pishock_url, text="Operation Succeeded.")
        intensity = 0.5
        result = self.pishock_api.minishock(intensity)
        self.assertTrue(result)
        
        mock.post(pishock_url, text="Intensity must be between 0 and 100")
        intensity = 1.5
        with self.assertRaises(ValueError) as context:
            self.pishock_api.minishock(intensity)
        self.assertEqual(str(context.exception), "The specified intensity was outside the permitted range.")
    
    @requests_mock.mock()
    def test_vibrate(self, mock):
        mock.post(pishock_url, text="Operation Succeeded.")
        intensity = 0.5
        duration = 5
        result = self.pishock_api.vibrate(intensity, duration)
        self.assertTrue(result)
        
        mock.post(pishock_url, text="Intensity must be between 0 and 100")
        intensity = 1.5
        with self.assertRaises(ValueError) as context:
            self.pishock_api.vibrate(intensity, duration)
        self.assertEqual(str(context.exception), "The specified intensity was outside the permitted range.")
        
        mock.post(pishock_url, text="Duration must be between 0 and 15")
