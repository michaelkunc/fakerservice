
from collections import namedtuple

Endpoint = namedtuple('Endpoint', 'url properties docs')

addresses = Endpoint(url='/addresses/',
                     properties=('city', 'state_prov', 'postal_code',
                                 'country', 'street_address'),
                     docs='../docs/addresses.yml'
                     )

companies = Endpoint(url='/companies/',
                     properties=('company_name', 'slogan'),
                     docs='../docs/companies.yml'
                     )

license_plates = Endpoint(url='/license_plates/',
                          properties=(['license_plate']),
                          docs='../docs/license_plates.yml'
                          )

people = Endpoint(url='/people/',
                  properties=('address', 'birthdate',
                              'company', 'mail', 'name', 'job'),
                  docs='../docs/people.yml'
                  )

credit_cards = Endpoint(url='/credit_cards/',
                        properties=(['full_card_detail']),
                        docs='../docs/credit_card.yml')


url = Endpoint(url='/internet/url/',
               properties=(['url']),
               docs='../docs/internet/url.yml')

email = Endpoint(url='/internet/email/',
                 properties=(['email']),
                 docs='../docs/internet/email.yml')

mac_address = Endpoint(url='/internet/mac_addresses/',
                       properties=(['mac_address']),
                       docs='../docs/internet/mac_address.yml')


username = Endpoint(url='/internet/usernames/',
                    properties=(['username']),
                    docs='../docs/internet/username.yml')

image_url = Endpoint(url='/internet/image_urls/',
                     properties=(['url']),
                     docs='../docs/internet/image_urls.yml')

ipv4 = Endpoint(url='/internet/ipv4s/',
                properties=(['ip']),
                docs='../docs/internet/ipv4s.yml')

password = Endpoint(url='/internet/passwords/',
                    properties=(['password']),
                    docs='../docs/internet/passwords.yml')
