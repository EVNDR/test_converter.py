class test_temp_converter():
    def test_celsius_is_converted_to_farenheight(self):
        """
            farenheight= Celsius*9/5 + 32
        """
        actual = convert_celsius_to_farenheight(10) 
        expected = 50 
        self.assertEqual(actual,expected,'celsius should convert to Farenheight')  

