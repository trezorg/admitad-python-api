admitad-python-api
==================

A Python wrapper around the Admitad API

Install
-------

Dependencies

* requests
* simplejson

Install by cloning from the GitHub repo:

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

    or

    client = api.get_oauth_client(access_token)

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


### Products ###

###### Categories of products ######

    res = client.ProductCategories.get()
    res = client.ProductCategories.get(limit=1, order_by=-name)
    res = client.ProductCategories.getOne(2)


###### Vendors of products ######

    res = client.ProductVendors.get()
    res = client.ProductVendors.get(limit=1, order_by=-name)
    res = client.ProductVendors.getOne(2)


###### Campaigns with products ######

    res = client.ProductCampaigns.get(22)
    res = client.ProductCampaigns.get(22, limit=1, order_by=-name)
    res = client.ProductCampaigns.getOne(22, 6)


###### Products for website ######

    res = client.Products.get(22)
    res = client.Products.get(22, limit=1)
    res = client.Products.get(22, limit=1, order_by=-price)
    res = client.Products.get(22, price_from=1000)
    res = client.ProductCampaigns.getOne(22, 2)


### Announcements ###


###### List of announcements ######

    res = client.Announcements.get()
    res = client.Announcements.get(limit=1, offset=2)
    res = client.Announcements.getOne(2)

###### Manage announcements ######

    res = client.AnnouncementsManage.delete(12)


Notes
------

It is possible to override the default response handler by passing handler as
a keyword argument to a client function call. For example:

    func = lambda x: (x, x)
    result = client.Me.get(handler=func)
