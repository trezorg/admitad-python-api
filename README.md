admitad-python-api
==================

A Python wrapper around the Admitad API

Install
-------

Dependencies

* requests
* simplejson

PyAdmitad is not yet available on PyPI, we're waiting to have it a bit more
stable. Install by cloning from the GitHub repo:

    $ git clone git://github.com/trezorg/admitad-python-api.git
    $ cd admitad-python-api
    $ python setup.py test
    $ python setup.py build
    $ python setup.py install

    or just

    $ cp -r admitad-python-api/pyadmitad path/to/destination


Example
-------

    from pyadmitad import api

    client_id = ""
    client_secret = ""
    username = ""
    password = ""
    scope = "private_data"

    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )

    print client.Me.get()

    scope = "public_data"

    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )

    print client.WebsiteTypes.get()
    print client.WebsiteTypes.get(limit=2, offset=1)


API Items
-------------

### Me ###

    res = client.Me.get()


### WebsiteTypes ###

    res = client.WebsiteTypes.get()
    res = client.WebsiteTypes.get(limit=2, offset=1)


### WebsiteRegions ###

    res = client.WebsiteRegions.get()
    res = client.WebsiteRegions.get(limit=2, offset=1)

### SystemLanguages ###

    res = client.SystemLanguages.get()
    res = client.SystemLanguages.get(limit=2, offset=1)
    res = client.SystemLanguages.getOne(code='ru')

### SystemCurrencies ###

    res = client.SystemCurrencies.get()
    res = client.SystemCurrencies.get(limit=2, offset=1)


### AdvertiserServices ###

    res = client.AdvertiserServices.get()
    res = client.AdvertiserServices.get(limit=2, offset=1)
    res = client.AdvertiserServices.getOne(_id=2)
    res = client.AdvertiserServices.getOne(1)
    res = client.AdvertiserServices.getForKind(kind='website')
    res = client.AdvertiserServices.getForKind('website')
    res = client.AdvertiserServices.getForKindOne(_id=2, kind='website')
    res = client.AdvertiserServices.getForKindOne(2, 'website')


### CampaignCategories ###

    res = client.CampaignCategories.get()
    res = client.CampaignCategories.get(limit=2, offset=1)
    res = client.CampaignCategories.getOne(_id=2)
    res = client.CampaignCategories.getOne(2)

### Coupons ##

    res = client.Coupons.get()
    res = client.Coupons.get(order_by=date_start)
    res = client.Coupons.get(order_by=-date_end)
    res = client.Coupons.get(campaign=1, category=2)
    res = client.Coupons.get(filtering={'campaign': [1, 2]}, category=2)
    res = client.Coupons.getOne(_id=2)
    res = client.Coupons.getOne(2)

### CouponsForWebsite ###

    res = client.CouponsForWebsite.get(_id=2)
    res = client.CouponsForWebsite.get(2)
    res = client.CouponsForWebsite.get(2, order_by=date_start)
    res = client.CouponsForWebsite.get(2, campaign=1, category=2)
    res = client.CouponsForWebsite.get(2, filtering={'campaign': [1, 2]}, category=2)
    res = client.CouponsForWebsite.getOne(_id=2, c_id=1)
    res = client.CouponsForWebsite.getOne(2, 1)


### Websites ###

    res = client.Websites.get()
    res = client.Websites.get(status='new', campaign_status='active')
    res = client.Websites.getOne(_id=2)
    res = client.Websites.getOne(2)

### Statistics ###

###### Statistics by websites ######

    res = client.StatisticWebsites.get(website=1, campaign=1)
    res = client.StatisticWebsites.get(sub_id="ADS778")
    res = client.StatisticWebsites.get(limit=2)
    res = client.StatisticWebsites.get(date_start='01.01.2013')

###### Statistics by campaigns ######

    res = client.StatisticCampaigns.get()
    res = client.StatisticCampaigns.get(website=1, campaign=1)
    res = client.StatisticCampaigns.get(sub_id="ADS778")
    res = client.StatisticCampaigns.get(limit=2)
    res = client.StatisticCampaigns.get(date_start='01.01.2013')


###### Statistics by days ######

    res = client.StatisticDays.get()
    res = client.StatisticDays.get(website=1, campaign=1)
    res = client.StatisticDays.get(sub_id="ADS778")
    res = client.StatisticDays.get(limit=2)
    res = client.StatisticDays.get(date_start='01.01.2013')

###### Statistics by months ######

    res = client.StatisticMonths.get()
    res = client.StatisticMonths.get(website=1, campaign=1)
    res = client.StatisticMonths.get(sub_id="ADS778")
    res = client.StatisticMonths.get(limit=2)
    res = client.StatisticMonths.get(date_start='01.01.2013')


###### Statistics by actions ######

    res = client.StatisticActions.get()
    res = client.StatisticActions.get(date_start='01.01.2013')
    res = client.StatisticActions.get(website=1, campaign=1)
    res = client.StatisticActions.get(sub_id="ADS778")
    res = client.StatisticActions.get(limit=2)

###### Statistics by sub-ids ######

    res = client.StatisticSubIds.get()
    res = client.StatisticSubIds.get(date_start='01.01.2013')
    res = client.StatisticSubIds.get(sub_id="ADS778")
    res = client.StatisticSubIds.get(limit=2)


###### Statistics by sources ######

    res = client.StatisticSources.get()
    res = client.StatisticSources.get(date_start='01.01.2013')
    res = client.StatisticSources.get(limit=2)

###### Statistics by keywords ######

    res = client.StatisticKeywords.get()
    res = client.StatisticKeywords.get(date_start='01.01.2013')
    res = client.StatisticKeywords.get(limit=2)


Notes
------

It is possible to override the default response handler by passing handler as
a keyword argument to a client function call. For example:

    func = lambda x: (x, x)
    result = client.Me.get(handler=func)
