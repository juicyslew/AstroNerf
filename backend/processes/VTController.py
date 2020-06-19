from backend.helpers.URLFuncs import RepURL
import asyncio

class VTController:
    def __init__(self):
        self.rep_url = RepURL();
        pass

    def LoadReps(self, stateID):
        rep_info = asyncio.run(self.rep_url.getAllReps(stateID))

        if (rep_info["status"] != "OK"):
            print("Status not \"OK\"")
            return -1

        senator_dict = {}
        for result in rep_info["results"]:
            print(result)
            senator_dict[result["id"]] = {"name":result["name"],
                                          "role":result["role"],
                                          "party":result["party"],
                                          "twitter":result["twitter_id"]}

        ret = {"senators":senator_dict}
        return ret

