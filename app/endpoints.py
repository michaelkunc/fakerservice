
from collections import namedtuple
from faker import Faker

data = Faker()

Endpoint = namedtuple('Endpoint', 'name url properties docs data')

addresses = Endpoint(name='addresses',
                     url='/addresses/full_addresses/',
                     properties=('city', 'state_prov', 'postal_code',
                                 'country', 'street_address'),
                     docs='../docs/addresses/addresses.yml',
                     data={'street_address': data.street_address,
                           'city': data.city, 'state_prov': data.state_abbr,
                           'postal_code': data.postalcode, 'country': data.country}
                     )

country = Endpoint(name='country', url='/addresses/countries/',
                   properties=(['country']),
                   docs='../docs/addresses/countries.yml',
                   data=data.country)


country_code = Endpoint(name='country_code', url='/addresses/country_codes/',
                        properties=(['country_code']),
                        docs='../docs/addresses/country_codes.yml',
                        data=data.country_code)


military_state = Endpoint(name='military_state', url='/addresses/military_states/',
                          properties=(['military_state']),
                          docs='../docs/addresses/military_states.yml',
                          data=data.military_state)

military_ship = Endpoint(name='military_ship', url='/addresses/military_ships/',
                         properties=(['military_ship']),
                         docs='../docs/addresses/military_ships.yml',
                         data=data.military_ship)


state_abbr = Endpoint(name='state_abbr', url='/addresses/state_abbreviations/',
                      properties=(['state']),
                      docs='../docs/addresses/state_abbreviations.yml',
                      data=data.state_abbr)

street_address = Endpoint(name='street_address', url='/addresses/street_addresses/',
                          properties=(['street_address']),
                          docs='../docs/addresses/street_addresses.yml',
                          data=data.street_address)

companies = Endpoint(name='companies', url='/companies/',
                     properties=('company_name', 'slogan'),
                     docs='../docs/companies.yml',
                     data=None
                     )

license_plates = Endpoint(name='license_plates', url='/license_plates/',
                          properties=(['license_plate']),
                          docs='../docs/license_plates.yml',
                          data=data.license_plate
                          )

people = Endpoint(name='people', url='/people/',
                  properties=('address', 'birthdate',
                              'company', 'mail', 'name', 'job'),
                  docs='../docs/people.yml',
                  data=None
                  )

credit_cards = Endpoint(name='credit_cards', url='/credit_cards/full_cards/',
                        properties=(['full_card_detail']),
                        docs='../docs/credit_card.yml',
                        data=data.credit_card_full)


credit_card_security_code = Endpoint(name='credit_card_security_code', url='/credit_cards/security_codes/',
                                     properties=(['security_code']),
                                     docs='../docs/security_code.yml',
                                     data=data.credit_card_security_code)


credit_card_expire = Endpoint(name='credit_card_expire', url='/credit_cards/expiration_date/',
                              properties=(['expiration_date']),
                              docs='../docs/expiration_date.yml',
                              data=data.credit_card_expire)

credit_card_provider = Endpoint(name='credit_card_provider', url='/credit_cards/providers/',
                                properties=(['provider']),
                                docs='../docs/providers.yml',
                                data=data.credit_card_provider)


url = Endpoint(name='url', url='/internet/url/',
               properties=(['url']),
               docs='../docs/internet/url.yml',
               data=data.url)

email = Endpoint(name='email', url='/internet/email/',
                 properties=(['email']),
                 docs='../docs/internet/email.yml',
                 data=data.email)

mac_address = Endpoint(name='mac_address', url='/internet/mac_addresses/',
                       properties=(['mac_address']),
                       docs='../docs/internet/mac_address.yml',
                       data=data.mac_address)


username = Endpoint(name='username', url='/internet/usernames/',
                    properties=(['username']),
                    docs='../docs/internet/username.yml',
                    data=data.user_name)

image_url = Endpoint(name='image_url', url='/internet/image_urls/',
                     properties=(['url']),
                     docs='../docs/internet/image_urls.yml',
                     data=data.image_url)

ipv4 = Endpoint(name='ipv4', url='/internet/ipv4s/',
                properties=(['ip']),
                docs='../docs/internet/ipv4s.yml',
                data=None)

password = Endpoint(name='password', url='/internet/passwords/',
                    properties=(['password']),
                    docs='../docs/internet/passwords.yml',
                    data=None)

rgb_color = Endpoint(name='rgb_color', url='/colors/rgb_colors/',
                     properties=(['rgb_color']),
                     docs='../docs/colors/rgb_colors.yml',
                     data=data.rgb_color)

color_name = Endpoint(name='color_name', url='/colors/color_names/',
                      properties=(['color_name']),
                      docs='../docs/colors/color_names.yml',
                      data=data.color_name)

rgb_css_color = Endpoint(name='rgb_css_color', url='/colors/rgb_css_colors/',
                         properties=(['rgb_css_color']),
                         docs='../docs/colors/rgb_css_colors.yml',
                         data=data.rgb_css_color)

hex_color = Endpoint(name='hex_color', url='/colors/hex_colors/',
                     properties=(['hex_color']),
                     docs='../docs/colors/hex_colors.yml',
                     data=data.hex_color)

