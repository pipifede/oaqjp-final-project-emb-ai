import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    Clase de pruebas unitarias para validar cada emoción dominante 
    de forma independiente.
    """
    def test_joy(self):
        """Prueba para la emoción dominante: Joy"""
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')
    def test_anger(self):
        """Prueba para la emoción dominante: Anger"""
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')
    def test_disgust(self):
        """Prueba para la emoción dominante: Disgust"""
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')
    def test_sadness(self):
        """Prueba para la emoción dominante: Sadness"""
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')
    def test_fear(self):
        """Prueba para la emoción dominante: Fear"""
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()

