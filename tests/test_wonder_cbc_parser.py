import sys

from defined_exceptions import NoDataException

reload(sys)
sys.setdefaultencoding('UTF-8')
from unittest import TestCase
from mock import Mock
from tests.samples import sample

from parsers.Wonder_cdc_parser import Wonder_cbc_parser


class TestWonder_cbc_parser(TestCase):

    text = '''
    Hepatitis (viral, acute), Type C, Probable previous 52 weeks maximum
    Hepatitis (viral, acute), Type C, Probable cummulative for 2017
    Hepatitis (viral, acute), Type C, Probable cummulative for 2016

    tab delimited data:
    UNITED STATES	8	44	134	1,770	2,398	3	18	80	690	830
    NEW ENGLAND	-	5	14	179	422	-	1	4	40	110
    Conn.	-	0	1	6	16	-	0	0	-	-
    Maine	-	0	2	15	17	-	0	1	5	10
    Mass.	-	4	14	154	384	-	1	4	35	100
    N.H.	-	0	0	-	-	-	0	0	-	-
    R.I.	-	0	0	-	-	-	0	0	-	-
    etwert
    wert
    we
    w'''
    def test_calculate_first_row(self):
        request = Mock()
        parser = Wonder_cbc_parser(request)
        fr = parser.calculate_first_row(self.text)
        self.assertEqual(fr,6)


    def test_calculate_skipfooter(self):
        request = Mock()
        parser = Wonder_cbc_parser(request)
        parser.region_length = 7
        sf = parser.calculate_skipfooter(self.text,5)
        self.assertEqual(sf,4)


    def test_weekly_data_2017(self):
        request = Mock()


        text = sample.sample1

        request.get = Mock(return_value=text)

        parser = Wonder_cbc_parser(request)

        df = parser.weekly_data('url.com/%s/%s','2017','01',1)

        suma = df['current_week'].sum()

        self.assertEqual(suma,24)

        self.assertEqual(len(df), 67)



    def test_weekly_data_2016(self):
        request = Mock()


        text = sample.sample2

        request.get = Mock(return_value=text)

        parser = Wonder_cbc_parser(request)

        df = parser.weekly_data('url.com/%s/%s','2016','01',11)


        suma = df['current_week'].sum()

        self.assertEqual(suma,90)

        self.assertEqual(len(df), 67)


    def test_weekly_no_data(self):
        request = Mock()


        text = sample.sample3

        request.get = Mock(return_value=text)

        parser = Wonder_cbc_parser(request)

        try:
            parser.weekly_data('url.com/%s/%s', '2016', '01', 11)
            self.assertEqual(1,2,'exception didnt rise')
        except :

            self.assertEqual(1,1,'exception raise')