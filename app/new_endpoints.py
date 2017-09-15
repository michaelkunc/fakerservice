from collections import namedtuple

Endpoint = namedtuple('Endpoint', 'name url properties docs')

addresses = Endpoint(name='addresses',
                     url='/addresses/full_addresses/',
                     properties=('city', 'state_prov', 'postal_code',
                                 'country', 'street_address'),
                     docs='../docs/addresses/addresses.yml'
                     )

country = Endpoint(name='country',
                   url='/addresses/countries/',
                   properties=(['country']),
                   docs='../docs/addresses/countries.yml')

endpoint_list = [addresses, country]
