import unittest
from services.voices import *

class TestVoices(unittest.TestCase):

    def setUp(self):
        # Setup code to run before each test
        store_voice("Test Voice", "test_voice_id", 0.5, 0.8, 0.7, True)

    def tearDown(self):
        # Cleanup code to run after each test
        delete_voice("test_voice_id")

    def test_store_voice(self):
        self.assertTrue(voice_exists("test_voice_id"))

    def test_retrieve_voice(self):
        voice = retrieve_voice("test_voice_id")
        self.assertIsNotNone(voice)
        self.assertEqual(voice[0], "Test Voice")
        self.assertEqual(voice[1], "test_voice_id")
        self.assertEqual(voice[2], 0.5)
        self.assertEqual(voice[3], 0.8)
        self.assertEqual(voice[4], 0.7)
        self.assertEqual(voice[5], 1)

    def test_get_all_voices(self):
        voices = get_all_voices()
        self.assertGreater(len(voices), 0)

    def test_delete_voice(self):
        delete_voice("test_voice_id")
        self.assertFalse(voice_exists("test_voice_id"))

    def test_all_functionality(self):
        # Test storing the voice
        store_voice("Test Voice 2", "test_voice_id_2", 0.6, 0.9, 0.8, True)
        self.assertTrue(voice_exists("test_voice_id_2"))

        # Test retrieving the voice
        voice = retrieve_voice("test_voice_id_2")
        self.assertIsNotNone(voice)
        self.assertEqual(voice[0], "Test Voice 2")
        self.assertEqual(voice[1], "test_voice_id_2")
        self.assertEqual(voice[2], 0.6)
        self.assertEqual(voice[3], 0.9)
        self.assertEqual(voice[4], 0.8)
        self.assertEqual(voice[5], 1)

        # Test getting all voices
        voices = get_all_voices()
        self.assertGreater(len(voices), 1)

        # Test deleting the voice
        delete_voice("test_voice_id_2")
        self.assertFalse(voice_exists("test_voice_id_2"))
        
if __name__ == "__main__":
    unittest.main()