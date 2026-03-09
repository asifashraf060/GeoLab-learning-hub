import numpy as np
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.core.event import (
    Catalog, Event, Pick, WaveformStreamID, Origin)

client = Client("USGS")
catalog = client.get_events(
    starttime=UTCDateTime(2014, 7, 17),
    endtime=UTCDateTime(2014, 7, 19),
    latitude=46.2, longitude=-122.19,
    maxradius=0.25)

print(f"\n\nTotal stations: {catalog.count()}\n\n")
catalog.write("usgs_catalog.xml", format="QUAKEML")