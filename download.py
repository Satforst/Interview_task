import urllib.request
import urllib.error
import ast


class Download:
    def get_time(self):
        try:
            # download serverTimestamp and serverTimezoneOffset
            with urllib.request.urlopen("https://www.seznamzpravy.cz/pro/serverdate") as req:
                req_read = req.read()
                req_decoded = req_read.decode()
                req_dict = ast.literal_eval(req_decoded)
                return req_dict
        except urllib.error.URLError as error:
            print(error)
            return error