safe_hex_color = Endpoint(name='safe_hex_color', url='/colors/safe_hex_colors/',
                          properties=(['safe_hex_color']),
                          docs='../docs/colors/safe_hex_colors.yml',
                          data=data.safe_hex_color)

safe_color_name = Endpoint(name='safe_color_name', url='/colors/safe_color_names/',
                           properties=(['safe_color_name']),
                           docs='../docs/colors/safe_color_names.yml',
                           data=data.safe_color_name)

ean8 = Endpoint(name='ean8', url='/barcode/ean8/',
                properties=(['ean8']),
                docs='../docs/barcode/ean8.yml',
                data=data.ean8)


ean13 = Endpoint(name='ean13', url='/barcode/ean13/',
                 properties=(['ean13']),
                 docs='../docs/barcode/ean13.yml',
                 data=data.ean13)

currency = Endpoint(name='currency', url='/currencies/currency_codes/',
                    properties=(['currency']),
                    docs='../docs/currencies/currency_codes.yml',
                    data=data.currency_code)

crypto_currency = Endpoint(name='crypto_currency', url='/currencies/crypto_currency_codes/',
                           properties=(['crypto_currency']),
                           docs='../docs/currencies/crypto_currency_codes.yml',
                           data=data.cryptocurrency_code)

file_extension = Endpoint(name='file_extension', url='/files/file_extensions/',
                          properties=(['file_extension']),
                          docs='../docs/files/file_extensions.yml',
                          data=data.file_extension)

file_path = Endpoint(name='file_path', url='/files/file_paths/',
                          properties=(['file_path']),
                          docs='../docs/files/file_paths.yml',
                          data=data.file_path)

mime_type = Endpoint(name='mime_type', url='/files/mime_types/',
                          properties=(['mime_type']),
                          docs='../docs/files/mime_types.yml',
                          data=data.mime_type)

file_name = Endpoint(name='file_name', url='/files/file_names/',
                          properties=(['file_name']),
                          docs='../docs/files/file_names.yml',
                          data=data.file_name)

ssn = Endpoint(name='ssn', url='/ssns/',
               properties=(['ssn']),
               docs='../docs/ssn.yml',
               data=data.ssn)


job = Endpoint(name='job', url='/jobs/',
               properties=(['job']),
               docs='../docs/jobs.yml',
               data=data.job)

words = Endpoint(name='words', url='/lorem/words/',
                 properties=(['words']),
                 docs='../docs/lorem/words.yml',
                 data=data.words)

paragraphs = Endpoint(name='paragraphs', url='/lorem/paragraphs/',
                      properties=(['paragraphs']),
                      docs='../docs/lorem/paragraphs.yml',
                      data=data.paragraphs)

sentence = Endpoint(name='sentence', url='/lorem/sentences/',
                    properties=(['sentence']),
                    docs='../docs/lorem/sentence.yml',
                    data=data.sentence)

word = Endpoint(name='word', url='/lorem/word/',
                properties=(['word']),
                docs='../docs/lorem/word.yml',
                data=data.word)

text = Endpoint(name='text', url='/lorem/text/',
                properties=(['text']),
                docs='../docs/lorem/text.yml',
                data=data.text)

phone_number = Endpoint(name='phone_number', url='/phone_numbers/',
                        properties=(['phone_number']),
                        docs='../docs/phone_number.yml',
                        data=data.phone_number)


sha1 = Endpoint(name='sha1', url='/sha1s/',
                properties=(['sha1']),
                docs='../docs/sha1.yml',
                data=data.sha1)


boolean = Endpoint(name='boolean', url='/booleans/',
                   properties=(['boolean']),
                   docs='../docs/boolean.yml',
                   data=data.boolean)

locale = Endpoint(name='locale', url='/locales/',
                  properties=(['locale']),
                  docs='../docs/locale.yml',
                  data=data.locale)

language_code = Endpoint(name='language_code', url='/language_codes/',
                         properties=(['language_code']),
                         docs='../docs/language_code.yml',
                         data=data.language_code)

sha256 = Endpoint(name='sha256', url='/sha256/',
                  properties=(['sha256']),
                  docs='../docs/sha256.yml',
                  data=data.sha256)

uuid4 = Endpoint(name='uuid4', url='/uuid4/',
                 properties=(['uuid4']),
                 docs='../docs/uuid4.yml',
                 data=data.uuid4)

md5 = Endpoint(name='md5', url='/md5/',
               properties=(['md5']),
               docs='../docs/md5.yml',
               data=data.md5)

null_boolean = Endpoint(name='null_boolean', url='/null_boolean/',
                        properties=(['null_boolean']),
                        docs='../docs/null_boolean.yml',
                        data=data.null_boolean)


endpoint_list = (addresses, country, country_code,
                 military_state, military_ship, state_abbr, street_address, companies,
                 license_plates, people, credit_cards, credit_card_security_code, credit_card_expire, credit_card_provider, url, email, mac_address, username,
                 image_url, ipv4, password, rgb_color, color_name, rgb_css_color, hex_color, safe_hex_color, safe_color_name, ean8,
                 ean13, currency, crypto_currency, file_extension, file_path, mime_type, file_name,
                 ssn, job, words, paragraphs, sentence, word, text, phone_number, sha1, boolean,
                 locale, language_code, sha256, uuid4, md5, null_boolean)
