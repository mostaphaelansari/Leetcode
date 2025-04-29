class TweetCounts:

    def __init__(self):
        self.tweetcounts ={}
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweetcounts:
            self.tweetcounts[tweetName] = []
        self.tweetcounts[tweetName].append(time)


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        freq_map = {"minute": 60, "hour": 3600, "day": 86400}
        interval = freq_map[freq]
        size = (endTime - startTime) // interval + 1
        result = [0] * size

        if tweetName in self.tweetcounts:
            for time in self.tweetcounts[tweetName]:
                if startTime <= time <= endTime:
                    index = (time - startTime) // interval
                    result[index] += 1

        return result
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)