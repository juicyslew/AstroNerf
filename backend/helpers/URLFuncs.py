from backend.auth.key import publica_key
import requests
import asyncio
import concurrent.futures

#threads for requests
executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

class RepURL:
	""" Class to get representative information.
	"""

	def __init__(self):
		self.key = publica_key
		self.headers = {"X-API-Key":publica_key}
		self.stateBase = "https://api.propublica.org/congress/v1/members/{chamber}/{state}/current.json"
		self.stateDistbase = "https://api.propublica.org/congress/v1/members/{chamber}/{state}/{district}/current.json"

	async def getAllReps(self, stateID, districtID = -1):
		url = ""
		if (districtID == -1):
			url = self.stateBase.format(chamber="senate",
										state=stateID)
		else:
			url = self.stateDistBase.format(chamber="senate",
								state=stateID,
								district=districtID)
		print(url)
		loop = asyncio.get_event_loop()
		req = await loop.run_in_executor(executor, lambda: requests.get(url, headers=self.headers))
		req = req.json()
		print(req)
		return req