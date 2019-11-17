#!/usr/bin/env python
import app
import json

if __name__ == "__main__":
    offers = app.fetch_offers()
    offers = [offer for offer in offers]

    print(json.dumps(offers, cls=app.OfferEncoder))
