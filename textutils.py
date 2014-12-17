class TextUtils:

    def convertRate(self, rate):
        rate = int(rate/4)
        return ("+"*(rate+1)+"-"*(4-rate))
