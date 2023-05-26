from django.test import TestCase
from diabetes_prediction_app.views import model

class MyModelTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data or resources for the tests
        self.model = model

    def test_prediction_accuracy(self):
        # Set up test data
        input_data = [[1.0, 57.0, 0.0, 0.0, 3.0, 57.1, 6.5, 126.0]]
        expected_output = 1

        # Execute the model
        actual_output = self.model.predict(input_data)

        # Compare actual and expected output
        self.assertEqual(actual_output, expected_output)

    def test_model_performance(self):
        # Set up test data
        input_data = [[1.0, 50.0, 1.0, 0.0, 1.0, 27.32, 5.7, 260.0]]
        expected_output = 1

        # Execute the model
        actual_output = self.model.predict(input_data)

        # Compare actual and expected output
        self.assertEqual(actual_output, expected_output)
