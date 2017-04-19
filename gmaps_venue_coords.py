import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='AIzaSyCsJnOb6VESNe9C-BXpkbrLppPA2ygCJMg')

HOWMANY = 500

venues = pd.read_csv("venues.txt", sep="\t")
venues = venues.iloc[:HOWMANY,:]

print("total venues: {}\nworking...".format(len(venues)))

def find_coords(st):

	attempted_search_res = gmaps.geocode(st)

	if attempted_search_res:
		res = attempted_search_res[0]["geometry"]["location"]
		return res
	else:
		return {'lat': None, 'lng': None}

res = pd.concat([venues, venues.v_addr.apply(lambda x: pd.Series(find_coords(x)))], axis=1)
res.to_csv("venue_coords_500_gmaps.csv", index=False, sep="\t")



