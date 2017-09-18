
from collections import namedtuple
from faker import Faker

data = Faker()

Endpoint = namedtuple('Endpoint', 'name url properties docs data_function')

addresses = Endpoint(name='addresses',
                     url='/addresses/full_addresses/',
                     properties=('city', 'state_prov', 'postal_code',
                                 'country', 'street_address'),
                     docs='../docs/addresses/addresses.yml',
                     data_function=None
                     )

country = Endpoint(name='country', url='/addresses/countries/',
                   properties=(['country']),
                   docs='../docs/addresses/countries.yml',
                   data_function=data.country)


country_code = Endpoint(name='country_code', url='/addresses/country_codes/',
                        properties=(['country_code']),
                        docs='../docs/addresses/country_codes.yml',
                        data_function=None)


military_state = Endpoint(name='military_state', url='/addresses/military_states/',
                          properties=(['military_state']),
                          docs='../docs/addresses/military_states.yml',
                          data_function=None)

military_ship = Endpoint(name='military_ship', url='/addresses/military_ships/',
                         properties=(['military_ship']),
                         docs='../docs/addresses/military_ships.yml',
                         data_function=None)


state_abbr = Endpoint(name='state_abbr', url='/addresses/state_abbreviations/',
                      properties=(['state']),
                      docs='../docs/addresses/state_abbreviations.yml',
                      data_function=None)

street_address = Endpoint(name='street_address', url='/addresses/street_addresses/',
                          properties=(['street_address']),
                          docs='../docs/addresses/street_addresses.yml',
                          data_function=None)

companies = Endpoint(name='companies', url='/companies/',
                     properties=('company_name', 'slogan'),
                     docs='../docs/companies.yml',
                     data_function=None
                     )

license_plates = Endpoint(name='license_plates', url='/license_plates/',
                          properties=(['license_plate']),
                          docs='../docs/license_plates.yml',
                          data_function=None
                          )

people = Endpoint(name='people', url='/people/',
                  properties=('address', 'birthdate',
                              'company', 'mail', 'name', 'job'),
                  docs='../docs/people.yml',
                  data_function=None
                  )

credit_cards = Endpoint(name='credit_cards', url='/credit_cards/full_cards/',
                        properties=(['full_card_detail']),
                        docs='../docs/credit_card.yml',
                        data_function=None)


credit_card_security_code = Endpoint(name='credit_cards', url='/credit_cards/security_codes/',
                                     properties=(['security_code']),
                                     docs='../docs/security_code.yml',
                                     data_function=None)


url = Endpoint(name='url', url='/internet/url/',
               properties=(['url']),
               docs='../docs/internet/url.yml',
               data_function=None)

email = Endpoint(name='email', url='/internet/email/',
                 properties=(['email']),
                 docs='../docs/internet/email.yml',
                 data_function=None)

mac_address = Endpoint(name='mac_address', url='/internet/mac_addresses/',
                       properties=(['mac_address']),
                       docs='../docs/internet/mac_address.yml',
                       data_function=None)


username = Endpoint(name='username', url='/internet/usernames/',
                    properties=(['username']),
                    docs='../docs/internet/username.yml',
                    data_function=None)

image_url = Endpoint(name='image_url', url='/internet/image_urls/',
                     properties=(['url']),
                     docs='../docs/internet/image_urls.yml',
                     data_function=None)

ipv4 = Endpoint(name='ipv4', url='/internet/ipv4s/',
                properties=(['ip']),
                docs='../docs/internet/ipv4s.yml',
                data_function=None)

password = Endpoint(name='password', url='/internet/passwords/',
                    properties=(['password']),
                    docs='../docs/internet/passwords.yml',
                    data_function=None)


endpoint_list = [addresses, country, country_code,
                 military_state, military_state, state_abbr, street_address, companies,
                 license_plates, people, credit_cards, url, email, mac_address, username,
                 image_url, ipv4, password]
