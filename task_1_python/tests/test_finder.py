import pytest
from src.finder import Finder


# Contains unit tests for the Finder class
class TestFinder():

    def test_find_with_empty_param(self):
        """Find the empty given token"""
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        finder = Finder(string_list)
        find = finder.find('')
        expected = []
        assert find == expected

    def test_find_with_none_param(self):
        """Find the empty given token"""
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        finder = Finder(string_list)
        find = finder.find(None)
        expected = []
        assert find == expected

    def test_find_with_original_order(self):
        """Find the given token regardless of order"""
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        finder = Finder(string_list)
        find = finder.find('asd')
        expected = ['asd', 'asdd']
        assert find == expected

    def test_find_with_changed_order(self):
        """Find the given token regardless of order"""
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        finder = Finder(string_list)
        find = finder.find('sad')
        expected = ['asd', 'asdd']
        assert find == expected

    def test_find_with_big_initialization(self):
        """Find the given token regardless of order"""
        string_list = ['North America', 'South America', 'Asia',
                       'Africa', 'Europe', 'Antartica', 'Australia']
        finder = Finder(string_list)
        find = finder.find('ac')
        expected_result = ['North America',
                           'South America', 'Africa', 'Antartica']
        assert find == expected_result

    def test_find_with_large_initialization(self):
        """Find the given token regardless of order with a big input"""
        string_list = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua & Deps', 'Argentina', 'Armenia', 'Australia', 'Austria',
                       'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
                       'Bosnia Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
                       'Cape Verde', 'Central African Rep', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Congo', 'Costa Rica', 'Croatia',
                       'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt',
                       'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia',
                       'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary',
                       'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan',
                       'Kazakhstan', 'Kenya', 'Kiribati', 'Korea North', 'Korea South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia',
                       'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar',
                       'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
                       'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
                       'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan',
                       'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania',
                       'Russian Federation', 'Rwanda', 'St Kitts & Nevis', 'St Lucia', 'Saint Vincent & the Grenadines', 'Samoa', 'San Marino',
                       'Sao Tome & Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
                       'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden',
                       'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad & Tobago', 'Tunisia',
                       'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay',
                       'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
        finder = Finder(string_list)
        find = finder.find('tan')
        expected_result = ['Afghanistan', 'Bhutan', 'Kazakhstan', 'Kyrgyzstan',
                           'Mauritania', 'Pakistan', 'Tajikistan', 'Turkmenistan', 'Uzbekistan', 'Vietnam']
        assert find == expected_result
