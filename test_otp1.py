import OTP1 as otp
import unittest
import pytest

class Tests(unittest.TestCase):

    def test_generateOtp(self):
        result = otp.generateOtp()
        expected_len = 6

        isint = result.isdigit()
        expec_isint = True
        
        self.assertEqual(len(result), expected_len)
        self.assertEqual(isint, expec_isint)

    def test_validateEmailID(self):

        result = otp.validateEmailID("test@gma.ilcom")
        expected = True

        self.assertEqual(result, expected)




if __name__ == "__main__":
    pytest.main()


