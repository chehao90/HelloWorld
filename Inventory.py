import boto
from boto.mws.connection import MWSConnection

MarketPlaceID = 'MARKETPLACE_ID'
MerchantID = 'MERCHANT_ID'
AccessKeyID = 'ACCESS_KEY'
SecretKey = 'SECRET_KEY'

conn = MWSConnection(
    aws_access_key_id=AccessKeyID,
    aws_secret_access_key=SecretKey)

conn.SellerId = MerchantID
conn.Merchant = MerchantID
conn.MarketplaceId = MarketPlaceID

request = conn.list_inventory_supply(QueryStartDateTime='2015-04-01')
