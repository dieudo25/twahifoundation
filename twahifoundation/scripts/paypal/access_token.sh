curl -v https://api.sandbox.paypal.com/v1/oauth2/token \
   -H "Accept: application/json" \
   -H "Accept-Language: en_US" \
   -u "AdFvI06WTp1Ersw2irjLA7lfvcgRa0v4tQfCV0xrJ_aky_4Rrtzk8ytB3ePdDBOWlcvaKAYUHdD7sfRR:EELiYpqeALAU7I6hr8MWbSr3ldG0n6sYwzmju_xbnJAQHEO4RARMbegA3TXbJRagM40NI7Tzqd519i94" \
   -d "grant_type=client_credentials" \
   | python -m json.tool

curl -v -X GET https://api.sandbox.paypal.com/v1/reporting/transactions?start_date=2020-09-01T00:00:00-0700&end_date=2020-09-30T23:59:59 \
   -H "Content-Type: application/json" \
   -H "Authorization: Bearer A21AAKrXx5WgtoHPMXbOe2SjrlqR6yCLpPiCdLVu08y-r4xif2uUCxpLMfMikvZGUM9g_v1O0_1AsuUSs677g5ziQYbaNnW5Q"