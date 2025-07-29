import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
__rapidapi_url__ = 'https://rapidapi.com/3b-data-3b-data-default/api/airbnb13'

mcp = FastMCP('airbnb13')

@mcp.tool()
def autocomplete(query: Annotated[str, Field(description='Query parameter')]) -> dict: 
    '''Find locations by query'''
    url = 'https://airbnb13.p.rapidapi.com/autocomplete'
    headers = {'x-rapidapi-host': 'airbnb13.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_by_location(location: Annotated[str, Field(description='Location (city, region, suburb, etc.)')],
                       checkin: Annotated[Union[str, datetime], Field(description='Check-in date')],
                       checkout: Annotated[Union[str, datetime], Field(description='Check-out date')],
                       adults: Annotated[Union[int, float], Field(description='Number of adult guests (13 years and over) Default: 1')],
                       children: Annotated[Union[int, float, None], Field(description='Number of children (2-12 years) Default: 0')] = None,
                       infants: Annotated[Union[int, float, None], Field(description='Number of infants (under 2 years) Default: 0')] = None,
                       pets: Annotated[Union[int, float, None], Field(description='Number of pets Default: 0')] = None,
                       page: Annotated[Union[int, float, None], Field(description='Page of results returned Allowed values: 1-8 Default: 1')] = None,
                       currency: Annotated[Union[str, None], Field(description='Price currency, default: USD')] = None,
                       min_beds: Annotated[Union[int, float, None], Field(description='Minimum number of beds')] = None,
                       min_bedrooms: Annotated[Union[int, float, None], Field(description='Minimum number of bedrooms')] = None) -> dict: 
    '''Find rooms at a location'''
    url = 'https://airbnb13.p.rapidapi.com/search-location'
    headers = {'x-rapidapi-host': 'airbnb13.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'checkin': checkin,
        'checkout': checkout,
        'adults': adults,
        'children': children,
        'infants': infants,
        'pets': pets,
        'page': page,
        'currency': currency,
        'min_beds': min_beds,
        'min_bedrooms': min_bedrooms,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_by_geo_coordinates(ne_lat: Annotated[Union[int, float], Field(description='Latitude of the northeastern corner of the search area Default: 52.51')],
                              ne_lng: Annotated[Union[int, float], Field(description='Longitude of the northeastern corner of the search area Default: 13.41')],
                              sw_lat: Annotated[Union[int, float], Field(description='Latitude of the southwestern corner of the search area Default: 52.41')],
                              sw_lng: Annotated[Union[int, float], Field(description='Longitude of the southwestern corner of the search area Default: 13.31')],
                              checkin: Annotated[Union[str, datetime], Field(description='Check-in date')],
                              checkout: Annotated[Union[str, datetime], Field(description='Check-out date')],
                              adults: Annotated[Union[int, float], Field(description='Number of adult guests (13 years and over) Default: 1')],
                              children: Annotated[Union[int, float, None], Field(description='Number of children (2-12 years) Default: 0')] = None,
                              infants: Annotated[Union[int, float, None], Field(description='Number of infants (under 2 years) Default: 0')] = None,
                              pets: Annotated[Union[int, float, None], Field(description='Number of pets Default: 0')] = None,
                              page: Annotated[Union[int, float, None], Field(description='Returned page of results. Allowed values: 1-8 Default: 1')] = None,
                              currency: Annotated[Union[str, None], Field(description='Price currency, default: USD')] = None,
                              min_beds: Annotated[Union[int, float, None], Field(description='Minimum number of beds')] = None,
                              min_bedrooms: Annotated[Union[int, float, None], Field(description='Minimum number of bedrooms')] = None) -> dict: 
    '''Find rooms in a rectangles bounded by provided coordinates'''
    url = 'https://airbnb13.p.rapidapi.com/search-geo'
    headers = {'x-rapidapi-host': 'airbnb13.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ne_lat': ne_lat,
        'ne_lng': ne_lng,
        'sw_lat': sw_lat,
        'sw_lng': sw_lng,
        'checkin': checkin,
        'checkout': checkout,
        'adults': adults,
        'children': children,
        'infants': infants,
        'pets': pets,
        'page': page,
        'currency': currency,
        'min_beds': min_beds,
        'min_bedrooms': min_bedrooms,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_listing_details(listing_id: Annotated[str, Field(description='The ID of Airbnb listing')],
                        checkin: Annotated[Union[str, datetime, None], Field(description='Check-in date')] = None,
                        checkout: Annotated[Union[str, datetime, None], Field(description='Check-out date')] = None,
                        adults: Annotated[Union[int, float, None], Field(description='Number of adult guests (13 years and over) Default: 0')] = None,
                        children: Annotated[Union[int, float, None], Field(description='Number of children (2-12 years)')] = None,
                        infants: Annotated[Union[int, float, None], Field(description='Number of infants (under 2 years)')] = None,
                        pets: Annotated[Union[int, float, None], Field(description='Number of pets')] = None,
                        locale: Annotated[Union[str, None], Field(description='Locale, default: en')] = None,
                        currency: Annotated[Union[str, None], Field(description='Price currency, default: USD')] = None) -> dict: 
    '''Get listing details, availability and price for selected interval'''
    url = 'https://airbnb13.p.rapidapi.com/room'
    headers = {'x-rapidapi-host': 'airbnb13.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'listing_id': listing_id,
        'checkin': checkin,
        'checkout': checkout,
        'adults': adults,
        'children': children,
        'infants': infants,
        'pets': pets,
        'locale': locale,
        'currency': currency,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def calendar(room_id: Annotated[str, Field(description='')],
             currency: Annotated[Union[str, None], Field(description='Price currency, default: USD')] = None,
             year: Annotated[Union[str, None], Field(description='Calendar year, default: current year')] = None,
             month: Annotated[Union[str, None], Field(description='Calendar month, default: current month')] = None,
             count: Annotated[Union[str, None], Field(description='Returned number of months, default: 12, max: 12')] = None) -> dict: 
    '''Returns availability and prices of a listing'''
    url = 'https://airbnb13.p.rapidapi.com/calendar'
    headers = {'x-rapidapi-host': 'airbnb13.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'room_id': room_id,
        'currency': currency,
        'year': year,
        'month': month,
        'count': count,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
async def get_full_airbnb_list(
    location: Annotated[str, Field(description='Location (city, region, suburb, etc.)')],
    checkin: Annotated[Union[str, datetime], Field(description='Check-in date')],
    checkout: Annotated[Union[str, datetime], Field(description='Check-out date')],
    adults: Annotated[Union[int, float], Field(description='Number of adult guests (13 years and over). Default: 1')],
    children: Annotated[Union[int, float, None], Field(description='Number of children (2-12 years). Default: 0')] = None,
    infants: Annotated[Union[int, float, None], Field(description='Number of infants (under 2 years). Default: 0')] = None,
    pets: Annotated[Union[int, float, None], Field(description='Number of pets. Default: 0')] = None,
    currency: Annotated[Union[str, None], Field(description='Price currency. Default: USD')] = None,
    min_beds: Annotated[Union[int, float, None], Field(description='Minimum number of beds')] = None,
    min_bedrooms: Annotated[Union[int, float, None], Field(description='Minimum number of bedrooms')] = None,
) -> dict:
    """Fetch up to 200 Airbnb listings for the given search by fetching the first 5 pages in parallel (page size is 40)."""
    url = 'https://airbnb13.p.rapidapi.com/search-location'
    headers = {'x-rapidapi-host': 'airbnb13.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}

    import httpx, asyncio
    logged_pages = set()
    async def fetch_page(page):
        params = {
            'location': location,
            'checkin': checkin,
            'checkout': checkout,
            'adults': adults,
            'children': children,
            'infants': infants,
            'pets': pets,
            'page': page,
            'currency': currency,
            'min_beds': min_beds,
            'min_bedrooms': min_bedrooms,
        }
        params = {k: v for k, v in params.items() if v is not None}
        logger.info(f"Requesting page {page} with params: {params}")
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, headers=headers, params=params)
            result = resp.json()
        if page not in logged_pages:
            if isinstance(result, dict):
                logger.info(f"Page {page} returned {len(result.get('results', []))} items.")
            else:
                logger.info(f"Page {page} returned non-dict result.")
            logged_pages.add(page)
        return result

    async def gather_first_5_pages():
        # Fetch pages 1-5 in parallel
        tasks = [fetch_page(page) for page in range(1, 6)]
        results = await asyncio.gather(*tasks)
        all_results = []
        for result in results:
            items = result.get('results', []) if isinstance(result, dict) else []
            all_results.extend(items)
        return {'all_results': all_results[:200]}

    return await gather_first_5_pages()


if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
