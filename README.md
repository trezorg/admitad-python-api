admitad-python-api [![Build Status](https://travis-ci.org/janitor/admitad-python-api.svg?branch=master)](https://travis-ci.org/janitor/admitad-python-api)
==================

A Python wrapper around the [Admitad API](https://developers.admitad.com/en/)

Install
-------

    pip install admitad-api

Example
-------
```python
from pyadmitad import api

client_id = ""
client_secret = ""
scope = "private_data"

client = api.get_oauth_password_client(
    client_id,
    client_secret,
    scope
)

print(client.Me.get())
```

Tests
-----

    python setup.py test

API Items
-------------

### Me ###

    res = client.Me.get()


### Balance ###

    res = client.Balance.get()


### Types of websites ###

    res = client.WebsiteTypes.get()
    res = client.WebsiteTypes.get(limit=2, offset=1)


### Regions of websites ###

    res = client.WebsiteRegions.get()
    res = client.WebsiteRegions.get(limit=2, offset=1)

### Languages ###

    res = client.SystemLanguages.get()
    res = client.SystemLanguages.get(limit=2, offset=1)
    res = client.SystemLanguages.getOne(code='ru')

### Currencies ###

    res = client.SystemCurrencies.get()
    res = client.SystemCurrencies.get(limit=2, offset=1)


### Advertising services ###

    res = client.AdvertiserServices.get()
    res = client.AdvertiserServices.get(limit=2, offset=1)
    res = client.AdvertiserServices.getOne(_id=2)
    res = client.AdvertiserServices.getOne(1)
    res = client.AdvertiserServices.getForKind(kind='website')
    res = client.AdvertiserServices.getForKind('website')
    res = client.AdvertiserServices.getForKindOne(_id=2, kind='website')
    res = client.AdvertiserServices.getForKindOne(2, 'website')


### Categories of advertising campaigns ###

    res = client.CampaignCategories.get()
    res = client.CampaignCategories.get(limit=2, offset=1)
    res = client.CampaignCategories.getOne(_id=2)
    res = client.CampaignCategories.getOne(2)

### Coupons ##

###### List of coupons ######

    res = client.Coupons.get()
    res = client.Coupons.get(order_by=date_start)
    res = client.Coupons.get(order_by=-date_end)
    res = client.Coupons.get(campaign=1, category=2)
    res = client.Coupons.get(campaign=[1, 2], category=2)
    res = client.Coupons.getOne(_id=2)
    res = client.Coupons.getOne(2)

###### List of coupons for a website ######

    res = client.CouponsForWebsite.get(_id=2)
    res = client.CouponsForWebsite.get(2)
    res = client.CouponsForWebsite.get(2, order_by=date_start)
    res = client.CouponsForWebsite.get(2, campaign=1, category=2)
    res = client.CouponsForWebsite.get(2, campaign=[1, 2], category=2)
    res = client.CouponsForWebsite.getOne(_id=2, c_id=1)
    res = client.CouponsForWebsite.getOne(2, 1)


### Websites ###

##### List of websites #####

    res = client.Websites.get()
    res = client.Websites.get(status='new', campaign_status='active')
    res = client.Websites.getOne(_id=2)
    res = client.Websites.getOne(2)

##### Manage websites #####

###### Create website ######

    res = client.WebsitesManage.create(
        regions=['RU'],
        atnd_hits='20',
        atnd_visits='10',
        name='website1',
        language='ru',
        site_url='http://site.com',
        description='description',
        categories=['1', '2'],
        kind='website'
    )

###### Update website ######

    res = client.WebsitesManage.update(50, name='test', language='de')

###### Verify website ######

    res = client.WebsitesManage.verify(50)

###### Delete website ######

    res = client.WebsitesManage.delete(50)


### Statistics ###

###### Statistics by websites ######

    res = client.StatisticWebsites.get(website=1, campaign=1)
    res = client.StatisticWebsites.get(subid="ADS778")
    res = client.StatisticWebsites.get(limit=2)
    res = client.StatisticWebsites.get(date_start='01.01.2013')

###### Statistics by campaigns ######

    res = client.StatisticCampaigns.get()
    res = client.StatisticCampaigns.get(website=1, campaign=1)
    res = client.StatisticCampaigns.get(subid="ADS778")
    res = client.StatisticCampaigns.get(limit=2)
    res = client.StatisticCampaigns.get(date_start='01.01.2013')


###### Statistics by days ######

    res = client.StatisticDays.get()
    res = client.StatisticDays.get(website=1, campaign=1)
    res = client.StatisticDays.get(subid="ADS778")
    res = client.StatisticDays.get(limit=2)
    res = client.StatisticDays.get(date_start='01.01.2013')

###### Statistics by months ######

    res = client.StatisticMonths.get()
    res = client.StatisticMonths.get(website=1, campaign=1)
    res = client.StatisticMonths.get(subid="ADS778")
    res = client.StatisticMonths.get(limit=2)
    res = client.StatisticMonths.get(date_start='01.01.2013')


###### Statistics by actions ######

    res = client.StatisticActions.get()
    res = client.StatisticActions.get(date_start='01.01.2013')
    res = client.StatisticActions.get(website=1, campaign=1)
    res = client.StatisticActions.get(subid="ADS778")
    res = client.StatisticActions.get(subid2="ADS778")
    res = client.StatisticActions.get(limit=2)

###### Statistics by sub-ids ######

    res = client.StatisticSubIds.get()
    res = client.StatisticSubIds.get(date_start='01.01.2013')
    res = client.StatisticSubIds.get(subid="ADS778")
    res = client.StatisticSubIds.get(subid1="ADS778", sub_id_number=2)
    res = client.StatisticSubIds.get(limit=2)


###### Statistics by sources ######

    res = client.StatisticSources.get()
    res = client.StatisticSources.get(date_start='01.01.2013')
    res = client.StatisticSources.get(limit=2)

###### Statistics by keywords ######

    res = client.StatisticKeywords.get()
    res = client.StatisticKeywords.get(date_start='01.01.2013')
    res = client.StatisticKeywords.get(limit=2)


### Referrals ###

    res = client.Referrals.get()
    res = client.Referrals.get(limit=2)
    res = client.Referrals.getOne(_id=2)
    res = client.Referrals.getOne(2)


### Banners ###

###### List of banners ######

    res = client.Banners.get(_id=2)
    res = client.Banners.get(2)
    res = client.Banners.get(2, limit=2)


###### List of banners for a website ######

    res = client.BannersForWebsite.get(_id=2, w_id=3)
    res = client.BannersForWebsite.get(2, 3)
    res = client.BannersForWebsite.get(2, 3, limit=5)


### Campaigns ###

###### List of campaigns ######

    res = client.Campaigns.get()
    res = client.Campaigns.get(limit=2)
    res = client.Campaigns.getOne(2)

###### List of campaigns for a website ######

    res = client.CampaignsForWebsite.get(22)
    res = client.CampaignsForWebsite.get(limit=2)
    res = client.CampaignsForWebsite.getOne(6, 22)

###### Manage campaigns ######

    res = client.CampaignsManage.connect(6, 22)
    res = client.CampaignsManage.connect(c_id=6, w_id=22)
    res = client.CampaignsManage.disconnect(6, 22)
    res = client.CampaignsManage.disconnect(c_id=6, w_id=22)


### Payments ###


###### List of payment ######

    res = client.Payments.get()
    res = client.Payments.get(limit=2)
    res = client.Payments.getOne(2)

###### Manage payments ######

    res = client.PaymentsManage.create('USD')
    res = client.PaymentsManage.confirm(71)
    res = client.PaymentsManage.delete(71)


Notes
------

It is possible to override the default response handler by passing handler as
a keyword argument to a client function call. For example:

    func = lambda x: (x, x)
    result = client.Me.get(handler=func)
