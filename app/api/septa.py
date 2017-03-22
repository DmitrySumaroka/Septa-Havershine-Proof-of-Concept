# -*- coding: utf-8 -*-
# @Author: dima
# @Date:   2017-02-07 12:59:01
# @Last Modified by:   Dima Sumaroka
# @Last Modified time: 2017-03-21 20:39:48

from app import app
from flask import render_template, request
import json
from requests import get
from haversine import haversine
import requests_cache

@app.route('/transit', methods=['GET'])
def transit():
    # Get Args that are necessary
    by_transit_id = request.args.get('transitSelect')
    search = request.args.get('search')
    search_closest = request.args.get('searchClosest')
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    radius = request.args.get('radius')

    # Set initial variables
    vehicle_list = []
    transit_ids = []
    closest_dist = None
    closest_marker = None
    point_to_search = None
    if search or search_closest:
        if lat is None or lng is None:
            responce = {
                "success": False,
                "responce": "Latitude or Longitude are missing"
            }
            return json.dumps(responce)

        if search and radius is None:
            responce = {
                "success": False,
                "responce": "Radius is missing"
            }
            return json.dumps(responce)
        elif radius is not None:
            radius = float(radius)
    # Cache for faster serarching since Septa is super slow
    requests_cache.install_cache()

    if request.args.get('noCached'):
        with requests_cache.disabled():
            transit_view_responce = get(app.septa_transit_view)
    else:
        transit_view_responce = get(app.septa_transit_view)

    if transit_view_responce.status_code == 200:
        transit_view_json = json.loads(transit_view_responce.text)
        today_date = next(iter(transit_view_json))

        if search or search_closest:
            point_to_search = (float(lat), float(lng))

        for vehicle_group in transit_view_json[today_date]:
            tran_id = next(iter(vehicle_group))
            transit_ids.append(tran_id)

            if by_transit_id:
                if by_transit_id == tran_id:
                    for vehicle in vehicle_group[tran_id]:
                        vehicle_list.append(vehicle)
            else:
                for vehicle in vehicle_group[tran_id]:
                    vehicle_lat = vehicle['lat']
                    vehicle_lng = vehicle['lng']
                    if search:
                        if haversine(point_to_search, (float(vehicle_lat), float(vehicle_lng)), miles=True) <= radius:
                            vehicle_list.append(vehicle)

                    elif search_closest:
                        dist = haversine(point_to_search, (float(vehicle_lat), float(vehicle_lng)))

                        if closest_dist is None or dist < closest_dist:
                            closest_dist = dist
                            closest_marker = vehicle
                    else:
                        vehicle_list.append(vehicle)
        if search_closest:
            vehicle_list.append(closest_marker)

        responce = {
            "success": True,
            "date": today_date,
            "vehicleList": vehicle_list,
            'transitIds': transit_ids
        }
    else:
        responce = {
            "success": False
        }
    return json.dumps(responce)