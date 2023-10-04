import json

from django.shortcuts import render


# Create your views here.


def dashboard(request):
    return render(request, "pages/logistics/home.html")


def fleet(request):
    data = {
        "vehicles": [
            {
                "id": 1,
                "number": "One",
                "name": "GJ 12 KW 1234",
                "location": "Ahmedabad, Gujarat",
                "progress": 67,
                "latitude": 23.0225,
                "longitude": 72.5714,
                "events": [
                    {
                        "driver": "Harjeet Singh",
                        "time": "Sep 03, 8:02 AM",
                        "type": "danger",
                        "behavior": "Harsh Braking"
                    },
                    {
                        "driver": "Harjeet Singh",
                        "time": "Sep 03, 10:34 AM",
                        "type": "warning",
                        "behavior": "Aggressive Acceleration"
                    },
                    {
                        "driver": "Harjeet Singh",
                        "time": "Sep 03, 3:54 PM",
                        "type": "warning",
                        "behavior": "Harsh Lane Change"
                    },
                    {
                        "driver": "Harjeet Singh",
                        "time": "Sep 03, 5:12 PM",
                        "type": "danger",
                        "behavior": "Harsh Braking"
                    }
                ]
            },
            {
                "id": 2,
                "number": "Two",
                "name": "MH 05 AB 5678",
                "location": "Mumbai, Maharashtra",
                "progress": 45,
                "latitude": 19.0760,
                "longitude": 72.8777,
                "events": [
                    {
                        "driver": "Rahul Sharma",
                        "time": "Sep 04, 9:15 AM",
                        "type": "warning",
                        "behavior": "Aggressive Lane Change"
                    },
                    {
                        "driver": "Rahul Sharma",
                        "time": "Sep 04, 11:47 AM",
                        "type": "danger",
                        "behavior": "Harsh Braking"
                    },
                    {
                        "driver": "Rahul Sharma",
                        "time": "Sep 04, 2:30 PM",
                        "type": "warning",
                        "behavior": "Aggressive Acceleration"
                    },
                    {
                        "driver": "Rahul Sharma",
                        "time": "Sep 04, 4:18 PM",
                        "type": "danger",
                        "behavior": "Harsh Braking"
                    }
                ]
            },
            {
                "id": 3,
                "number": "Three",
                "name": "DL 03 XY 9876",
                "location": "Delhi, NCR",
                "progress": 80,
                "latitude": 28.6139,
                "longitude": 77.2090,
                "events": [
                    {
                        "driver": "Suman Gupta",
                        "time": "Sep 05, 7:30 AM",
                        "type": "danger",
                        "behavior": "Harsh Braking"
                    },
                    {
                        "driver": "Suman Gupta",
                        "time": "Sep 05, 10:15 AM",
                        "type": "warning",
                        "behavior": "Aggressive Acceleration"
                    }
                ]
            },
            {
                "id": 4,
                "number": "Four",
                "name": "TN 09 CD 4321",
                "location": "Chennai, Tamil Nadu",
                "progress": 60,
                "latitude": 13.0827,
                "longitude": 80.2707,
                "events": [
                    {
                        "driver": "Priya Verma",
                        "time": "Sep 06, 9:45 AM",
                        "type": "danger",
                        "behavior": "Harsh Lane Change"
                    },
                    {
                        "driver": "Priya Verma",
                        "time": "Sep 06, 2:20 PM",
                        "type": "warning",
                        "behavior": "Aggressive Acceleration"
                    }
                ]
            },
            {
                "id": 5,
                "number": "Five",
                "name": "KA 08 PQ 7890",
                "location": "Bangalore, Karnataka",
                "progress": 55,
                "latitude": 12.9716,
                "longitude": 77.5946,
                "events": [
                    {
                        "driver": "Amit Patel",
                        "time": "Sep 07, 11:10 AM",
                        "type": "danger",
                        "behavior": "Harsh Braking"
                    },
                    {
                        "driver": "Amit Patel",
                        "time": "Sep 07, 3:55 PM",
                        "type": "warning",
                        "behavior": "Aggressive Lane Change"
                    }
                ],
            }

        ]
    }
    data['vehicles_json'] = json.dumps(data['vehicles'])
    return render(request, "pages/logistics/fleet.html", data)