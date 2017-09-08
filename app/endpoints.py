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
